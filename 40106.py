#admin
#leaned on https://cryptography.io/en/latest/fernet/ and chatgpt to improve error handling and try-catch

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

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
def encrypt_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
        print("File successfully encrypted.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

#    Decrypt the target file if in mode 2.
#        Delete the encrypted target file and replace it entirely with the decrypted version.

def decrypt_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
        print("File successfully decrypted.")
    except Exception as e:
        print(f"Error decrypting file: {e}")


#    Encrypt the string if in mode 3.
#        Print the ciphertext to the screen.

def encrypt_message(message):
    try:
        encrypted_message = f.encrypt(message.encode())
        print("Successfully encrypted:", encrypted_message)
    except Exception as e:
        print(f"Error encrypting message: {e}")

#    Decrypt the string if in mode 4.
#        Print the cleartext to the screen.

def decrypt_message(encrypted_message):
    try:
        decrypted_message = f.decrypt(encrypted_message).decode()
        print("Successfully decrypted:", decrypted_message)
    except Exception as e:
        print(f"Error decrypting message: {e}")

##########################################################################################
#    If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#    If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

def main():
    choice = main_menu()
    if choice == '1':
        file1 = input("Enter a file: ")
        encrypt_file(file1)
    elif choice == '2':
        file2 = input("Enter a file: ")
        decrypt_file(file2)
    elif choice == '3':
        string3 = input("Enter a string: ")
        encrypt_message(string3)
    elif choice == '4':
        string4 = input("Enter a string: ")
        decrypt_message(string4)
    else:
        print("Invalid choice. Please select a valid option.")

##########################################################################################
if __name__ == "__main__":
    main()
