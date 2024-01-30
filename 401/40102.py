# write a script that:
## transmits a ping every two seconds
## evaluates response as success or failure
## assigns outcome to a variable
## prints transmissions as date-time - outcome - dest ip

from datetime import datetime
import time
import subprocess

destIP = str(input("enter a target IP: "))
print("Ok, pinging",destIP,"\n\n")

# open an infiinite loop
while True:
    # do the ping and capture the output
    pingResult = subprocess.run(f"ping -c 1 {destIP} | awk '/received/{{print $4}}'", shell=True, stdout=subprocess.PIPE, text=True)

    # define time right now
    t1 = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # assess result
    if pingResult.returncode == 0:
        result_value = int(pingResult.stdout.strip())

        if result_value == 0:
            result = "Failed to ping"

        elif result_value == 1:
            result = "Successfully pinged"

        else:
            print("Error interpreting ping result")
            result = "Error pinging"

    else:
        print("Error running ping command")
        result = "Error"

    # print the time for the ping and the result
    print("As of",t1,result,destIP,"\n")
    
    # wait 2 seconds
    time.sleep(2)


# example result for reference
#    PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
#    64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.706 ms
#    64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.622 ms
#    64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.672 ms

#    --- 192.168.1.1 ping statistics ---
#    3 packets transmitted, 3 received, 0% packet loss, time 2056ms
#    rtt min/avg/max/mdev = 0.622/0.666/0.706/0.034 ms
    


