import chess
import random


def bestMove(game):
    ugly_moves = game.legal_moves
    return ugly_moves[1, len(ugly_moves)]