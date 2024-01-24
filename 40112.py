#!/usr/bin/python3

import sys
from scapy.all import IP, ICMP, TCP, sr1, send, RandShort
from ipaddress import ip_network

# automation, baby - made main_menu() skeleton in 45 seconds flat with gpt: https://chat.openai.com/share/191cb25a-be7b-4b49-8c08-e88e9cde19d0
# imported tcp function from 40111.py

###########################################################################################################
###########################################################################################################

# get IP address from user

def getTgt1():
    target = input("enter the destination IP address for TCP scan: ")
    print("\ngot it, looking at",target,"\n")
    return target

def getTgt2():
    target = input("enter the destination IP address and cidr for ICMP sweep: ")
    print("\ngot it, looking at",target,"\n")
    return target

###########################################################################################################

# get target ports from user as list

def getPort():
    portList = []
    ports = input("enter a port of interest for TCP scan: ")
    print("\ngot it, looking at",ports,"\n")
    portList.append(ports)

    morePorts = input("do you want to add another port? y/n ")
    if morePorts == 'y':
        while True:
            ports = input("\nenter a port of interest for TCP scan: ['q' to break] ")
            if ports == 'q':
                break
            print("got it, looking at",ports,"\n")
            portList.append(ports)
        
    return portList

###########################################################################################################

#    Test each port in the specified range using a for loop

def portTester(target, portList):
    
    results = []
    
    for p in portList:
        host = target
        dstPort = p
        srcPort = int(RandShort())  # Generate a random source port
        response = sr1(IP(dst=host)/TCP(sport=int(srcPort), dport=int(dstPort), flags='S'), timeout=1, verbose=0)
        
        ## got help on the interpretation from GPT - I wouldn't have used .getlayer but i kind of like it
        if response:

            # Extract flags from the received packet
            flags = response.getlayer(TCP).flags

            # Check for SYN-ACK
            if flags & 0x12:
                print("\nReceived a SYN-ACK on port", dstPort, "- the port is OPEN. Sending a RST to close.")

                # Send a RST packet to close the connection
                send(IP(dst=host)/TCP(sport=int(srcPort), dport=int(dstPort), flags='R'), verbose=0)

                results.append((dstPort, 'Open'))

            # Check for RST-ACK
            elif flags & 0x14:
                print("Received a RST-ACK on port", dstPort, "- the port is CLOSED.")

                results.append((dstPort, 'Closed'))

        else:
            print("No response received on port", dstPort, "- the port is FILTERED or the packet was DROPPED.")

            results.append((dstPort, 'Filtered/Dropped'))
    
    return results

###########################################################################################################

def tcp_port_scan():
    print("\n\nTCP Port Scan\n\n")

    target = getTgt1()
    portList = getPort()

    print("\n##########\nTARGETING:\n",target,"\nON PORTS:\n",portList,"\n##########\n")

    test = portTester(target,portList)
    print("\nRESULTS:\n")
    print(test)

###########################################################################################################

def icmp_ping_sweep():
    print("\n\nICMP Ping Sweep\n\n")
    netCidr = getTgt2()
    targets = ip_network(netCidr)
    hostReplies = 0

    for host in targets.hosts():

        ping = IP(dst=str(host))/ICMP()
        reply = sr1(ping, timeout=1, verbose=0)

# little help from GPT - just automating
        if reply is None:
            print(f"{host} is down or not responding.")
        elif reply.haslayer(ICMP):
            if int(reply.getlayer(ICMP).type) == 3 and int(reply.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"{host} is actively blocking ICMP traffic.")
            else:
                print(f"{host} is active.")
                hostReplies += 1
                hostList.append(host)
        else:
            print(f"{host} is active.")
            hostReplies += 1

    print(f"\nNumber of active hosts: {hostReplies}")
    print(hostList)
    return hostList

###########################################################################################################

def scan_up_hosts(hostList):
    portList = getPort()

    for host in hostList:
        print(f"\n##########\nTARGETING:\n  {host}\nON PORTS:\n  {portList}\n##########\n")

        test = portTester(host, portList)
        print("\nRESULTS for host", host, ":\n")
        print(test)

###########################################################################################################

def main_menu():
    hostList = []
    while True:
        print("\nMenu:")
        print("1 - TCP Port Scan")
        print("2 - ICMP Ping Sweep")
        print("3 - Port Scan Up_Hosts (run after #2)")
        print("4 - Quit - 'q' or 4")

        choice = input("Enter your choice: ")

        if choice == '1':
            tcp_port_scan()
        elif choice == '2':
            hostList = icmp_ping_sweep()
            print(hostList)
        elif choice == '3':
            if hostList:  # Ensure there is a list of hosts to scan
                scan_up_hosts(hostList)
            else:
                print("No active host list available. Run ICMP Ping Sweep first.")
        elif choice == '4' or choice.lower() == 'q':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

###########################################################################################################

if __name__ == "__main__":
    main_menu()
