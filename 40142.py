#!/usr/bin/python3
# demo code from https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md


# import
import nmap

# use the scanner throughout
scanner = nmap.PortScanner()

# header
print("Nmap Automation Tool")
print("--------------------")

# ip intake and print
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# choose options
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""") 
print("You have selected option: ", resp)

# choose port range
range = input("Enter port range to scan (e.g., 1-1024): ") 

# option 1 - syn/ack
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

# option 2 - udp
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("No UDP ports found.")

# option 3 - comprehensive scan
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS -sU -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys(), scanner[ip_addr].get('udp', {}).keys())

# weak input handling
else:
    print("Please enter a valid option")
