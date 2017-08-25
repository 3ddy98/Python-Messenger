#!usr/bin/python

import socket
import time
import sys

def recieveMessage(conn):
	while True:
		data = conn.recv(1024).decode()
		print(data)		


def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.bind(('localhost', 6677))
	except socket.error as msg:
		print("Bind was a failure, now quiting...")
		sys.exit()

	server.listen(2)
	print("[+] Server is Listening")
	while True:	
		conn, addr = server.accept()
		print("Connected with", addr)
		recieveMessage(conn)

	server.shutdown(socket.SHUT_RDWR)
	server.close()

if __name__ == "__main__":
	main()
