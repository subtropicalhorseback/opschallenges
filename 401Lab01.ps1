# load up the GP tools
Import-Module GroupPolicy

# define the GPO name
$gpoName = "ScreenLock"

# make the gpo
New-GPO -Name $gpoName

# set duration as variable (hardcode because anyone configuring this for the enterprise knows how to change this, I hope)
$ScreenLockDuration = 600

# actually configure the gpo through regedit
Set-GPRegistryValue -Name $gpoName -Key "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -ValueName "InactivityTimeoutSecs" -Type DWORD -Value $ScreenLockDuration
Set-GPRegistryValue -Name $gpoName -Key "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -ValueName "InactivityTimeoutAction" -Type DWORD -Value 1

# define the audience for gpo and apply the gpo to that audience (everyone in the domain initrobe.com)
$OUPath = "OU=Users,DC=initrobe,DC=com"
New-GPLink -Name $gpoName -Target $OUPath


gpupdate /force
