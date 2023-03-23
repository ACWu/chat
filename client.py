# OSU CS 372 Winter 2023
# Programming Project 4 - Client Chat
# Student Name: Anthony Wu
# Student ID: wuant
# Citation: Adapted from https://realpython.com/python-sockets/

import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 3861  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #connect to socket
    s.connect((HOST, PORT))      
    print("Connected to %s port %s" % (HOST, PORT))

    print("Type /q to quit; enter a message to send...\n")
    while True:
        print('Client> ', end='', flush=True)

        #send thru socket
        s.sendall(str.encode(input()))

        #receive from socket
        data = s.recv(1024)              

        if (not data) or data.decode()=='/q':
            break
        else:
            print("Server: " + data.decode())
