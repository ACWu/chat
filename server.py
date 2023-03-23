# OSU CS 372 Winter 2023
# Programming Project 4  - Server Chat
# Student Name: Anthony Wu
# Student ID: wuant
# Citation: Adapted from https://realpython.com/python-sockets/

import socket

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 3861  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #to reuse socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #bind to socket
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on %s port %s" % (HOST, PORT))

    #accept incoming connection
    conn, addr = s.accept()

    with conn:
        
        print(f"Connected by {addr}")
        print("Type /q to quit; enter a message to send...\n")
        while True:
            #receive from socket
            data = conn.recv(1024)
            if (not data) or data.decode()=='/q':
                break
            else:
                print("Client: " + data.decode())

            print('Server> ', end='', flush=True)
            
            #send thru socket
            conn.sendall(str.encode(input()))
