# OSU CS 372 Winter 2023
# Programming Project 4  - Client / Server Chat
# Student Name: Anthony Wu
# Student ID: wuant
# 
# Citation:
# 1. Kurose and Ross, Computer Networking: A Top-Down Appro        ach, 8th Edition, Pearson. p. 153 - 164
# 2. https://internalpointers.com/post/making-http-requests    -sockets-python

import socket
serverName = "localhost"
serverPort = 3861
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

#set up socket for TCP connection to the server and port
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sckt.gethostname((serverName, serverPort))

#print(request)


#send request
#sckt.send(request.encode())

sckt.listen(1)

#get response and print it
#response = sckt.recv(1024)

#print("[RECV] - length: ", len(response.decode()))
print(response.decode())

while True:
    (clientsocet, address) = serversocket.accept()

    ct = client_thread(clientsocket)
    ct.run()

sckt.close()


