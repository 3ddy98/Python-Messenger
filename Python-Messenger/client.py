#!usr/bin/python

import socket
import time

def main():
	while True:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[+] Connecting...")
		try:
			client.connect(("localhost", 80))
			break
		except: 
			print("Connection Failed, Retrying...")
			time.sleep(3)
	
	print("[+] Connected")
	print(client.getpeername())
					
if __name__ == "__main__":
	main()
