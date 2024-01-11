#!/bin/bash

# Script Name: 30101 Ops Challenge: backup and remove logs
# Author: Ian
# Date of Latest Revision: 1 Dec 23

# Write a log clearing bash script. - check
# Print to the screen the file size of the log files before compression - check
# Compress the contents of the log files listed below to a backup directory - check
# /var/log/syslog, /var/log/wtmp - check
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS - check
# Example: /var/log/backups/syslog-20220928081457.zip - check

# Clear the contents of the log file - check
# Print to screen the file size of the compressed file - check
# Compare the size of the compressed files to the size of the original log files - check

##########################################################
#  ___      _______  _______  __   __  _______  _______  #
# |   |    |       ||       ||  | |  ||       ||       | #
# |   |    |   _   ||    ___||  |_|  ||   _   ||    ___| #
# |   |    |  | |  ||   | __ |       ||  | |  ||   | __  #
# |   |___ |  |_|  ||   ||  ||       ||  |_|  ||   ||  | #
# |       ||       ||   |_| ||   _   ||       ||   |_| | # 
# |_______||_______||_______||__| |__||_______||_______| #
##########################################################
##########################################################
# Declaration of variables

syslog="/var/log/syslog"
kernlog="/var/log/kern.log"
authlog="/var/log/auth.log"
dpkglog="/var/log/dpkg.log"
bootlog="/var/log/boot.log"
ufwlog="/var/log/ufw.log"
wtmplog="/var/log/wtmp"

##########################################################
# Take destination directory

read -p "This script will let you backup log files before deletion. Please enter the target directory to save zipped backups (absolute path): " targetdir
echo ""
sleep 0.5
if [ ! -d "$targetdir" ]; then
    mkdir -p "$targetdir"
    echo "Target directory created: $targetdir"
fi
echo -e "Backing logs up to $targetdir before deletion\n"
sleep 1

##########################################################
##########################################################
# Declaration of functions

backup_and_compress_log() {

    local log_file="$1"

    # Check if syslog file exists
    if [ -f "$log_file" ]; then

        # Before compression
        original_size=$(du -h "$log_file" | cut -f1)
        echo "Original size of $log_file: $original_size"
        sleep 1
              
        # make sure i have permissions
        sudo chmod 755 "$log_file"
        sudo chmod 755 "$targetdir"
        echo -e "\nCopying log file from $log_file\n\n"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$log_file" "$targetdir/log-$timestamp"
        sleep 0.5
        gzip "$targetdir/log-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo -e "Log file copied and zipped successfully.\n"
            # After compression
            compressed_size=$(du -h "$targetdir/log-$timestamp.gz" | cut -f1)
            echo -e "Compressed size of log backup: $compressed_size\n"
            sleep 2

            # Calculate percentage difference
            percent_diff=$(awk "BEGIN {print (($original_size / $compressed_size - 1) * 100)}")
            # Calculate size difference in bytes
            size_diff=$(awk "BEGIN {print ($original_size - $compressed_size)}")

            # Print the result
            echo "The original size of $log_file was $original_size, and the compressed size is $compressed_size."
            echo "The file size reduced by approximately $percent_diff% (${size_diff}B) after compression."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/log-$timestamp"*
            sudo rm "$log_file"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2


        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The log file does not exist at $log_file.\n\n"
        sleep 2
    fi
}

##########################################################
##########################################################
# Declaration of logpicker function

logpicker() {

    echo " Welcome to the"
    echo "##########################################################"
    echo "#  ___      _______  _______  __   __  _______  _______  #"
    echo "# |   |    |       ||       ||  | |  ||       ||       | #"
    echo "# |   |    |   _   ||    ___||  |_|  ||   _   ||    ___| #"
    echo "# |   |    |  | |  ||   | __ |       ||  | |  ||   | __  #"
    echo "# |   |___ |  |_|  ||   ||  ||       ||  |_|  ||   ||  | #"
    echo "# |       ||       ||   |_| ||   _   ||       ||   |_| | #"
    echo "# |_______||_______||_______||__| |__||_______||_______| #"
    echo "##########################################################"
    echo -e "##########################################################\n\n\n"
    sleep 5
    while :; do
        echo -e "1) syslog: This log is located at $syslog. It contains general system messages from various components and applications.\n2) kern.log: This log is located at $kernlog. It logs kernel-related messages, including hardware and device driver messages.\n3) auth.log: This log is located at $authlog. It records authentication-related messages, including user logins and authentication attempts.\n4) dpkg.log: This log is located at $dpkglog. It logs package management activities, including installations, removals, and upgrades.\n5) boot.log: This log is located at $bootlog. It contains information about the boot process, including messages from the kernel and services started during boot.\n6) ufw.log: This log is located at $ufwlog. It logs messages related to the Uncomplicated Firewall (UFW) configuration and activities.\n7) wtmp log: This log is located at $wtmplog. It is a system log file on Unix and Unix-like operating systems that records user login and logout activity.\n8) Choose another specific directory or file to backup to $targetdir.\n\n"

        read -p "Enter the number of the log to backup and clear (1-7), 8 to define a different directory, or 9/no/exit/escape to end session: " choice

        case $choice in
            0) echo "Exiting."; exit ;;
            1) echo -e "Got it, looking for truffles in $syslog\n\n"; log_file=$syslog ;;
            2) echo -e "Got it, looking for truffles in $kernlog\n\n"; log_file=$kernlog ;;
            3) echo -e "Got it, looking for truffles in $authlog\n\n"; log_file=$authlog ;;
            4) echo -e "Got it, looking for truffles in $dpkglog\n\n"; log_file=$dpkglog ;;
            5) echo -e "Got it, looking for truffles in $bootlog\n\n"; log_file=$bootlog ;;
            6) echo -e "Got it, looking for truffles in $ufwlog\n\n"; log_file=$ufwlog ;;
            7) echo -e "Got it, looking for truffles in $wtmplog\n\n"; log_file=$wtmplog ;;
            8) echo -e "Ok, let's talk about it."; read -p "Please enter the log location to search for, backup, and remove (absolute path): " user_log; echo -e "\n Got it, $user_log\n\n"; log_file=$user_log ;;
            9|[Nn]|[Nn][Oo]|[Ee][Xx][Ii][Tt]|[Ee][Ss][Cc][Aa][Pp][Ee]) clear; sleep 1; echo "       Oink Oink.."; echo -e "\n\n\n       ~~"; exit ;;
            *) echo "You Chose..."; sleep 1; echo "poorly. (try again)"; sleep 2 ;;
        esac

        if [ "$choice" -ge 1 ] && [ "$choice" -le 8 ]; then
            backup_and_compress_log "$log_file"
        fi

        echo ""
        read -p "Press Enter to continue"

    done
}

##########################################################
##########################################################
# Main
logpicker

# End