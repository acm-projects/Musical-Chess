import io
import chess.pgn
import lichess.api
from lichess.format import SINGLE_PGN

user = input('Enter your lichess username: ')
info = lichess.api.user(user)

pgn = lichess.api.user_games(user, max=20, format=SINGLE_PGN)  # max param is for number of games, don't touch anything else on this line
pgn_store = []
with open(f'last20{user}.pgn', 'w') as f:  # creates a file with filename last20{user}.pgn, containing all of the pgn's for the max= games
    f.write(pgn)
pgn_ = io.StringIO(pgn)
game = chess.pgn.read_game(pgn_)
board = game.board()
print(f'{board}\n')
print(game.mainline_moves())

# username: khreate
