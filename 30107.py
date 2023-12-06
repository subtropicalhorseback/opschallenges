#!/usr/bin/env python3

# assignment: 
  #   Script must ask the user for a file path and read a user input string into a variable. --- CHECK
  #   Second function that creates a directory with os.makdirs  --- CHECK
  #   Create sub-directories with names (string1, string2, string3) --- CHECK
  #   Script must use the os.walk() function from the os library. --- CHECK
  #   Script must enclose the os.walk() function within a python function that hands it the user input file path. --- CHECK
  #   Save output as .txt --- CHECK
  #   Open the .txt with libre office -- no



# get libraries
import os
import subprocess
from datetime import datetime

# define variables

    ##   take user input for file path
targetDir = str(input("Please enter a file path: "))

# define functions

def directories(a):
    while True:
        ##   print input back to user
        print("Okay, targeting",a)
        
##   check for existence of a directory

        ##  it exists:
        if os.path.exists(a):
            print("Your selected Directory exists.")
            break

        ##   it doesn't exist            
        else:
            print("Your selected Directory does not exist.")

            ##   offer to create a directory
            makeit = str(input("Do you want to create the Directory? y/n "))
           
            ##   user wants to make the directory
            if makeit == "y" or makeit == "Y":
                
##   attempt to make a directory and print success
                try:
                    os.mkdir(a)
                    print(f"Created the directory",a)
                
                ##   unable to make the directory
                except Exception as err:
                    print(f"Encountered an error: {err}")
            
            ##   user does not want to make the directory
            elif makeit == "n" or makeit == "N":

                ##   ask if user wants to go again
                again = str(input("Do you want to try looking for another directory? (y/n): "))

                ##   user wants to go again; exit to top while loop
                if again == "y" or again == "Y":
                    print("Okay! Here we go.")
                    
                    ##   take user input for new file path
                    target2 = str(input("Please enter a different file path: "))
                
                    ##   print new file back to user
                    print("Now targeting",target2)
                
                    ##   redefine the target
                    a = target2
                    continue
            
                ##   user does not want to go again; end the process
                elif again == "n" or again == "N":
                    print("Okay, done searching.")
                    break
                
                ##   bad answer
                else:
                    print("Invalid response")
                    continue
            
            ##   bad answer
            else:
                print("Not a valid response.")
                continue
            
##   ask if user wants to go again
            while True:
                again = str(input("Do you want to try looking for another directory? (y/n): "))

                ##   user wants to go again; exit to top while loop
                if again == "y" or again == "Y":
                    print("Okay! Here we go.")
                    break
            
                ##   user does not want to go again; end the process
                elif again == "n" or again == "N":
                    print("Okay, done searching!")
                    break
                
                ##   bad answer
                else:
                    print("Invalid response")

    subDirs = str(input("Do you want to create subdirectories? (y/n): "))
    while True:
        
        if subDirs == "y" or subDirs == "Y":
            try:
                num_subdirs = int(input("How many subdirectories do you want to create? "))
                for i in range(1, num_subdirs + 1):
                    subdir_name = str(input(f"Enter the name for subdirectory {i}: "))
                    os.mkdir(os.path.join(a, subdir_name))
                    print(f"Created subdirectory: {subdir_name}")

                print("Subdirectories created successfully.")
                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

            except Exception as err:
                print(f"Encountered an error: {err}")
                break

        elif subDirs == "n" or subDirs == "N":
            print("Okay, no subdirectories will be created.")
            break

        else:
            print("Invalid response")

    

def walker(a):
    ##   get username
    username = os.popen("whoami").read().strip()

    ##   get file name
    file = str(input("What would you like to name the saved log of the current contents of your target directory? "))

    ##   file location
    fileloc = f"/home/{username}/Documents/{file}.txt"
    print("Ok, saving to", fileloc)

    ##   create the file
    subprocess.run(["touch", fileloc])
    
    with open(fileloc, "w") as outputloc:
        current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        outputloc.write(f"The following information is accurate as of {current_time}\n\n")
        for dirpath, dirnames, filenames in os.walk(a):
            outputloc.write(f"Current directory: {dirpath}\n")
            outputloc.write("Subdirectories: {}\n".format(', '.join(dirnames)))
            outputloc.write("Files: {}\n\n".format(', '.join(filenames)))


# execute

directories(targetDir)
walker(targetDir)