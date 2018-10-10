#!/usr/bin/python3

import sys
import chess
import random
import numpy as np
from os import system
from itertools import chain

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

def completeFen(board):
    fen = (board.fen().split(' '))[0]
    for i in range(1,9):
        text = "0" * i
        fen = fen.replace("{}".format(i),text)
    fen = fen.replace("/","")
    return fen

def replacePiece(text):
    PIECE_SYMBOLS = {'P': '♟', 'B': '♝', 'N': '♞',
                     'R': '♜', 'Q': '♛', 'K': '♚',
                     'p': '♙', 'b': '♗', 'n': '♘',
                     'r': '♖', 'q': '♕', 'k': '♔'}
    for k, v in PIECE_SYMBOLS.items():
        text = text.replace("{}".format(k), "{}".format(v))
    return text

def print_board(board):
    clear()
    completeFen(board)
    fen = (board.fen().split(' '))[0]

    b = str(board)
    b = replacePiece(b)
    b = b.split('\n')
    col = [8,7,6,5,4,3,2,1]
    row = "A B C D E F G H"

    for i in range(0,8,1):
        print("%s %s" %(col[i],b[i]))
    print("  %s"%row)
    #print(fen)

def matrixChess(board):
    fen = completeFen(board)
    matrixBoard = [{'a': '0', 'b': '0', 'c': '0','d': '0', 'e': '0', 'f': '0','g': '0', 'h': '0'} for i in range(8)]
    row=0
    i = 0
    word="abcdefgh"
    for piece in fen:
        letter=word[i]
        matrixBoard[row][letter]=piece
        i = i + 1
        if row < 7 and i>7:
            row = row + 1
        if i> 7:
            i = 0
    return matrixBoard

def getPiece(board, x, y):
    matrix = matrixChess(board)
    x = int(x) - 1
    return replacePiece(matrix[int(x)][y])

def in_dictlist(key, value, my_dictlist):
    for this in my_dictlist:
        if this[key] == value:
            return True
    return False

def themove_dictlist(key, value, my_dictlist):
    for this in my_dictlist:
        if this[key] == value:
            print(this['mov'])
            return this['mov']


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
        n = 0
        for mov in listMoves(board):
            m = str(mov)
            # print(m)
            piece = getPiece(board, m[1], m[0]) + " "+m[2:]
            moves.append({'nro': n, 'piece': piece, 'mov': str(m)})
            n += 1
        # print(moves)

        string=[]
        for i in moves:
            string.append(str(i.get('nro'))+(i.get('piece')).replace(" ", ""))

        for i in range(0, len(string), 4):
            print(",\t".join(string[i:i+4]))

        try:
            move = int(input("Re-enter your move: "))
        except ValueError:
            print("This is not a whole number.")
            move=9999
        while not in_dictlist('nro', move, moves):
            try:
                move = int(input("Re-enter your move: "))
            except ValueError:
                print("This is not a whole number.")
                move = 9999

        if in_dictlist('nro', move, moves):
            board.push(chess.Move.from_uci(themove_dictlist('nro', move, moves)))

        evaluateBoard(board)
        playing = not board.is_checkmate()

if __name__ == '__main__':
    main()
