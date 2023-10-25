#!/bin/bash

# Script Name: OC 03 Login History
# Author: Ian
# Date of Latest Revision: 25/10/2023
# Purpose: Class 03

### I worked with Marcus Nogueira and Michael Roberts, but
### just general discussion - not final answers. I also used
### ChatGPT but it was basic. Link next line.
### https://chat.openai.com/share/b3320226-7675-4982-9228-3d5ff8735239

# Declaration of variables



# Declaration of functions

print_logins() {
    last | grep -vE "system boot" 
    && echo This is the login history
}



# Main

print_logins
print_logins
print_logins


# End
