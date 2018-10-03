#!/usr/bin/python3

import sys
import chess
import random
import numpy as np

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


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
    fen = ''.join(i for i in fen if  not i.isdigit())
    lst = np.asarray([piece[k] for k in list(fen)], dtype=np.int32)
    print(lst.sum())

    #value = 0
    # while i < len(fen[0]):
    #     value = value + piece[i]
    # for k, v in piece.items():
    #     if f in fen[0]:
    #         if f == piece[k]:
    #             value = value + piece[k]
    #             print("Code : {0}, Value : {1}".format(k, v))
    # print(value)


def main():
    """Beat The Turk"""
    board = chess.Board()
    playing = True
    while playing:
        themove = random.choice(listMoves(board))
        print(themove)
        board.push(themove)
        print(board)
        print("Posible moves: ")
        for mov in listMoves(board):
            print(mov)
        move = input("Enter your move: ")
        if move in listMoves(board):
            board.push(move)
        evaluateBoard(board)
        playing = not board.is_checkmate()

if __name__ == '__main__':
    main()