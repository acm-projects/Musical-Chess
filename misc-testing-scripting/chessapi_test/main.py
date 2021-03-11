import requests
import io
import chess.pgn
import chess.svg
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
count = 0
color = None
for move in game.mainline_moves():  # this prints a board for every position in the game.
    board.push(move)
    count += 1
    if board.is_check():
        if count % 2 == 0:
            color = 'black'
        if count % 2 == 1:
            color = 'white'
        print(f'Move {count} by {color} is a check: {move}')
    boards.append(str(board))
    info = engine.analyse(board, chess.engine.Limit(depth=10))
    print(info['score'])
print(board)
