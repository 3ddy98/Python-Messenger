#!usr/bin/python

import socket
import time
import sys

def sendMessages(username, client):
	while 1:
		message = input(username + " >> ")
		if( message == "/disconnect"):
			sys.exit()
		client.send((username+ " >> "+message).encode())
	
def main():
	while True:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[+] Connecting...")
		try:
                    client.connect(('192.168.1.10', 6677))
                    break

		except: 
			print("Connection Failed, Retrying...")
			time.sleep(3)
	
	print("[+] Connected")
	print(client.getpeername())
	username = input("Enter your Username: ")
	sendMessages(username, client)
					
if __name__ == "__main__":
	main()
