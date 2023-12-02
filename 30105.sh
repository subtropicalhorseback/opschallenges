#!/bin/bash

# Script Name: 30101 Ops Challenge: Append Date and Time
# Author: Ian
# Date of Latest Revision: 28 Nov 23

# Write a log clearing bash script. - check
# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory - check
# /var/log/syslog, /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS - check
# Example: /var/log/backups/syslog-20220928081457.zip - check

# Clear the contents of the log file - check
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files

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

syslog_function() {

    # Check if syslog file exists
    if [ -f "$syslog" ]; then

        # Before compression
        original_size=$(du -h "$syslog" | cut -f1)
        echo "Original size of $syslog: $original_size"
        sleep 1
              
        # make sure i have permissions
        sudo chmod 755 "$syslog"
        sudo chmod 755 "$targetdir"
        echo -e "\nCopying log file from $syslog\n\n"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$syslog" "$targetdir/syslog-$timestamp"
        sleep 0.5
        gzip "$targetdir/syslog-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo -e "Log file copied and zipped successfully.\n"
            # After compression
            compressed_size=$(du -h "$targetdir/syslog-$timestamp.gz" | cut -f1)
            echo -e "Compressed size of syslog backup: $compressed_size\n"
            sleep 2

            # Calculate percentage difference
            percent_diff=$(awk "BEGIN {print (($original_size / $compressed_size - 1) * 100)}")
            # Calculate size difference in bytes
            size_diff=$(awk "BEGIN {print ($original_size - $compressed_size)}")

            # Print the result
            echo "The original size of $syslog was $original_size, and the compressed size is $compressed_size."
            echo "The file size reduced by approximately $percent_diff% (${size_diff}B) after compression."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/syslog-$timestamp"*
            sudo rm "$syslog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2


        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The syslog file does not exist at $syslog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

kernlog_function() {
    # Check if kernlog file exists
    if [ -f "$kernlog" ]; then

        # Before compression
        original_size=$(du -h "$kernlog" | cut -f1)
        echo "Original size of $kernlog: $original_size"
        sleep 1
              
        # make sure i have permissions
        sudo chmod 755 "$kernlog"
        sudo chmod 755 "$targetdir"
        echo -e "\nCopying log file from $kernlog\n\n"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$kernlog" "$targetdir/kernlog-$timestamp"
        sleep 0.5
        gzip "$targetdir/kernlog-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo -e "Log file copied and zipped successfully.\n"
            # After compression
            compressed_size=$(du -h "$targetdir/kernlog-$timestamp.gz" | cut -f1)
            echo -e "Compressed size of kernlog backup: $compressed_size\n"
            sleep 2

            # Calculate percentage difference
            percent_diff=$(awk "BEGIN {print (($original_size / $compressed_size - 1) * 100)}")
            # Calculate size difference in bytes
            size_diff=$(awk "BEGIN {print ($original_size - $compressed_size)}")

            # Print the result
            echo "The original size of $kernlog was $original_size, and the compressed size is $compressed_size."
            echo "The file size reduced by approximately $percent_diff% (${size_diff}B) after compression."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/kernlog-$timestamp"*
            sudo rm "$kernlog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2


        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The kernlog file does not exist at $kernlog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

authlog_function() {
    # Check if authlog file exists
    if [ -f "$authlog" ]; then

        # Before compression
        original_size=$(du -h "$authlog" | cut -f1)
        echo "Original size of $authlog: $original_size"
        sleep 1
              
        # make sure i have permissions
        sudo chmod 755 "$authlog"
        sudo chmod 755 "$targetdir"
        echo -e "\nCopying log file from $authlog\n\n"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$authlog" "$targetdir/authlog-$timestamp"
        sleep 0.5
        gzip "$targetdir/authlog-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo -e "Log file copied and zipped successfully.\n"
            # After compression
            compressed_size=$(du -h "$targetdir/authlog-$timestamp.gz" | cut -f1)
            echo -e "Compressed size of authlog backup: $compressed_size\n"
            sleep 2

            # Calculate percentage difference
            percent_diff=$(awk "BEGIN {print (($original_size / $compressed_size - 1) * 100)}")
            # Calculate size difference in bytes
            size_diff=$(awk "BEGIN {print ($original_size - $compressed_size)}")

            # Print the result
            echo "The original size of $authlog was $original_size, and the compressed size is $compressed_size."
            echo "The file size reduced by approximately $percent_diff% (${size_diff}B) after compression."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/authlog-$timestamp"*
            sudo rm "$authlog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2


        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The authlog file does not exist at $authlog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

dpkglog_function() {
    # Check if dpkglog file exists
    if [ -f "$dpkglog" ]; then

        # Before compression
        original_size=$(du -h "$dpkglog" | cut -f1)
        echo "Original size of $dpkglog: $original_size"
        sleep 1
              
        # make sure i have permissions
        sudo chmod 755 "$dpkglog"
        sudo chmod 755 "$targetdir"
        echo -e "\nCopying log file from $dpkglog\n\n"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$dpkglog" "$targetdir/dpkglog-$timestamp"
        sleep 0.5
        gzip "$targetdir/dpkglog-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo -e "Log file copied and zipped successfully.\n"
            # After compression
            compressed_size=$(du -h "$targetdir/dpkglog-$timestamp.gz" | cut -f1)
            echo -e "Compressed size of dpkglog backup: $compressed_size\n"
            sleep 2

            # Calculate percentage difference
            percent_diff=$(awk "BEGIN {print (($original_size / $compressed_size - 1) * 100)}")
            # Calculate size difference in bytes
            size_diff=$(awk "BEGIN {print ($original_size - $compressed_size)}")

            # Print the result
            echo "The original size of $dpkglog was $original_size, and the compressed size is $compressed_size."
            echo "The file size reduced by approximately $percent_diff% (${size_diff}B) after compression."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/authlog-$timestamp"*
            sudo rm "$dpkglog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2


        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The dpkglog file does not exist at $dpkglog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

bootlog_function() {
    # Check if bootlog file exists
    if [ -f "$bootlog" ]; then
        echo -e "Copying log file from $bootlog\n\n"
        sudo chmod 755 "$bootlog"
        sudo chmod 755 "$targetdir"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$bootlog" "$targetdir/bootlogbackup-$timestamp"
        gzip "$targetdir/bootlogbackup-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo "Log file copied and zipped successfully."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/bootlogbackup-$timestamp"*
            sudo rm "$bootlog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2

        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The bootlog file does not exist at $bootlog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

ufwlog_function() {
    # Check if ufwlog file exists
    if [ -f "$ufwlog" ]; then
        echo -e "Copying log file from $ufwlog\n\n"
        sudo chmod 755 "$ufwlog"
        sudo chmod 755 "$targetdir"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$ufwlog" "$targetdir/ufwlogbackup-$timestamp"
        gzip "$targetdir/ufwlogbackup-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo "Log file copied and zipped successfully."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/ufwlogbackup-$timestamp"*
            sudo rm "$ufwlog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2

        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The ufwlog file does not exist at $ufwlog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

wtmplog_function() {

    # Check if ufwlog file exists
    if [ -f "$wtmplog" ]; then
        echo -e "Copying log file from $wtmplog\n\n"
        sudo chmod 755 "$wtmplog"
        sudo chmod 755 "$targetdir"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$wtmplog" "$targetdir/ufwlogbackup-$timestamp"
        gzip "$targetdir/ufwlogbackup-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo "Log file copied and zipped successfully."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/ufwlogbackup-$timestamp"*
            sudo rm "$wtmplog"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2

        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The ufwlog file does not exist at $wtmplog.\n\n"
        sleep 2
    fi
}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

usr_def_function() {

    # take new dir location

    read -p "Please enter the log location to search for, backup, and remove (absolute path): " usr_def
    echo ""
    sleep 0.5
    echo -e "Okay, checking for $usr_def\n"
    sleep 1

    # Check if ufwlog file exists
    if [ -f "$usr_def" ]; then
        echo -e "Copying log file from $usr_def\n\n"
        sudo chmod 755 "$usr_def"
        sudo chmod 755 "$targetdir"
        sleep 1
        
        # cp and gzip with timestamp - need to use a variable because gzip gets confused
        timestamp=$(date +%Y%m%d-%H:%M:%S)
        cp "$usr_def" "$targetdir/ufwlogbackup-$timestamp"
        gzip "$targetdir/ufwlogbackup-$timestamp"
        
        # check for success
        if [ $? -eq 0 ]; then
            echo "Log file copied and zipped successfully."
            sleep 2
            
            # rm with wildcard
            sudo rm "$targetdir/ufwlogbackup-$timestamp"*
            sudo rm "$usr_def"
            echo -e "Removed copied file (unzipped) and removed original log.\n\n"
            sleep 2

        else
            echo -e "Failed to copy and zip the log file. Please check permissions and try again.\n\n"
            sleep 2

        fi
    else
        echo -e "Error: The ufwlog file does not exist at $usr_def.\n\n"
        sleep 2
    fi
}

##########################################################
##########################################################
# Declaration of logpicker function

logpicker() {
    while :; do
        echo -e "1) syslog: This log is located at $syslog. It contains general system messages from various components and applications.\n2) kern.log: This log is located at $kernlog. It logs kernel-related messages, including hardware and device driver messages.\n3) auth.log: This log is located at $authlog. It records authentication-related messages, including user logins and authentication attempts.\n4) dpkg.log: This log is located at $dpkglog. It logs package management activities, including installations, removals, and upgrades.\n5) boot.log: This log is located at $bootlog. It contains information about the boot process, including messages from the kernel and services started during boot.\n6) ufw.log: This log is located at $ufwlog. It logs messages related to the Uncomplicated Firewall (UFW) configuration and activities.\n7) Choose another specific directory or file to backup to $targetdir.\n\n"

        read -p "Enter the number of the log to backup and clear (1-7), 8 to define a different directory, or 9/no/exit/escape to end session: " choice

        case $choice in
            1) sleep 0.5; echo -e "Got it, looking for truffles in $syslog\n\n"; sleep 1; syslog_function ;;
            2) sleep 0.5; echo -e "Got it, looking for truffles in $kernlog\n\n"; sleep 1; kernlog_function ;;
            3) sleep 0.5; echo -e "Got it, looking for truffles in $authlog\n\n"; sleep 1; authlog_function ;;
            4) sleep 0.5; echo -e "Got it, looking for truffles in $dpkglog\n\n"; sleep 1; dpkglog_function ;;
            5) sleep 0.5; echo -e "Got it, looking for truffles in $bootlog\n\n"; sleep 1; bootlog_function ;;
            6) sleep 0.5; echo -e "Got it, looking for truffles in $ufwlog\n\n"; sleep 1; ufwlog_function ;;
            7) sleep 0.5; echo -e "Got it, looking for truffles in $wtmplog\n\n"; sleep 1; wtmplog_function ;;
            8) sleep 0.5; echo "Ok, let's talk about it."; sleep 1; usr_def_function ;;
            9|[Nn]|[Nn][Oo]|[Ee][Xx][Ii][Tt]|[Ee][Ss][Cc][Aa][Pp][Ee]) clear; sleep 1; echo "Oink Oink.."; echo -e "\n\n\n~~"; exit ;;
            *) echo "You Chose..."; sleep 1; echo "poorly. (try again)"; sleep 2 ;;
        esac

        read -p "Press Enter to continue"

    done
}

##########################################################
##########################################################
# Main
logpicker

# End
