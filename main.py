#!/usr/bin/python3

import sys
import chess
import random

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def bestMove(game):
    ugly_moves = game.legal_moves
    return list(ugly_moves)

def main():
    """Beat The Turk"""
    game = chess.Board()
    playing = True
    while playing:
        themove = random.choice(bestMove(game))
        print(themove)
        game.push(themove)
        print(game)
        print("Posible moves: ")
        for mov in bestMove(game):
            print(mov)
        move = input("Enter your move: ")
        if move in bestMove(game):
            game.push(move)
        playing = not game.is_checkmate()

if __name__ == '__main__':
    main()