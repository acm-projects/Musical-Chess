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
    dates = []
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
        final_date = f'Game was played on {monthx}, {day}, {yearx} versus {enemy_username}; {winner} won.'
        dates.append(final_date)
    return jsonify(dates)


@app.route('/api/<name>/<year>/<month>/<opponent>')
def get_games(name, year, month, opponent):
    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
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
            final_date = f'Game was played on {monthx}, {day}, {yearx} versus {enemy_username}; {winner} won.'
            return final_date
