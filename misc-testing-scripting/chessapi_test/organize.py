import requests
import io
import chess.pgn

pgn_store = []


def search(username, input_month, input_year, input_opponent):
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
                if game.headers["White"] == username:
                    enemy_username = game.headers["Black"]
                else:
                    enemy_username = game.headers["White"]
                winner = game.headers["Termination"].split(' ')[0]
                final_date = f'Game was played on {month}, {day}, {year} versus {enemy_username}; {winner} won.'
                print(final_date)


if __name__ == "__main__":
    in_username = input('Enter your chess.com username: ')
    month = input('Enter the month to get games from: ')
    year = input('Enter the year to get games from: ')
    opponent = input('If you\'re looking for a game against a specific opponent, enter their username: ')
    search(in_username, month, year, opponent)
