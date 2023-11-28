# Script Name: OC 10 Processes in Powershell
# Author: Ian
# Date of Latest Revision: 11/3/2023
# Purpose: Class 10

#####################
# Declaration of variables

$commandsArray = @("10ProcessByTime", "10ProcessByID", "5ProcessByWSK", "GoToSite", "10NotesStarts", "NoMoreNotes", "KillByPID")

#####################
# Declaration of functions

# Show top 10 active processes by oldest to newest
function 10ProcessByTime {Get-Process | Sort-Object -Property TotalProcessorTime -Descending | Select-Object -First 10 | Format-List}

# Show top 10 active processes by PID
function 10ProcessByPID {Get-Process | Sort-Object -Property Id | Select-Object -First 10 | Format-List}

# Top 5 by WSK
function 5ProcessByWSK {Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 5 | Format-List}

# Open a webpage in a specific browser
function GoToSite {Start-Process -FilePath "C:\Program Files\Mozilla Firefox\Firefox.exe" -ArgumentList https://owasp.org/www-project-top-ten/}

# Start Notepad ten times
function 10NotesStarts {1..10 | ForEach-Object {Start-Process -FilePath "C:\Windows\System32\notepad.exe"}}

# close notepad(s)
function NoMoreNotes {Get-Process | Where-Object { $_.ProcessName -eq "notepad" } | ForEach-Object { Stop-Process -Id $_.Id }}

# kill by PID - same as above but only one
function KillByPID($pid) {Stop-Process -Id $pid}

#####################
# Main

# Display available options to the user. Write-Host prints the prompt and then the array items; the for loop iterates through them all
Write-Host "Available commands:"
for ($i = 0; $i -lt $commandsArray.Length; $i++) {
    Write-Host "[$($i+1)] $($commandsArray[$i])"
}

# Prompt the user for an integer input, Read-Host takes the input from the user
do {
    $userChoice = Read-Host "Enter the number of the command you want to run (1 through $($commandsArray.Length))"
    $userChoice = [int]$userChoice
} while ($userChoice -lt 1 -or $userChoice -gt $commandsArray.Length)

# Execute the selected function based on the user's input - calculates the function based on the number from the user
$selectedCommand = $commandsArray[$userChoice - 1]

switch ($selectedCommand) {
    "10ProcessByTime" { 10ProcessByTime }
    "10ProcessByPID" { 10ProcessByPID }
    "5ProcessByWSK" { 5ProcessByWSK }
    "GoToSite" { GoToSite }
    "10NotesStarts" { 10NotesStarts }
    "NoMoreNotes" { NoMoreNotes }
    "KillByPID" {
        $pid = Read-Host "Enter the PID to kill"
        KillByPID $pid
    }
    default {
        Write-Host "Invalid command. Please enter a valid command from the list."
    }
}

# End