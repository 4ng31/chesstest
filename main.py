import chess
import random

def bestMove(game):
    ugly_moves = game.legal_moves
    return list(ugly_moves)

if __name__ == '__main__':
    game = chess.Board()
    playing = True
    while playing:
        themove = random.choice(bestMove(game))
        print(themove)
        game.push(themove)
        print(game)
        #print(bestMove(game)[Move.from_uci])
        print("Posible moves: ")
        for mov in bestMove(game):
            print(mov)
        move = input("Enter your move: ")
        if move in bestMove(game):
            game.push(move)
        playing = not game.is_checkmate()
        
    