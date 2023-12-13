
# https://www.manageengine.com/products/ad-manager/powershell/create-new-adorganizationalunit-using-powershell.html

# https://github.com/codefellows/seattle-ops-301d14/tree/main/class-13/challenges


Import-Module ActiveDirectory
New-ADOrganizationalUnit -Name "ExampleOU" -Path "DC=corp,DC=globexpower,DC=com"

New-ADGroup -Name "ExampleGroup" -SamAccountName "ExampleGroup" -GroupScope Global -GroupCategory Security -Path "OU=ExampleOU,DC=corp,DC=globexpower,DC=com"

New-ADUser -Name "Franz Ferdinand" -SamAccountName "ferdif" -UserPrincipalName "ferdif@globexpower.com" -GivenName "Franz" -Surname "Ferdinand" -DisplayName "Franz Ferdinand" -Path "OU=ExampleOU,DC=corp,DC=globexpower,DC=com" -AccountPassword (ConvertTo-SecureString -AsPlainText "Solarwinds123" -Force) -Enabled $true

Add-ADGroupMember -Identity "ExampleGroup" -Members "ferdif"
