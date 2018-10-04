#!/usr/bin/python3

import sys
import chess
import random
import numpy as np
from os import system


if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def clear():
        _ = system('clear')

def listMovesSTR(game):
    moves = []
    for mov in list(game.legal_moves):
        moves.append(str(mov))
    return moves

def listMoves(game):
    return list(game.legal_moves)

def calculateBestMove(game):
    moves = listMoves(game)
    for move in moves:
        _game = game
        _game.push(move)

def evaluateBoard(board):
    fen = (board.fen().split(' '))[0]
    piece = {
        'P': 1,
        'R': 5,
        'N': 3,
        'B': 3,
        'Q': 9,
        'K': 1000,
        'p': -1,
        'r': -5,
        'n': -3,
        'b': -3,
        'q': -9,
        'k': -1000
    }
    fen = fen.replace("/","")
    fen = ''.join(i for i in fen if not i.isdigit())
    lst = np.asarray([piece[k] for k in list(fen)], dtype=np.int32)
    print(lst.sum())

def print_board(board):
    clear()
    PIECE_SYMBOLS = {'P': '♟', 'B': '♝', 'N': '♞',
                     'R': '♜', 'Q': '♛', 'K': '♚',
                     'p': '♙', 'b': '♗', 'n': '♘',
                     'r': '♖', 'q': '♕', 'k': '♔'}
    fen = (board.fen().split(' '))[0]
    b = str(board)
    for k, v in PIECE_SYMBOLS.items():
        b = b.replace("{}".format(k), "{}".format(v))
    b = b.split('\n')
    col = [8,7,6,5,4,3,2,1]
    row = "A B C D E F G H"

    for i in range(0,8,1):
        print("%s %s" %(col[i],b[i]))
    print("  %s"%row)
    #print(fen)

def main():
    """Beat The Turk"""
    board = chess.Board()
    playing = True
    while playing:
        themove = random.choice(listMoves(board))
        print(themove)
        board.push(themove)
        print_board(board)
        print("Posible moves: ")

        moves = []
        for mov in listMoves(board):

            moves.append(str(mov))

        for i in range(0, len(moves), 4):
            print(", ".join(moves[i:i+4]))

        move = input("Enter your move: ")
        while move not in listMovesSTR(board):
            move = input("Re-enter your move: ")

        if move in listMovesSTR(board):
            print(move)
            board.push(chess.Move.from_uci(move))

        evaluateBoard(board)
        playing = not board.is_checkmate()

if __name__ == '__main__':
    main()
