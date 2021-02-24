import requests
import io
import chess.pgn
import chess.svg
import chess.engine
from flask import Flask, render_template, Markup
engine = chess.engine.SimpleEngine.popen_uci('stockfish_13_win_x64_avx2.exe')
pgn_store = []
username = input("Enter your username here: ")
games_raw = requests.get(f"https://api.chess.com/pub/player/{username}/games/2021/02")
games = games_raw.json()['games']
for _ in games:  # prints every game pgn for month of february
    pgn_store.append(games[0]['pgn'][20:])
# print(pgn_store)
pgn = io.StringIO(pgn_store[0])
# this makes a game object using chess package pgn parsing, and pushes the moves to a board.
game = chess.pgn.read_game(pgn)
board = game.board()
print(type(board))
svgs = []
boards = []
for move in game.mainline_moves():  # this prints a board for every position in the game.
    board.push(move)
    boards.append(str(board))
    svgs.append(chess.svg.board(board, size=400))
print(board)
info = engine.analyse(board, chess.engine.Limit(depth=10))
print(info['score'])
app = Flask(__name__)


@app.route('/')
def do_thing():
    return render_template('test.html', boards=boards)
