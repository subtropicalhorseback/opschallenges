#!/bin/bash

# Script Name: OC 04 identify and kill processes
# Author: Ian
# Date of Latest Revision: 27/10/2023
# Purpose: Class 05

############################################################################################
################################# SEARCH AND DESTROY (SaD) #################################
############################################################################################


# Assignment:
# Write a script that:
    # Displays running processes
    # Asks the user for a PID
    # Kills the process with that PID
    # Starts over at step 1 and continues until the user exits with Ctrl + C

    #Use a loop so that the script will continuously start over
    #ask the user if they would like to kill again, if yes causes the script to finish.

#####################
# Declaration of variables

iter=1

#####################
# Declaration of functions

turnedOn(){
    
    ## initial prompt to begin killing spree
    read -p "Would you like to kill a process? y/n " inp

    ## keeps func running until broken
    while true;
    do

        ## clean break of function
        if [[ $inp == 'no' || $inp == 'n' ]];
        then
            
            ## exit greeting
            echo Thanks for killing! Have a nice day.
            break

        fi
        
        ## display running processes
        ps aux 

        ## input to select a identify a target
        read -p "Enter the number of the process you want to end: " ProN

        ## issue a kill order, report success, and if successful show current iteration
        kill -9 ${ProN} && echo "Killed the process with PID #${ProN} (iteration number $iter)"        
        
        ##count up // modify iterations
        iter=$((iter+1))

        ## prompt to stop or continue
        read -p "Would you like to kill again? y/n " inp


    done
}

#####################
# Main

turnedOn



# End