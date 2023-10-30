#!/bin/bash

# Script Name: OC 04 identify and kill processes
# Author: Ian
# Date of Latest Revision: 27/10/2023
# Purpose: Class 05

############################################################################################
################################ Check Directory (Cheddar) #################################
############################################################################################


# Assignment:
# Write a script that:
    # detects if a file or directory exists
    # creates it if it does not exist.
    # Your script must use at least one array, one loop, and one conditional.

#####################
# Declaration of variables

cheddirray=()                                       ## declares ARRAY

#####################
# Declaration of functions

#####################
# Main

read -p "What directory do you want? " dir          ## initial prompt to check for a directory
while true;                                         ## opens infinite while (LOOP)
do
    echo "$dir - great. I'll look... you relax."    ## takes input
    echo " "
    cheddirray+=($dir)                              ## adds input to ARRAY
    if [ -d "$dir" ];                               ## checks for directory (CONDITIONAL)
    then
        echo "I found your, uh, whatever"           ## output if true
        echo " "
    else
        echo "I don't see it anywhere...Sigh... I'll make it for you. No - don't help or anything"  ## output if false
        echo " "
        mkdir -p $dir                                            ## makes the directory

        if [ $? -eq 0 ];                                        ## checks for directory
        then 
            echo "Alright, I made $dir successfully."           ## output if successful
            echo " "
        else
            echo "That didn't feel too good..."                 ## output if failed to create
        fi
    fi
    read -p "Do we have to Cheddir (Ch.Dir.) again? (y/n) " again               ## prompt to continue or break
    if [ "$again" = "y" ];                                                      ## CONDITIONAL for input to continue
    then
        echo "I mean, we've only checked '${cheddirray[@]}' so far, so surrreee - let's keep looking..." ## prints array contents
        echo " "
        read -p "What are we looking for this time? " dir                       ## takes new input
    else
        echo "Thank god that's all I had to do today..."                        ## prints array contents
        echo " "
        echo "~**~ Signing off ~**~"                                            ## breaks LOOP
        break
    fi
done

# End