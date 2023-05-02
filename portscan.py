import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$") #  Variable for checking that expression is equivalaent to the later given input for IP

port_range_pattern = re.compile("([0-9]+)-([0-9]+)") # Variable for checking that expression is equivalaent to the later given input for ports

port_min = 0 # Minimum port is 0, they cannot choose lower than this
port_max = 65535 # Maximum port is 65535, they cannot go higher

print("################## - NMAP Port Python Scanner - ##################")

while True:
        ip_add_entered = input("Enter IP for scanning: ")
        try:
                ip_address_obj = ipaddress.ip_address(ip_add_entered) # Combines the address into a full object
                print("Valid IP.")
                break # If its valid, continue, otherwise keep looping
        except:
                print("Invalid IP")

while True:
        print("Enter Port Range in format: <int>-<int> (For example, 20-80")
        ip_add_entered = input("Port Range for Scanning (Min: 0, Max: 65535") # ip_add_entered refers to the port range as raw input
        port_range_valid = port_range_pattern.search(port_range.replace(" "," ")) # Seperates the input into 2 numbers that can be taken later
        if port_range_valid:
                port_min = int(port_range_valid.group(1)) # The FIRST number is counted as lowest
                port_max = int(port_range_valid.group(2)) # The SECOND number is counted as the highest the user wants to go
                break

nm = nmap.PortScanner() # Introducing nmap into the script

for port in range(port_min, port_max + 1): # for loop that goes through each number between lowest and highest
        try:
                result = nm.scan(ip_add_entered, str(port)) # Scans the number associated with the port
                port_status = (result['scan'][ip_add_entered]['tcp'][port]['state']) # Port status variable is if the port returns open, filtered, closed etc
                print(f"Port {port} is {port_status}") # prints a return, like nmap does itself
        except:
                print(f"Cannot scan port {port}.") # Otherwise, tell the user the port cant be scanned by the script
