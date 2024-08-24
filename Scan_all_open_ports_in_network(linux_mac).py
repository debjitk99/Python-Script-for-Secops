# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AVOlu7MVLzmG_24qb8_OHv3Kukrc_Hq6
"""

#Scan all open port in the network

#Install nmap
!apt-get update
!apt-get install nmap
!pip install python-nmap

import nmap
import subprocess

# user define function to scan & store open ports

def scan_network(host):

  # Create a new port scanner object
  scanner = nmap.PortScanner()
  scanner.scan(host, '1-65535')
  open_port = [] #store open ports
  for port in scanner [host]['tcp']:
    if scanner [host]['tcp'][port]['state'] == 'open':
      open_port.append(port)
  if not open_port:
    open_port.append(0)

  return open_port

#To check which application are using what portin the linux/mac machine

def check_port_usage(port):
    try:
        # For Linux/MacOS
        result = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True)
        if result.stdout:
            print(f"Application using port {port}:\n{result.stdout}")
        else:
            print(f"No application is using port {port}.")
    except Exception as e:
      print(f"An error occurred: {e}")

target_address = input ("Enter the host name you want to scan ")

open_port = scan_network(target_address)
for port in open_port:
  if port == 0:
    print(f"no ports are open for the IP {target_address}")
  else:
    print (f"{port} is open for the target IP address {target_address} and it is used for {check_port_usage(port)}")