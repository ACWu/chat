# OSU CS 372 Winter 2023
# Programming Project 4  - Server Game
# Student Name: Anthony Wu
# Student ID: wuant

import socket, pickle
from game import Board, TicTacToe

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 3861  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #to reuse socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #bind to socket
    s.bind((HOST, PORT))

    #listen for connection
    s.listen()
    print("Server listening on %s port %s" % (HOST, PORT))

    #accept incoming connection
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            #unserialize game object received from socket
            this_game = pickle.loads(conn.recv(1024))
            this_game.board.draw_board()

            #check for game over or tie
            if this_game.board.game_over:
                print("Game over, %s won the game" % this_game.player_1_char)
                break
            if this_game.check_tie():
                print("Game is a tie.")
                break
            
            #play the game
            this_game.get_player_input(this_game.player_2_char)
            
            #serialize game object and send thru socket
            conn.sendall(pickle.dumps(this_game))

            #wait for next turn
            if this_game.board.game_over or this_game.check_tie():
                break
            else:
                print(this_game.player_1_char + "'s turn...")
 
