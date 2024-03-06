#!/usr/bin/python3
# demo code from https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md
import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# Prompting the user for the scan type including the third scan type option.
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""") # Completed the third scan option
print("You have selected option: ", resp)

# Prompt the user to type in a port range for the scan.
range = input("Enter port range to scan (e.g., 1-1024): ") # Addressed the TODO for port range input

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # Added the missing code block for UDP Scan.
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("No UDP ports found.")
elif resp == '3':
    # Added the missing code block for Comprehensive Scan.
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS -sU -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys(), scanner[ip_addr].get('udp', {}).keys())
else:
    print("Please enter a valid option")
