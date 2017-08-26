#!usr/bin/python

import socket
import time
import sys
import multiprocessing as mp

mp.allow_connection_pickling()

def recieveMessage(conn):
	while True:
		data = conn.recv(1024).decode()
		print(data)		


def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	try:
		server.bind(('', 6677))
	except socket.error as msg:
		print("Bind was a failure, now quiting...")
		sys.exit()

	server.listen(2)
	print("[+] Server is Listening")
	while True:	
		conn, addr = server.accept()
		print("Connected with", addr)
		clientHandling = mp.Process(target = recieveMessage, args=(conn,))
		clientHandling.start()

	server.shutdown(socket.SHUT_RDWR)
	server.close()

if __name__ == "__main__":
	main()
