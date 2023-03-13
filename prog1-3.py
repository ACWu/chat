# OSU CS 372 Winter 2023
# Programming Project 1 Part 3 - The world's simplest HTTP server
# Student Name: Anthony Wu
# Student ID: wuant
# 
# Citation:
# 1. Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson. p. 153 - 164

import socket

serverIP = "127.0.0.1"
serverPort = 3862
data = "HTTP/1.1 200 OK\r\n"\
        "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
        "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

#set up server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((serverIP, serverPort))

serverSocket.listen(1)

#print request when there is connection
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(1024)

print("Received: ", sentence)

#send data in response to request
connectionSocket.send(data.encode())

print("\nSending>>>>>>>\n", data, "\n<<<<<<<<<<<<")

#close connection socket
connectionSocket.close()

#close server socket
serverSocket.close()


