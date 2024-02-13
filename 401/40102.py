# write a script that:
## transmits a ping every two seconds
## evaluates response as success or failure
## assigns outcome to a variable
## prints transmissions as date-time - outcome - dest ip

# 12 Feb added logging

import logging
from datetime import datetime
import time
import subprocess

# Configure logging
logging.basicConfig(filename='ping_log.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

destIP = str(input("Enter a target IP: "))
logging.info(f"Ok, pinging {destIP}")

# Open an infinite loop
while True:
    try:
        # Do the ping and capture the output
        pingResult = subprocess.run(f"ping -c 1 {destIP} | awk '/received/{{print $4}}'", shell=True, stdout=subprocess.PIPE, text=True)

        # Define time right now
        t1 = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        # Assess result
        if pingResult.returncode == 0:
            result_value = int(pingResult.stdout.strip())

            if result_value == 0:
                result = "Failed to ping"
                logging.warning(f"As of {t1} - {result} {destIP}")

            elif result_value == 1:
                result = "Successfully pinged"
                logging.info(f"As of {t1} - {result} {destIP}")

            else:
                logging.error("Error interpreting ping result")
                result = "Error pinging"

        else:
            logging.error("Error running ping command")
            result = "Error"

    except Exception as e:
        logging.error(f"An exception occurred: {e}")

    # Wait 2 seconds
    time.sleep(2)


# example result for reference
#    PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
#    64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.706 ms
#    64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.622 ms
#    64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.672 ms

#    --- 192.168.1.1 ping statistics ---
#    3 packets transmitted, 3 received, 0% packet loss, time 2056ms
#    rtt min/avg/max/mdev = 0.622/0.666/0.706/0.034 ms
    


