# Script Name: OC 11 - More Processes in Powershell
# Author: Ian
# Date of Latest Revision: 11/6/2023
# Purpose: Class 11

#####################
#  Enable File and Printer Sharing (firewall enable local sharing)

Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

# Allow ICMP traffic (firewall allow ping on ipv4)

netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 

# Enable Remote management (reg edit to allow remote connection and firewall open 3389 for actual rdp plus NLA for user login)

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f ; Enable-NetFirewallRule -DisplayGroup "Remote Desktop"; Set-ItemProperty ‘HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\‘ -Name “UserAuthentication” -Value 1

# Remove bloatware (awesome tool)

iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

# Enable Hyper-V

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

# Disable SMBv1, an insecure protocol

Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
