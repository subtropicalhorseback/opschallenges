#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

##########################################################################################
##########################################################################################

# borrowed this function from classmate Nathalie Abdallah after she demonstrated it during class today (1/17) - https://github.com/nataliabdallah/code-fellows-ops-challenges/blob/main/index/401_6_challenge.py
def generate_or_load_key():
    if os.path.isfile("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

##########################################################################################

def main_menu():
    print("Select an option:")
    print("1. Recursively encrypt a directory")
    print("2. Recursively decrypt a directory")

    choice = input("Enter your choice (1 or 2): ")
    
    return choice

##########################################################################################

def getList():
    mainList = []
    here = input("Enter the highest level directory to begin the process: ")

    # leaning on https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/

    try:
        for root, dirs, files in os.walk(here):
            for file_name in files:
                full_path = os.path.join(root, file_name)
                mainList.append((full_path))
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    return mainList

##########################################################################################

def encrypt_dir(fileList, fernet):
    try:
        for filename in fileList:
            with open(filename, 'rb') as file:
                file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
            with open(filename, 'wb') as file:
                file.write(encrypted_data)
            print(filename,"successfully encrypted.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

##########################################################################################
        
def decrypt_dir(fileList, fernet):
    try:
        for filename in fileList:
            with open(filename, 'rb') as file:
                file_data = file.read()
            decrypted_data = fernet.decrypt(file_data)
            with open(filename, 'wb') as file:
                file.write(decrypted_data)
            print(filename,"successfully decrypted.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

##########################################################################################

def main():
    key = generate_or_load_key()
    fernet = Fernet(key)

    fileList = getList()
    print("Targeting the following list:",fileList)

    choice = main_menu()

    if choice == '1':
        encrypt_dir(fileList, fernet)

    elif choice == '2':
        decrypt_dir(fileList, fernet)

    else:
        print("Invalid choice. Please select a valid option.")

##########################################################################################
if __name__ == "__main__":
    main()


    
