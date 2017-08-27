#!usr/bin/python

import socket
import time
import sys

#Server program meant to communicate with client
#Goal: communicate with sever clients
def terminateSession(conn, server):
	server.shutdown(socket.SHUT_RDWR)
	server.close()
	print("Connection is now closed")
	sys.exit()

def sendMessages(conn, server, username):
	message = input(username + " >> ")
	if(message == "/dis"):
		conn.send((username + " >> Disconnecting...").encode())
		terminateSession(conn, server)
	else:
		conn.send((username + " >> " + message).encode())


def recieveMessages(conn):
	data = conn.recv(1024).decode()
	if not data:
		pass
	else:
		print(data)

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	try:
		print("[+] Binding...")
		server.bind(('', 6677))
		print("[+] Bind was a success!")
	except socket.error as msg:
		print("Bind was a failure, now quiting...")
		sys.exit()

	server.listen(5)
	username = input("Please enter username: ")
	print("[+] Server is Listening")
	conn, addr = server.accept()
	print("Connected with", addr)
	print("Type '/dis' to disconnect from ", addr)
        
	while True:
		recieveMessages(conn)
		sendMessages(conn, server, username)

if __name__ == "__main__":
	main()
