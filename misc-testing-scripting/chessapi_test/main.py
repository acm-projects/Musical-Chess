import requests
import io
import chess.pgn
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci('stockfish_13_win_x64_avx2.exe')
pgn_store = []
username = input("Enter your username here: ")
games_raw = requests.get(f"https://api.chess.com/pub/player/{username}/games/2021/03")
games = games_raw.json()['games']
print(f'There are {len(games)} games.')
pick = int(input('Pick a number in games: '))
for i in range(len(games)):  # prints every game pgn for month of february
    # print(games[i]['pgn'])
    pgn_store.append(games[i]['pgn'])
print(pgn_store[pick])
pgn = io.StringIO(pgn_store[pick])
# this makes a game object using chess package pgn parsing, and pushes the moves to a board.
game = chess.pgn.read_game(pgn)
board = game.board()
print(type(board))
boards = []
checks = 0
color = None
for move in game.mainline_moves():  # this prints a board for every position in the game.
    board.push(move)
    checks += 1
    if board.is_check():
        if checks % 2 == 0:
            color = 'black'
        if checks % 2 == 1:
            color = 'white'
        print(f'Move {checks} by {color} is a check: {move}')
    boards.append(str(board))
    info = engine.analyse(board, chess.engine.Limit(depth=10))
    score_string = (str(info['score'])[12:16])
    clean_score = int(score_string.replace(')', '').replace(',', '').replace('(', '').replace('e', ''))
# ------------------------------- will use later to weigh stockfish score deltas ------------------------------
    # if 0 < abs(clean_score):
    # if abs(clean_score) <= 50 and clean_score > 0:
    # print(f'{clean_score}, inaccuracy for white.')
    # if abs(clean_score) <= 50 and clean_score < 0:
    # print(f'{clean_score}, inaccuracy for black.')
    # if abs(clean_score) <= 50 and clean_score > 0:
    # print(f'{clean_score}, mistake for white.')
    # if abs(clean_score) <= 50 and clean_score < 0:
    # print(f'{clean_score}, mistake for black.')
    # if abs(clean_score) <= 50 and clean_score > 0:
    # print(f'{clean_score}, blunder for white.')
    # if abs(clean_score) <= 50 and clean_score < 0:
    # print(f'{clean_score}, blunder for black.')

print(board)
