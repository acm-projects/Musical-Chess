import requests

from datetime import datetime

# Basic Info
user = input("Enter ur username: ")
year = input("enter the year: ")
month = input("enter the month: ")


#gets user as x-ndjson
#finds the users lichess data
url = f"https://www.lichess.org/api/games/user/{user}"

#midnight first day 
first = datetime.strptime(f'01.{month}.{year} 01:00:00,76',
                           '%d.%m.%Y %H:%M:%S,%f')                      
#midnight last day month
last = datetime.strptime(f'28.{month}.{year} 12:00:00,76',
                           '%d.%m.%Y %H:%M:%S,%f')
#milliseconds
first_stamp = first.timestamp() * 1000
last_stamp = last.timestamp() * 1000

print(f'{first_stamp} {last_stamp}')

#prints out in json format
request = requests.get(
    url,
    params={"since":str(first_stamp) , "until":str(last_stamp),  "opening":"true"},
    headers={"Accept": "application/x-chess-pgn"}
)

# #splits games up
games_raw = request.content.decode("utf-8")

print(games_raw)


# games = [json.loads(s) for s in games_raw.split("\n")[:-1]]

# # #prints out games in nice format
# for i in games:
#     a = json.dumps(i,indent = 2)
#     print(a)













