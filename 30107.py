#!/usr/bin/env python3

# assignment: 
  #   Script must ask the user for a file path and read a user input string into a variable. --- CHECK
   #  Script must use the os.walk() function from the os library.
    # Script must enclose the os.walk() function within a python function that hands it the user input file path.
    # Save output as .txt
    # Open the .txt with libre office
   #  Second function that creates a directory with os.makdirs  --- CHECK
  #   Create sub-directories with names (string1, string2, string3)

# reference: https://www.python.org/ftp/python/doc/quick-ref.1.3.html

# get libraries
import os

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
                again = input("Do you want to try looking for another directory? (y/n): ")

                ##   user wants to go again; exit to top while loop
                if again == "y" or again == "Y":
                    print("Okay! Here we go.")
                    
                    ##   take user input for new file path
                    target2 = str(input("Please enter a different file path: "))
                
                    ##   print new file back to user
                    print("Okay, now looking for",target2)
                
                    ##   redefine the target
                    a = target2
                    continue
            
                ##   user does not want to go again; end the process
                elif again == "n" or again == "N":
                    print("Bye!")
                    return
                
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
                again = input("Do you want to try looking for another directory? (y/n): ")

                ##   user wants to go again; exit to top while loop
                if again == "y" or again == "Y":
                    print("Okay! Here we go.")
                    break
            
                ##   user does not want to go again; end the process
                elif again == "n" or again == "N":
                    print("Bye!")
                    return
                
                ##   bad answer
                else:
                    print("Invalid response")

    print("the next thing")
                

# execute

directories(targetDir)