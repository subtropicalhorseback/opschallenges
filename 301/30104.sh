#!/bin/bash

# Script Name: 30104 Ops Challenge: Conditionals and Menu
# Author: Ian
# Date of Latest Revision: 30 Nov 23

# menu w following options:
# hello world
# ping loopback
# ip info
# exit

## take user input
## use input in conditional to evaluate and act
## loop back to menu

##############################################################################

# Declaration of functions

fontgrab(){
    sudo wget https://raw.githubusercontent.com/titusgroen/figlet-fonts/master/Modular.flf -O /usr/share/figlet/Modular.flf &
    wget_pid=$!
    wait $wget_pid
    clear
    echo "I downloaded a font for figlet to /usr/share/figlet/Modular.flf"
}

####################################################

hellothere(){

str1="hello there\n"
str2="General Kenobi!?\n"
str3="I hate sand.\n"
str4="Hello World\n"

array1=("$str1" "$str2" "$str3" "$str4")

for thing in "${array1[@]}"; do
    sleep 1
    echo -e "$thing"
done 

}


####################################################

toc(){

            ## leaned on class repo for this https://github.com/codefellows/seattle-ops-301d14/blob/main/class-04/challenges/DEMO.md
while true; do

    echo -e "Would you like to run one of these programs? Enter a number 1-5 or type 'no' to quit."
    echo "Here are the options: "
    echo "   1. Hello World - send a useless echo of Hello World to the screen."
    echo "   2. Ping Loopback IP - sends an ICMP ping to this device's loopback address"
    echo "   3. IP Info - prints ip info for this device to the screen."
    read choice

    if [[ $choice == 1 ]]; then
        figlet You  Chose  Hello World -f Modular.flf
        echo ""
        sleep 0.5
        echo "running"
        sleep 0.5
        hellothere 
        sleep 0.5
        read -p "Press Enter to continue"

    elif [[ $choice == 2 ]]; then
        figlet You  Chose  Self-Ping -f Modular.flf
        echo ""
        echo ""
        sleep 0.5
        echo "Sending 8 pings"
        ping -c 8 127.0.0.1
        sleep 0.5
        read -p "Press Enter to continue"

    elif [[ $choice == 3 ]]; then
        figlet You Chose IP Info -f Modular.flf
        echo ""
        echo ""
        sleep 0.5
        ip -o -4 addr show | awk '{print $1, $2, $4}'
        sleep 0.5
        read -p "Press Enter to continue"

    elif [[ $choice == "no" ]]; then
        sleep 0.5
        echo -e "adios \nmotha \nclucka" | figlet -f Modular.flf
        echo ""
        echo "~~"
        echo ""
        break

    else
        sleep 0.5
        figlet "wrong answer sucker" -f Modular.flf
        sleep 0.5
        read -p "Press Enter to continue"
    fi
done
}

# Main

fontgrab &
sleep 1
toc | lolcat