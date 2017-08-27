#!usr/bin/python

import socket
import time
import sys
import multiprocessing

#Client for the messaging program

def recieveMessages(client):
	data = client.recv(1024).decode() #Decodes incoming binary data
	if not data:
		pass #If the recieved data is empty the function just passes
	else:
		print(data)

def sendMessages(username, client):
#The client is set to send the first message, and the server recieve
	message = input(username + " >> ")
	if( message == "/dis"):
		client.send((username + " >> Disconnecting...").encode())
		client.shutdown(socket.SHUT_RDWR)
		client.close()
		print("Connection is now closed.")
		sys.exit()
	else:
		client.send((username + " >> " + message).encode()) # This encodes the string into binary data to be transmitted
def connectToServer(client):
	while True:
		print("[+] Connecting...")
		try:
			client.connect(('192.168.1.10', 6677))
			break
		except: 
			print("Connection Failed, Retrying...")
			time.sleep(3)
	print("Connected to: " + str(client.getpeername()))

def main():
#This loop is going to run until the client finds the server it wants to connect to
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connectToServer(client)
	username = input("Enter your Username: ")
	print("Type '/dis' to end connection")
	while True:
		try:
			sendMessages(username, client)
			recieveMessages(client) #After the user has send their message, they will now listen
		except ConnectionResetError:
			print("[-] Connection has been lost by other user")
			main()
		except BrokenPipeError:
			print("[-] Message was not sent, Broken Pipe")
			main()

if __name__ == "__main__":
	main()
