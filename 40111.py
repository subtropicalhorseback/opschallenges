#In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

#    Utilize the scapy library

from scapy.all import IP, TCP, sr1, send, RandShort

#    Define host IP

def getTgt():
    target = input("enter the destination IP address for TCP scan: ")
    print("\ngot it, looking at",target,"\n")
    return target

#    Define port range or specific set of ports to scan

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


target = getTgt()
portList = getPort()

print("\n\nTARGETING:",target,portList)

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
    
test = portTester(target,portList)

print("\n\nRESULTS:       \n")
print(test)
