# Script Name: OC 09 System Logs
# Author: Ian
# Date of Latest Revision: 11/2/2023
# Purpose: Class 09

#####################
# Declaration of variables


#####################
# Declaration of functions

# output 24 hours of system event logs
function Export24 {Get-WinEvent -LogName 'System' -MaxEvents 500 | Where-Object { $_.TimeCreated -ge (Get-Date).AddDays(-1) } | Out-File "$env:USERPROFILE\Documents\24HourSystemLogs.txt"}

# output of error logs
function Errors {Get-WinEvent -LogName 'System' -MaxEvents 500 | Where-Object { $_.LevelDisplayName -eq 'Error' } | Out-File "$env:USERPROFILE\Documents\ErrorLogs.txt"}

# display all the ID 16 events
function ShowID16 {Get-WinEvent -LogName 'System' -MaxEvents 500 | Where-Object { $_.Id -eq 16 } | Format-Table -AutoSize}

# give me 20
function Show20 {Get-WinEvent -LogName 'System' -MaxEvents 20 | Format-Table -AutoSize}

#  source check for 500 events
function Show500Sources {Get-WinEvent -LogName 'System' -MaxEvents 500 | Format-List -Property ProviderName, Message}

#####################
# Main

Export24
Errors
ShowID16
Show20
Show500Sources

# End
