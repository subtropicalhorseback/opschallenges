#!/usr/bin/python3'

import hashlib, os, time
from datetime import datetime



#
# Prompt the user for a directory to search in.
# recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
## Generate the file’s MD5 hash using Hashlib.
## Assign the MD5 hash to a variable.
## Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.
# The script must successfully execute on both Ubuntu and Windows 10
# Add logging capabilities to this script.  All data output to the screen should also append to a log file.
#

print("starting 40123\n")

# helper function for dir search
def list_directory_contents(directory):
    
    # print content list
    print(f"\nContents of '{directory}':")
    
    # actually make the list with os.
    contents = os.listdir(directory)

    # sort them so it's readable
    contents.sort()  # Sort the contents alphabetically
    
    # iterate through printing the list items
    for i, content in enumerate(contents, 1):
        print(f"{i}. {content}")
    print()

# main dir search function
def search_for_directory():
    # start from right here
    current_directory = os.getcwd()  

    # open a loop for starting point
    while True:
        
        # take user input starting point
        input_path = input("Enter the base directory to start the search (e.g., /home/user/Documents) or '.' for the current directory: ").strip()
        
        # home is where the heart is
        if input_path == '.':
            break

        # if the vibe is right then 
        elif os.path.isdir(input_path):

            # go ahead and say that to me one more time (conv to abs path)
            current_directory = os.path.abspath(input_path)
            break
        
        # english, do you speak it
        else:
            print("Invalid input. Please enter a valid directory path.")

    # set your pick as empty
    selected_directory = None

    # another loop for selection
    while True:

        # this is just a fancy LS
        list_directory_contents(current_directory)
        
        # print prompt and take input
        user_choice = input("Enter the number of the item, 'up' to go to the parent directory, 'cancel' to cancel, or the name of the directory if you see it: ").strip()

        # check user input
        if user_choice.isdigit():

            # menu starts at 1 but python starts at 0
            choice_index = int(user_choice) - 1
            
            # list the contents again
            contents = os.listdir(current_directory)

            # sort them again
            contents.sort()
            
            # i did this weeks ago and don't remember what it does
            if 0 <= choice_index < len(contents):

                # your pick is the input number minus 1
                selected_item = contents[choice_index]

                # make an absolute path out of the pwd + choice
                chosen_path = os.path.join(current_directory, selected_item)

                # if it is legit
                if os.path.isdir(chosen_path):

                    # then you must acquit, or pick it
                    print(f"\nDirectory '{selected_item}' selected.")

                    # double check since i wanted to be able to pick subdirectories
                    action = input("Enter 'confirm' to select this directory, or 'explore' to list its contents: ").strip().lower()
                    
                    # if you double down
                    if action == 'confirm':

                        # then here's what's behind door number choice_index
                        selected_directory = chosen_path
                        break

                    # or we dump it out again to look inside
                    elif action == 'explore':
                        
                        # good thing there's a loop here
                        current_directory = chosen_path

                    else:
                        print("Invalid input. Please enter 'confirm' or 'explore'.")
                else:
                    print("The selected item is not a directory. Please try again.")
            else:
                print("Invalid selection. Please try again.")

        # try to go up
        elif user_choice == 'up':

            # self explanatory
            if os.path.dirname(current_directory) == current_directory:
                print("You are at the root directory. Cannot go up.")
            
            # move pwd (not really pwd just a var) if possible
            else:
                current_directory = os.path.dirname(current_directory)

        # self explanatory                
        elif user_choice == 'cancel':
            print("Operation cancelled by user.")
            break

        # same thing as original prompt = digit, but user input file path, see if it's there, etc
        elif os.path.isdir(os.path.join(current_directory, user_choice)):
            chosen_path = os.path.join(current_directory, user_choice)
            print(f"\nDirectory '{user_choice}' selected.")
            action = input("Enter 'confirm' to select this directory, or 'explore' to list its contents: ").strip().lower()
            if action == 'confirm':
                selected_directory = chosen_path
                break
            elif action == 'explore':
                current_directory = chosen_path
            else:
                print("Invalid input. Please enter 'confirm' or 'explore'.")

        else:
            print("Invalid input. Please try again.")

    return selected_directory

# list the files in the directory
def enumerate_files(selected_directory):

    # empty list
    file_paths = []

    # sub-function
    def traverse_dir(directory):

        # iterate through the contents
        for item in os.listdir(directory):

            # build absolute path
            full_path = os.path.join(directory, item)

            # if that was done correctly, then do it again (getting to the full absolute path one directory level at a time)
            if os.path.isdir(full_path):
                
                # dirty loop
                traverse_dir(full_path)
            
            # but if you made it to /
            else:

                # then put that sucker on the list
                file_paths.append(full_path)

    # use the sub function to make the file list
    traverse_dir(selected_directory)

    # ask whether to print the list
    print_option = input("\nDo you want to print the list of file paths? (y/n): ").strip().lower()
    if print_option == 'y':
        for path in file_paths:
            print(path)

    return file_paths

    

def process_files(file_paths):
    # Running counters
    total_files = 0
    found_hits = 0

    for path in file_paths:
        try:
            # use the full absolute path for each file
            filename = path

            # show how to get the md5 (USED THE DEMO HERE)
            md5_hash = hashlib.md5()

            # open the file in read binary
            with open(filename,"rb") as f:

                # moving through 1024 bytes at a time, in binary
                for chunk in iter(lambda: f.read(1024),b""):

                    # get the hash with the addition of the new 1024
                    md5_hash.update(chunk)

            # saving the output md5 hash for the file as a variable
            hash_var = (md5_hash.hexdigest())
            
            found_hits += 1
            print(f"\nhit number {found_hits}: {path} | md5 hash = {hash_var}")

        except Exception as e:
            print(f"Error processing file: {path}. Reason: {e}")
            continue
        
        finally:
            # count files processed
            total_files += 1

    return total_files, found_hits

def main():
    selected_directory = search_for_directory()
    if selected_directory:
        print(f"\nSelected directory: {selected_directory}\n")
        time.sleep(1)
        file_paths = enumerate_files(selected_directory)
        total_files, found_hits = process_files(file_paths)
        print(f"\nSearch completed. Total files searched: {total_files}. Found hits: {found_hits}.")
    else:
        print("No directory selected.")

if __name__ == "__main__":
    main()
