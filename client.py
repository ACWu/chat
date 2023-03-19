# OSU CS 372 Winter 2023
# Programming Project 1 Part 1 - Using a socket to GET a file
# Student Name: Anthony Wu
# Student ID: wuant
# 
# Citation:
# 1. Kurose and Ross, Computer Networking: A Top-Down Appro        ach, 8th Edition, Pearson. p. 153 - 164
# 2. https://internalpointers.com/post/making-http-requests    -sockets-python

import socket
serverName = "gaia.cs.umass.edu"
serverPort = 80  #default port for http
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

#set up socket for TCP connection to the server and port
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sckt.connect((serverName, serverPort))

print(request)

#send request
sckt.send(request.encode())

#get response and print it
response = sckt.recv(1024)

print("[RECV] - length: ", len(response.decode()))
print(response.decode())

sckt.close()


