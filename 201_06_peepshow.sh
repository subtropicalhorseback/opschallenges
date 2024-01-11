#!/bin/bash

# Script Name: OC 06 SysInfo
# Author: Ian
# Date of Latest Revision: 31/10/2023
# Purpose: Class 06


# Assignment:
# Write a script that:
    # detects if a file or directory exists
    # creates it if it does not exist.
    # Your script must use at least one array, one loop, and one conditional.

#####################
# Declaration of variables


product=$(lshw -c system | grep "product" | grep -v "PnP" | awk -F': ' '{print $2}')

CPU=$(lshw -c cpu | grep "product" | awk -F': ' '{print $2}')
CPUvendor=$(lshw -c cpu | grep "vendor" | awk -F': ' '{print $2}')
CPUphysID=$(lshw -c cpu | grep "physical" | awk -F': ' '{print $2}')
CPUbus=$(lshw -c cpu | grep "bus" | awk -F': ' '{print $2}')
CPUwidth=$(lshw -c cpu | grep "width" | awk -F': ' '{print $2}')

RAM=$(lshw -c memory | grep "description: " | sed -n '5p' | awk -F': ' '{print $2}')
RAMphysID=$(lshw -c memory | grep "physical id: " | sed -n '5p' | awk -F': ' '{print $2}')
RAMsize=$(lshw -c memory | grep "size: " | sed -n '5p' | awk -F': ' '{print $2}')

display=$(lshw -c display | grep -v -E -e "logical|version" )

network=$(lshw -c network)


#####################
# Declaration of functions

statchecker(){

    echo "Computer Name: $product"
    echo " "
    echo "CPU Stats: $CPU // $CPUvendor // $CPUphysID // $CPUbus // $CPUwidth"
    echo " "
    echo "RAM Stats: $RAM // $RAMphysID // $RAMsize"
    echo " "
    echo "Here are the Display stats: $display"
    echo " "
    echo "And here are the Network stats: $network"

}


#####################
# Main

statchecker 

# End