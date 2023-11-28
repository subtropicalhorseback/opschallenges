#!/bin/bash

# Script Name: OC 04 Make Directories
# Author: Ian
# Date of Latest Revision: 26/10/2023
# Purpose: Class 04

# Assignment:
# Write a script that 1) Creates four directories; 
# 2) puts the names of the directories in an array; 
# 3) references the array variable to create a new text file in each directory

#####################
# Declaration of variables

arrayFour=() #this array is the input
arrayD=() #this array is the list of Directories

#####################
# Declaration of functions

TheThing(){

    #define the array
    arrayFour=("1" "2" "3" "4")

    #need a loop to use the array
    for numD in "${arrayFour[@]}"; do
        
        #make the directories
        mkdir Dir$numD

        #make the new array
        arrayD+=("Dir$numD")

        
        for x in "${arrayD[@]}"; do
            #make the text files
            touch $x/newfile.txt
        
        done

    done

    #show your work (echo the array)
    echo Successfully created the following directories:
    for name in "${arrayD[@]}"; do
        echo $name

    done

}

#####################
# Main

TheThing

# End
