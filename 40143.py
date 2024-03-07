#!/usr/bin/python3

# used demo script and 40136

import socket
import re

def getHost():
    while True:
        host = input("Please provide an IP address to connect to: ") or "192.168.1.xx"
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            octets = host.split('.')
            if all(0 <= int(octet) < 256 for octet in octets):
                break
            else:
                print("Invalid IP address format. Please try again.")
        else:
            print("Invalid IP address format. Please try again.")
    return host

def getPort():
    portList = []
    ports = input("Enter a port of interest for the target host(s): ")
    print("\nGot it, looking at", ports, "\n")
    portList.append(ports)
    morePorts = input("Do you want to add another port? y/n ")
    if morePorts == 'y':
        while True:
            ports = input("\nEnter another port of interest: ['q' to break]\n")
            if ports == 'q':
                break
            print("Got it, looking at", ports, "\n")
            portList.append(ports)
    return portList

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10
sockmod.settimeout(timeout)

hostip = getHost()
portno = getPort()

def portScanner(portno):
    for port in portno:
        if sockmod.connect_ex((hostip, int(port))) == 0:
            print("Port", port, "open")
        else:
            print("Port", port, "closed")

portScanner(portno)
