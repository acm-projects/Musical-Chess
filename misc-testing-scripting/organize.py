import requests
import io
import chess.pgn
pgn_store = []
username = input("Enter your username here: ")
input_month = input("What month would you like to get games from? ")
input_year = input("What year would you like to get games from? ")
games_raw = requests.get(f"https://api.chess.com/pub/player/{username}/games/{input_year}/{input_month}")

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

for i in range(0, len(games_raw.json()['games'])):
    game = chess.pgn.read_game(io.StringIO(games_raw.json()['games'][i]['pgn']))
