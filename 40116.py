#!/usr/bin/python3


# imports
import ssl
import nltk
from nltk.corpus import words
import time
import wget
import tarfile
import gzip
import shutil


# nltk word download ssl connection
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#################################################################################################
#################################################################################################        



#################################################################################################

# function to make a list of words from the ext file rockyou - some is from warmup
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
        
def mode1PrepB(password_list):
    for ThisIsAnAssignedVariable in password_list:
        print(ThisIsAnAssignedVariable)
        time.sleep(0.5)


def mode1():
    print("\nMode 1: Offensive; Dictionary Iterator activated.\n")
    password_list = mode1PrepA()
    mode1PrepB(password_list)
    
    # function to check user input against nltk wordlist

#################################################################################################
# function for nltk to get words from online dict and save to a wordlist - from the warmup
def mode2PrepA():
    print("Checking for nltk dictionary package \n")
    time.sleep(1)
    nltk.download('words')
    word_list = words.words()
    return word_list

# function to check user input against nltk wordlist - from the warmup
def mode2PrepB(external_words):
    user_answer = input("\nEnter a word: ")
    time.sleep(1.5)
    if user_answer in external_words:
        print("\nthe word is in the dictionary")
    else:
        print("\nthe word is not in the dictionary")

# automation - https://chat.openai.com/share/16ec755d-5281-4d78-8987-090fb0954ed9
def mode2():
    print("\nMode 2: Defensive; Password Recognized activated.\n")
    external_words = mode2PrepA()
    mode2PrepB(external_words)

#################################################################################################


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1 - Mode 1: Offensive; Dictionary Iterator")
        print("2 - Mode 2: Defensive; Password Recognized")
        print("n/q - Quit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == '1':
            mode1()
        elif choice == '2':
            mode2()
        elif choice in ['n', 'q']:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 'n', or 'q'.")

if __name__ == "__main__":
    main_menu()
