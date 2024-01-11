# instructions for 40103
## take user email and password to send notifications
## send email to administrator if host status changes up-down or down-up
## append all changes to log
## leaning hard on Roger's demo and resource: https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151

# instructions from 40102; most of original code remains, but made some edits based on Roger H review in class
# write a script that:
## transmits a ping every two seconds
## evaluates response as success or failure
## assigns outcome to a variable
## prints transmissions as date-time - outcome - dest ip

######################################
######################################

# import-export business

import logging
import smtplib
import ssl
import subprocess
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ping3 import ping, verbose_ping

######################################
######################################

# define functions:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# function to send email
def send_email(sender, receiver, password, subject, body):

    # defining 'msg' to build the email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, "plain"))

    # engage ssl
    context = ssl.create_default_context()
    
    # handle the actual email transmission via google/smtp
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


######################################

# function to send pings
def onePingonly(destIP):
    # try to ping
    response = ping(destIP, timeout=1)

    # define time right now
    time1 = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # evaluate ping reply and fwd to main function
    if response is not None:
        return "Remote Host appears UP", time1

    else:
        return "Remote Host appears DOWN", time1


######################################
# function to take inputs (ie Main)

def body():
    
    #logging
    logging.basicConfig(filename='ping_log.txt', level=logging.INFO)

    # get sender email
    sender = input("Enter a sender email: ")
    if not sender:
        sender = "defaultemail@gmail.com"

    # get sender email password
    # password = input("Enter that email account's password to authenticate: ")
    # if not password:
    #    print("No password, no email. \n\n Exiting.....")
    #    exit()

    # get receiver email
    receiver = input("Enter a recipient email: ")
    if not receiver:
        receiver = sender

    destIP = str(input("Please enter a target IP: "))
    if not destIP:
        destIP = "8.8.8.8"

    # set logging variables to empty before the ping loop
    last_status = 0
    last_time = 0

    # infinite loop for pinging
    while True:

        # do the ping 
        try:
            # define the status and time as the output from pinging
            current_status, current_time = onePingonly(destIP)
           
            # evaluate for change
            if current_status != last_status:
            
                # log status change
                logging.info(f"{current_time} - Status changed for {destIP} from {last_status} to {current_status}")
            
                # send email on status change 
                ###NEED TO ADD 'PASSWORD' THIRD
                send_email(sender, receiver, f"Ping status change for {destIP} as of {current_time} from {last_status} to {current_status}.", f"Currently, {current_status}")
            
            # update variable to monitor for new changes
            last_status = current_status

            # snooze 2 seconds
            time.sleep(2)

        # error handling    
        except Exception as e:
            logging.error(f"Error during pinging: {e}")


#########

# run the script
if __name__ == "__main__":
    body()



# example result for reference
#    PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
#    64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.706 ms
#    64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.622 ms
#    64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.672 ms

#    --- 192.168.1.1 ping statistics ---
#    3 packets transmitted, 3 received, 0% packet loss, time 2056ms
#    rtt min/avg/max/mdev = 0.622/0.666/0.706/0.034 ms