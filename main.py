import chess
import random
import numpy as np
import math



def bestMove(game):
    ugly_moves = game.legal_moves
    return random.choice(list(ugly_moves))

if __name__ == '__main__':
    game = chess.Board()
    themove=bestMove(game)
    print themove