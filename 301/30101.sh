#!/bin/bash

# Script Name: 30101 Ops Challenge: Append Date and Time
# Author: Ian
# Date of Latest Revision: 28 Nov 23

##########################
# Instructions
# Overview
## Time stamping is a critical step in automating log generation. Today, you will manipulate a variable in bash to apply today’s date to a log file.

# Objectives
## Create a bash script that:
   # Copies /var/log/syslog to the current working directory
   # Appends the current date and time to the filename

# For shell scripts, format your code according to the shell style guide linked above.

# Stretch Goals (Optional Objectives)
   # Pursue stretch goals if you are a more advanced user or have remaining lab time.
   # Include in your bash script some timestamped echo statements telling the user what is happening at each stage of the script.

##########################
##########################

# Declaration of variables

targetfile=/var/log/syslog

destination="Syslog_$(date +'%Y%m%d-%H%M%S')"

# Declaration of functions


# Main

echo "Copying file"
echo "from" 
echo $targetfile
echo "to"
pwd
echo "as of $(date +'%H:%M')"

# filler
echo "..."
sleep 1
echo "..."
sleep 1
echo "..."
sleep 2
##good things are worth waiting - this is a UI/UX choice^ because people feel like "it's doing something"

cp $targetfile "./$destination.txt" && echo "Successfully copied"

echo ""

# End
