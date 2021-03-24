import requests
import io
import chess.pgn
from flask import Flask, jsonify
from flask import render_template
app = Flask(__name__)


@app.route('/')
def render_index():
    render_template('index.html')


# chess.com implementation
@app.route('/api/<name>/<year>/<month>/')
def get_games_no_opponent(name, year, month):
    api_result = {}
    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        date = (str(game.headers["Date"])).split('.')  # year, month, day
        yearx = date[0]
        monthx = date[1]
        day = date[2]
        if game.headers["White"] == name:
            enemy_username = game.headers["Black"]
        else:
            enemy_username = game.headers["White"]
        winner = game.headers["Termination"].split(' ')[0]
        api_result[i] = {'name': name, 'year': yearx, 'month': monthx, 'day': day, 'opponent': enemy_username, 'winner': winner}
    return jsonify(api_result)


@app.route('/api/<name>/<year>/<month>/<opponent>')
def get_games(name, year, month, opponent):
    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
    api_result = {}
    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        if opponent in game.headers['Black'] or opponent in game.headers['White']:
            date = (str(game.headers["Date"])).split('.')  # year, month, day
            yearx = date[0]
            monthx = date[1]
            day = date[2]
            if game.headers["White"] == name:
                enemy_username = game.headers["Black"]
            else:
                enemy_username = game.headers["White"]
            winner = game.headers["Termination"].split(' ')[0]
            api_result[i] = {'name': name, 'year': yearx, 'month': monthx, 'day': day, 'opponent': enemy_username,
                            'winner': winner}
            return jsonify(api_result)
