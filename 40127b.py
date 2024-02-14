# write a script that:
## transmits a ping every two seconds
## evaluates response as success or failure
## assigns outcome to a variable
## prints transmissions as date-time - outcome - dest ip

# 12 Feb added logging
# 13 Feb new reqs - Add a log rotation feature based on size (this version)
        # i haven't used gemini for code before, and wanted to see what it could do
        # here's the link to that conversation - https://g.co/gemini/share/dbd9b170d36a

    # alternate: Add a log rotation feature based on time (40127B.py)
        # here's the revision https://g.co/gemini/share/c43a3832b68a 


import logging  # Import the logging module
from logging.handlers import TimedRotatingFileHandler  # Import for time-based rotation
from datetime import datetime  # Import for timestamping 
import time  # Import for delays
importsubprocess  # Import for running external commands 
import argparse  # Import for command-line argument handling
import re  # Import for regular expression-based IP validation

def is_valid_ip(ip):
    """Validatesan IP address (IPv4 format)."""  # Function definition comment
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    return bool(re.match(pattern, ip))  # Returns True if the IP matches the pattern

def ping_host(ip_address):
    """Pings a host and returns the result.""" 
    try:
        ping_result = subprocess.run(
            f"ping -c 1 {ip_address} | awk '/received/{{print $4}}'",  # Run ping command
            shell=True,  # Use shell to interpret command
            stdout=subprocess.PIPE,  # Capture standard output
            text=True  # Work with text output
        )

        if ping_result.returncode == 0:  # Check if the ping command was successful
            result_value = int(ping_result.stdout.strip())  # Extract result value
            return result_value, None  # Return the result value and no error message

        else:
            return None, "Error running ping command"  # Error if ping failed

    except subprocess.CalledProcessError as e:
        return None, f"Error pinging host: {e}"  # Error during ping execution

def main():
    # Configure logging
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Format for log messages
    log_handler = TimedRotatingFileHandler('ping_log.log', when='midnight', backupCount=5)  # Rotate at midnight, keep 5 backups
    log_handler.setFormatter(log_formatter)  # Set the format for log messages
    logger = logging.getLogger(__name__)  # Get the logger instance
    logger.setLevel(logging.DEBUG)  # Set log level to capture DEBUG messages and above
    logger.addHandler(log_handler)  # Add the handler to the logger

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Ping a target IP address.")  
    parser.add_argument("ip_address", help="The target IP address to ping.")  
    args = parser.parse_args()  

    logger.info(f"Ok, pinging {args.ip_address}")  # Log the start of the ping process

    while True:  # Start an infinite loop to continuously ping 
        result_value, error_msg = ping_host(args.ip_address)  # Call the ping_host function
        t1 = datetime.now().strftime("%d-%m-%y %H:%M:%S")  # Get the current timestamp

        if error_msg:  # If there was an error during the ping
            logger.error(error_msg)  # Log the error message
            print(error_msg)  # Print the error message to the console 
        else:  # If the ping was successful
            if result_value == 0:
                result = "Failed to ping" 
            elif result_value == 1:
                result = "Successfully pinged"
            else:
                result = "Error interpreting ping result" 
                logger.error(result)  

            print(result)  # Print the result to the console 
            log_level = logging.INFO if result_value == 1 else logging.WARNING  # Determine log level
            logger.log(log_level, f"As of {t1} - {result} {args.ip_address}")  # Log with appropriate level

        time.sleep(2)  # Wait 2 seconds before the next ping 

if __name__ == "__main__":
    main() 


# example result for reference
#    PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
#    64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.706 ms
#    64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.622 ms
#    64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.672 ms

#    --- 192.168.1.1 ping statistics ---
#    3 packets transmitted, 3 received, 0% packet loss, time 2056ms
#    rtt min/avg/max/mdev = 0.622/0.666/0.706/0.034 ms
    


