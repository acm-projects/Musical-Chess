import requests
import chess.engine
import io
import chess.pgn
from flask import Flask, jsonify, after_this_request, request
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

engine = chess.engine.SimpleEngine.popen_uci("stockfish_13_win_x64.exe")


@app.route('/')
def render_index():
    return render_template('index.html')


# chess.com implementation
@app.route('/api/chess/<name>/<year>/<month>/', methods=['GET'])
def get_games_no_opponent(name, year, month):
    # @after_this_request
    # def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return response

    api_result = {}

    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
    for i in range(0, len(games_raw.json()['games'])):

        if 'pgn' in games_raw.json()['games'][i]:
            game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
            board = chess.Board()
            moves_list = []
            scores = []
            colors = {}
            for move in game.mainline_moves():
                board.push(move)
                moves_list.append(str(move)[0] + str(move)[1] + '-' + str(move)[2:])
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
                             'result': result, 'winner': winner, 'end': end_position, 'moves': moves_list,
                             'scores': scores,
                             'colors': colors}
        else:
            pass
    return jsonify(api_result)


@app.route('/api/chess/<name>/<year>/<month>/<opponent>', methods=['GET'])
def get_games(name, year, month, opponent):
    games_raw = requests.get(f"https://api.chess.com/pub/player/{name}/games/{year}/{month}")
    api_result = {}
    colors = {}
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
                colors['name'] = 'White'
                colors['opponent'] = 'Black'
            else:
                enemy_username = game.headers["White"]
                colors['name'] = 'Black'
                colors['opponent'] = 'White'
            winner = game.headers["Termination"].split(' ')[0]
            api_result[i] = {'name': name, 'year': yearx, 'month': monthx, 'day': day, 'opponent': enemy_username,
                             'result': result,
                             'winner': winner, 'end': end_position, 'scores': scores}
            return jsonify(api_result)


# lichess api implementation

@app.route('/api/lichess/<name>/<year>/<month>/')
def get_games_li_no_opponent(name, year, month):
    # midnight first day  ->  #midnight last day month into timestamped seconds format
    first = datetime.strptime(f'01.{month}.{year} 01:00:00,76',
                              '%d.%m.%Y %H:%M:%S,%f')
    last = datetime.strptime(f'30.{month}.{year} 12:00:00,76',
                             '%d.%m.%Y %H:%M:%S,%f')
    first_stamp = first.timestamp() * 1000
    last_stamp = last.timestamp() * 1000

    url = f"https://www.lichess.org/api/games/user/{user}"

    request = requests.get(
        url,
        params={"since": first_stamp, "until": last_stamp, "opening": "true"},
        headers={"Accept": "application/x-chess-pgn"}
    )

    games_raw = request.content.decode("utf-8")
    return None


@app.route('/api/chess/<name>/<year>/<month>/<opponent>')
def get_games_li(name, year, month, opponent):
    return None
