import requests
import io
import chess.pgn
pgn_store = []
username = input("Enter your username here: ")
input_month = input("What month would you like to get games from? ")
input_year = input("What year would you like to get games from? ")
input_opponent = input("If you are looking for a game versus a specific opponent, type their username here; "
                       "otherwise, leave blank: ")
games_raw = requests.get(f"https://api.chess.com/pub/player/{username}/games/{input_year}/{input_month}")

if not input_opponent:
    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        date = (str(game.headers["Date"])).split('.')  # year, month, day
        year = date[0]
        month = date[1]
        day = date[2]
        enemy_username = ' '
        if game.headers["White"] == username:
            enemy_username = game.headers["Black"]
        else:
            enemy_username = game.headers["White"]
        winner = game.headers["Termination"].split(' ')[0]
        final_date = f'Game was played on {month}, {day}, {year} versus {enemy_username}; {winner} won.'
        print(final_date)
else:
    for i in range(0, len(games_raw.json()['games'])):
        game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
        if input_opponent in game.headers['Black'] or input_opponent in game.headers['White']:
            date = (str(game.headers["Date"])).split('.')  # year, month, day
            year = date[0]
            month = date[1]
            day = date[2]
            enemy_username = ' '
            if game.headers["White"] == username:
                enemy_username = game.headers["Black"]
            else:
                enemy_username = game.headers["White"]
            winner = game.headers["Termination"].split(' ')[0]
            final_date = f'Game was played on {month}, {day}, {year} versus {enemy_username}; {winner} won.'
            print(final_date)
