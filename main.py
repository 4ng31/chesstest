import chess
import random

def bestMove(game):
    ugly_moves = game.legal_moves
    return random.choice(list(ugly_moves))

if __name__ == '__main__':
    game = chess.Board()
    themove=bestMove(game)
    print themove