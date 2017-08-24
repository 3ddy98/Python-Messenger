#!usr/bin/python

import socket
import time

def main():
	while True:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('localhost',80))
		server.listen(5)
		print("[+] Listening...")
		time.sleep(5)

if __name__ == "__main__":
	main()
