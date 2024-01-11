import os
import psutil
import sys
import subprocess


def utilsteps():
    ut = psutil.cpu_times()

    def makespace():
        print("\n###################\n###################\n")

    # Time spent by normal processes executing in user mode
    makespace()
    print("This is the normal user time: ",ut.user)
    makespace()

    # Time spent by processes executing in kernel mode
    print("This is the system time in kernel mode: ",ut.system)
    makespace()

    # Time when system was idle
    print("This is the idle time: ",ut.idle)
    makespace()

    # Time spent by priority processes executing in user mode
    print("This is the priority execution time: ",ut.nice)
    makespace()

    # Time spent waiting for I/O to complete.
    print("this is the IO time: ",ut.iowait)
    makespace()

    # Time spent for servicing hardware interrupts
    print("This is the time for hardware interrupts: ",ut.irq)
    makespace()

    # Time spent for servicing software interrupts
    print("This is the time for software interrupts: ",ut.softirq)
    makespace()

    # Time spent by other operating systems running in a virtualized environment
    print("This is the time for virtual machines: ",ut.steal)
    makespace()

    # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
    print("This is the time for virtual CPUs: ",ut.guest)
    makespace()

# Save the information to a .txt file.
fileDest = str(input("Where do you want to save the file? Absolute path, incl filename: "))
print(fileDest, "\n\n")

with open(fileDest, 'w') as file:
    file.write("Dear sir,\n  The following text outlines system timing statistics: \n\n\n")
    sys.stdout = file
    utilsteps()
    sys.stdout = sys.__stdout__
    file.close()

# Email the .txt file to yourself using Sendmail.
# https://kenfavors.com/code/how-to-install-and-configure-sendmail-on-ubuntu/

sender = str(input("What's your/sender email address? "))
receiver = str(input("What's their/receiver email address? "))

sendmailcmd = ['sendmail', '-f', sender, receiver]

with open(fileDest, 'rb') as file:
    subprocess.run(sendmailcmd, stdin=file)
    file.close()

    print("Sent email to",receiver)