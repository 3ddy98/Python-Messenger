#!usr/bin/python

import socket
import time
def main():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[+] Connecting...")
		try:
			s.connect(("localhost", 80))
			time.sleep(3)
			break
		except: 
			print("Connection Failed.. Retrying")
			time.sleep(3)
	print("[+] Connected")
					
if __name__ == "__main__":
	main()
