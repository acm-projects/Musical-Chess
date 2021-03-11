import io
import chess.pgn
import lichess.api
import re
from lichess.format import SINGLE_PGN

#takes in username and last 20 games
user = input('Enter your lichess username: ')
info = lichess.api.user(user)
pgn = lichess.api.user_games(user, max=20, format=SINGLE_PGN)  # max param is for number of games, don't touch anything else on this line
print()
#make sure user only enters a number between 1 and 20
game_Num = input('Enter which game would you like? ')

#pgn_store is an array that holds all the games.   r'(1-0|0-1)$' splits everything with 1-0/0-1, but only checks at the end of each line.  
pgn_store = re.split(r'(1-0|0-1)$',pgn, flags=re.MULTILINE)

#prints out each game in the pgn_store array(debug)
#for game in pgn_store:
#    print(game)
#    print('-------------------------------------------------')

#   with -> Will make sure the file closes
with open(f'{user}.pgn', 'w') as f:  # creates a file with filename last20{user}.pgn, containing all of the pgn's for the max= games
    f.write(pgn)
pgn_ = io.StringIO(pgn_store[(int(game_Num) - 1) * 2]) 

#reads in a game
game = chess.pgn.read_game(pgn_)
board = game.board()
#prints board and the moves in the game
print(f'{board}\n')
print(game.mainline_moves())
print()

#keeps track of checks. Should do pins and etc next
check = 0

# this prints a board for every position in the game.
for move in game.mainline_moves():  
    board.push(move)
    if board.is_check():
        check += 1

print(f"{check} checks")
# prints final position, and the score at the end
print(board)
print(pgn_store[(int(game_Num) - 1) * 2 + 1])
# username: khreate
