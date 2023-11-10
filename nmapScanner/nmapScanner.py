#!/usr/bin/python3

#pip3 install nmap
import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')
print('<----------------------------------------------------------->')

ip_addr = input('Please enter the IP address you want to scan: ')
print('THe IP you entere is: ', ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehesive Scan \n""")
print('You hace selected option: ', resp)

if resp == '1':
    print('Nmap version: ', scanner.nmap.version())
    scanner.scan(ip_addr, '1-65535', '-v -sS')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap version: ', scanner.nmap.version())
    scanner.scan(ip_addr, '1-65535', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('Nmap version: ', scanner.nmap.version())
    scanner.scan(ip_addr, '1-65535', '-v -sS -sV -sC -O -p- --open')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print('Please enter a valid options...')
