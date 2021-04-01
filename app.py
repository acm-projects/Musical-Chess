import requests
import chess.engine
import io
import chess.pgn
from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

engine = chess.engine.SimpleEngine.popen_uci("stockfish_13_win_x64_avx2.exe")


@app.route('/')
def render_index():
    return render_template('index.html')


# chess.com implementation
@app.route('/api/chess/<name>/<year>/<month>/')
def get_games_no_opponent(name, year, month):
    api_result = {}

    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")

    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        board = chess.Board()
        moves_list = []
        scores = []
        colors = {}
        for move in game.mainline_moves():
            board.push(move)
            moves_list.append(str(move))
            info = engine.analyse(board, chess.engine.Limit(time=0.005))
            scores.append(info['score'].white().score())
        date = (str(game.headers["Date"])).split('.')  # year, month, day
        yearx = date[0]
        monthx = date[1]
        day = date[2]
        end_position = game.headers['CurrentPosition']
        result = game.headers['Termination'].split(' ')[3]
        if result == 'game':
            result = 'abandoned'
        if game.headers["White"].lower() == name.lower():
            enemy_username = game.headers["Black"]
            colors['name'] = 'White'
            colors['opponent'] = 'Black'
        else:
            enemy_username = game.headers["White"]
            colors['name'] = 'Black'
            colors['opponent'] = 'White'
        winner = game.headers["Termination"].split(' ')[0]
        api_result[i] = {'name': name, 'year': yearx, 'month': monthx, 'day': day, 'opponent': enemy_username,
                         'result': result, 'winner': winner, 'end': end_position, 'moves': moves_list, 'scores': scores,
                         'colors': colors}
    return jsonify(api_result)


@app.route('/api/chess/<name>/<year>/<month>/<opponent>')
def get_games(name, year, month, opponent):
    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
    api_result = {}
    info = None
    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        board = chess.Board()
        moves_list = []
        scores = []
        for move in game.mainline_moves():
            board.push(move)
            moves_list.append(str(move))
            info = engine.analyse(board, chess.engine.Limit(time=0.01))
            scores.append(info['score'].white().score())
        end_position = game.headers['CurrentPosition']
        result = game.headers['Termination'].split(' ')[3]
        if result == 'game':
            result = 'abandoned'
        if opponent in game.headers['Black'] or opponent in game.headers['White']:
            date = (str(game.headers["Date"])).split('.')  # year, month, day
            yearx = date[0]
            monthx = date[1]
            day = date[2]
            if game.headers["White"].lower() == name.lower():
                enemy_username = game.headers["Black"]
            else:
                enemy_username = game.headers["White"]
            winner = game.headers["Termination"].split(' ')[0]
            api_result[i] = {'name': name, 'year': yearx, 'month': monthx, 'day': day, 'opponent': enemy_username,
                             'result': result,
                             'winner': winner, 'end': end_position, 'scores': scores}
            return jsonify(api_result)


# lichess api implementation
@app.route('/api/lichess/<name>/<year>/<month>/')
def get_games_li_no_opponent(name, year, month):
    return None
    

@app.route('/api/chess/<name>/<year>/<month>/<opponent>')
def get_games_li(name, year, month, opponent):
    return None
