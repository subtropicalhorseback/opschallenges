# get modules

import os
import subprocess

# need some variables

var1 = "whoami"
var2 = "ip a"
var3 = ["lshw", "-short"]

# execute some bash in py

print("\n#############################################################\n#############################################################\nThis is the output from 'whoami': \n")
os.system(var1)

print("\n#############################################################\n#############################################################\nThis is the output from 'ip a': \n")
os.system(var2)

#stretch goal
print("\n#############################################################\n#############################################################\nThis is the output from 'lshw -short': \n")
subprocess.run(var3)