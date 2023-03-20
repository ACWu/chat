# OSU CS 372 Winter 2023
# Programming Project 4 - Client Game 
# Student Name: Anthony Wu
# Student ID: wuant

import socket, pickle
from game import Board, TicTacToe

HOST = "localhost"  # The server's hostname or IP address
PORT = 3861  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to %s port %s" % (HOST, PORT))

    this_game = TicTacToe() 
    player_char = this_game.get_player_char()
    this_game.board.draw_board()
    while True:
        this_game.get_player_input(player_char)
        s.sendall(pickle.dumps(this_game))

        if this_game.board.game_over or this_game.check_tie():
            break
        else:
            print(this_game.player_2_char + "'s turn...")
            this_game = pickle.loads(s.recv(1024))

            this_game.board.draw_board()

        if this_game.board.game_over:
            print("Game over, %s won the game" % this_game.player_2_char)
            break
        if this_game.check_tie():
            print("Game is a tie.")
            break
 
