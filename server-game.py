# OSU CS 372 Winter 2023
# Programming Project 4  - Client / Server Chat
# Student Name: Anthony Wu
# Student ID: wuant
# 
# Citation:
# 1. Kurose and Ross, Computer Networking: A Top-Down Appro        ach, 8th Edition, Pearson. p. 153 - 164
# 2. https://internalpointers.com/post/making-http-requests    -sockets-python

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on %s port %s" % (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        
        print(f"Connected by {addr}")
        print("Type /q to quit; enter a message to send...\n")
        while True:
            data = conn.recv(1024)
            if (not data) or data.decode()=='/q':
                break
            else:
                print("Client: " + data.decode())
            #conn.sendall(data)

            print('Server> ', end='', flush=True)

            conn.sendall(str.encode(input()))