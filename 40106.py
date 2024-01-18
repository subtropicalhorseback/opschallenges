#admin
#leaned on https://cryptography.io/en/latest/fernet/ and chatgpt to improve error handling and try-catch
#also got some gpt help https://chat.openai.com/share/8005ea45-f239-4220-a75c-790de555191

import os
from cryptography.fernet import Fernet

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

#    Prompt the user to select a mode:
#        Encrypt a file (mode 1)
#        Decrypt a file (mode 2)
#        Encrypt a message (mode 3)
#        Decrypt a message (mode 4)

def main_menu():
    print("Select an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    choice = input("Enter your choice (1-4): ")
    
    return choice

##########################################################################################
#Depending on the selection, perform one of the below functions. You’ll need to create four functions:

#    Encrypt the target file if in mode 1.
#        Delete the existing target file and replace it entirely with the encrypted version.

def encrypt_file(filepath, fernet):
    try:
        with open(filepath, 'rb') as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
        print("File successfully encrypted.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

#    Decrypt the target file if in mode 2.
#        Delete the encrypted target file and replace it entirely with the decrypted version.

def decrypt_file(filepath, fernet):
    try:
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
        print("File successfully decrypted.")
    except Exception as e:
        print(f"Error decrypting file: {e}")


#    Encrypt the string if in mode 3.
#        Print the ciphertext to the screen.

def encrypt_message(message, fernet):
    try:
        encrypted_message = fernet.encrypt(message.encode())
        print("Successfully encrypted:", encrypted_message)
    except Exception as e:
        print(f"Error encrypting message: {e}")

#    Decrypt the string if in mode 4.
#        Print the cleartext to the screen.

def decrypt_message(encrypted_message, fernet):
    try:
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        print("Successfully decrypted:", decrypted_message)
    except Exception as e:
        print(f"Error decrypting message: {e}")

##########################################################################################
#    If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#    If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

def main():
    key = generate_or_load_key()
    fernet = Fernet(key)
    choice = main_menu()

    if choice == '1':
        filepath = input("Enter a file: ")
        encrypt_file(filepath, fernet)
    elif choice == '2':
        filepath = input("Enter a file: ")
        decrypt_file(filepath, fernet)
    elif choice == '3':
        message = input("Enter a message: ")
        encrypt_message(message, fernet)
    elif choice == '4':
        encrypted_message = input("Enter an encrypted message: ")
        decrypt_message(encrypted_message, fernet)
    else:
        print("Invalid choice. Please select a valid option.")

##########################################################################################
if __name__ == "__main__":
    main()