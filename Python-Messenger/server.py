#!usr/bin/python

import socket
import time
import sys

def main():
	print("[+] Listening...")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		server.bind(('localhost', 80))
	except socket.error as msg:
		print("Bind was a failure, now quiting...")
		sys.exit()

	server.listen(1)
	
	conn, addr = server.accept()
	print("Connected with", addr)
	server.shutdown(socket.SHUT_RDWR)
	server.close()

if __name__ == "__main__":
	main()
