# Musical-Chess
*Compose masterful musical melodies online using data from your best chess matches.*

---------------

# Overview
Our website allows users to import games from their Lichess or Chess.com accounts, and then it will generate music based on the moves played out in the game. 

# Project Features
1) Import games from popular chess websites Lichess and Chess.com by using their respective APIs.
2) Analyze board position using stockfish, and then retrieve centipawn loss from each move played in a game.
3) Generate music based on each moves centipawn loss.
4) Concurrently play the moves and the music for a chessgame
5) Simple user interface for ease of use.

# User interface
1) Enter a Chess.com or Lichess username, the month and year you want games from, and then hit get games based on which website an account is from. 
2) After the games are loaded in select the game you want by entering its assigned number.
3) Hit generate music
4) Hit change board position to played out the moves and music.

![image](https://user-images.githubusercontent.com/73033177/117071234-70d5f580-acf4-11eb-8028-b9d8208060fa.png)

# This Branch

This branch contains the API that backend has created in Flask, as well as a template index.html page containing a chessboard.

# To run: 

Make sure Python is installed, clone this repo, then install dependencies via `pip install`. 
Then, in terminal (Windows): `set FLASK_APP=app.py`
Then, in terminal (Windows): `flask run`
