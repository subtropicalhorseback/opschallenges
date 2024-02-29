#!/usr/bin/python3
# import libraries
import re, subprocess, time


#    Prompts the user to type a URL or IP address.

def getHost():
    
    #open loop to cycle through error handling until valid IP input
    while True:
        host = input("Please provide an IP address to connect to: ") or "192.168.1.xx"
    
        #this error handling brought to you by GPT4
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            octets = host.split('.')
    
            if all(0 <= int(octet) < 256 for octet in octets):
                break
    
            else:
                print("Invalid IP address format. Please try again.")
    
        else:
            print("Invalid IP address format. Please try again.")

    return host

#    Prompts the user to type a port number.
   
def getPort():
    # declare empty list
    portList = []
    # take user input 1
    ports = input("enter a port of interest for the target host(s): ")
    print("\ngot it, looking at",ports,"\n")
    # add input 1 to list
    portList.append(ports)

    # ask for additional inputs?
    morePorts = input("do you want to add another port? y/n ")
    # if more inputs
    if morePorts == 'y':
        while True:
            # then get those inputs too
            ports = input("\nenter another port of interest: ['q' to break]\n")
            # until escape
            if ports == 'q':
                break
            print("got it, looking at",ports,"\n")
            # and keep adding them to the list
            portList.append(ports)
        
    return portList

#    Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.

def BGnetcat(host, portList):
    ncOut = []
    http_request = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(host)
    for p in portList:
        ncCmd = ['nc', host, str(p)]
        # Send HTTP request after establishing connection
        inlineOut1 = subprocess.run(ncCmd, input=http_request, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ncOut.append(f"{host}: {p} || {inlineOut1.stdout} || {inlineOut1.stderr}\n")

    return ncOut

#    Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.

def BGtelnet(host, portList):
    tnOut = []
    for p in portList:
        tnCmd = ['telnet', host, p]
        inlineOut2 = (subprocess.run(tnCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
        tnOut.append(f"{host}: {p} || {inlineOut2.stdout} || {inlineOut2.stderr}\n")

    return tnOut    

#    Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

def BGnmap(host, portList):
    nmOut = []
    while True:
        choice = input("Would you like to use the standard port list 1-1000 (1) with nmap, or your custom list (2)? (1 or 2)")
        if choice == '1':
            ports = "-p1-1000"
            nmCmd = ['nmap', '-vv', '-sV', ports, host]
            inlineOut3 = (subprocess.run(nmCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
            nmOut.append(f"{host}: 1-1000 || {inlineOut3.stdout} || {inlineOut3.stderr}")
            break

        elif choice == '2':
            for p in portList:
                port = f"-p{p}"
                nmCmd = ['nmap', 'sV', port, host]
                inlineOut3 = (subprocess.run(nmCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
                nmOut.append(f"{host}: {p} || {inlineOut3.stdout}")
            break
    
        else:
            print("invalid reponse. pick 1 or 2")

    return '\n'.join(nmOut)

## main ##
def main():
    host = getHost()
    portList = getPort()
    ncOut = BGnetcat(host, portList)
    tnOut = BGtelnet(host, portList)
    nmOut = BGnmap(host, portList)

    print(f"\nConducted scan on {host} against ports {portList}. Results follow.\n")
    print("netcat:\n")
    print(f"{ncOut}\n\n")
    time.sleep(2)
    print("telnet:\n")
    print(f"{tnOut}\n\n")
    time.sleep(2)
    print("nmap:\n")
    print(f"{nmOut}\n\n")

main()