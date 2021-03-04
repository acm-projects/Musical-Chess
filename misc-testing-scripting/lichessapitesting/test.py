import io
import chess.pgn
import lichess.api
from lichess.format import SINGLE_PGN

user = input('Enter your lichess username: ')
info = lichess.api.user(user)

pgn = lichess.api.user_games(user, max=1, format=SINGLE_PGN)
pgn_store = []
with open(f'last20{user}.pgn', 'w') as f:
    f.write(pgn)
pgn_ = io.StringIO(pgn)
game = chess.pgn.read_game(pgn_)
board = game.board()
print(f'{board}\n')
print(game.mainline_moves())
