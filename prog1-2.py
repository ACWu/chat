# OSU CS 372 Winter 2023
# Programming Project 1 Part 2 - GET the data for a large file
# Student Name: Anthony Wu
# Student ID: wuant
# 
# Citation:
# 1. Kurose and Ross, Computer Networking: A Top-Down Appro    ach, 8th Edition, Pearson. p. 153 - 164
# 2. https://internalpointers.com/post/making-http-requests-sockets-python
 

import socket

serverName = "gaia.cs.umass.edu"
serverPort = 80  #default port for http
request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

#set up socket for TCP connection to the server and port
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sckt.connect((serverName, serverPort))

print(request)

#send request
sckt.send(request.encode())

next = ""

response = sckt.recv(1024)
next = sckt.recv(1024)

#aggregate and loop until the size of response received is 0
while len(next) > 0:
    response = response + next
    next = sckt.recv(1024)

#print the combined response
print("[RECV] - length: ", len(response.decode()))
print(response.decode())

sckt.close()


