#!/bin/bash

# Script Name: OC 04 Make Directories
# Author: Ian
# Date of Latest Revision: 26/10/2023
# Purpose: Class 04


# Declaration of variables

## take the input number of directories
read -p "Number of Directories to Make? " numD
echo "$numD directories coming right up!"

## define the empty array
D_array=() 

# Declaration of functions

maker() {
    
    ## populate the array
    for ((i = 1; i <= numD; i++)); do
        D_array+=("$i")
    
    ## make the directories and files using array reference
    mkdir Directory$i
    touch Directory$i/TextFile.txt
    
    ## populate and print status updates
    echo Created Directory" "$i and a subordinate text file.
    echo $((i * 100/ numD)) Percent Complete
    
    done
    
    echo Order Up! 

    }


# Main

maker

# End
