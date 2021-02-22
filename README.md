# Musical-Chess
*Compose masterful musical melodies online using data from your best chess matches.*

---------------

# Design Day
- Live gameplay with music generation
- Game submission
- Situation music (based on one board position rather than entire game)
- Major/minor moves based on chess engine output

## Design Day MVP
1. Upload completed games (pgn)
2. Connect to chess engine to evaluate board positions
3. Music algorithm
4. Users select instruments
5. Chess board displays moves in sync with music

## Design Day Stretch Goals
1. Download sound files
2. Live Chess moves
3. Pull games from a chess.com / Lichess account
4. Tactics like fork / pin will change music

## Music Generation ideas

----------------

This app accepts chess games (via pgn or fen files or through a Lichess / chess.com link) and composes music based on the moves. Intelligent moves create pleasing chord progressions and melodies, while mistakes and blunders create atonal, unpleasant sound. Alternatively, music generation could be based on piece type moved and location/distance.

> The ReadMe is not set in stone! We will be reviewing/adjusting MVP/Stretch goals on Design Day. You are also welcome and encouraged to do your own research at any time.

## Installations / Resources
### Frontend
* [ReactJS](https://reactjs.org/)
  * Either is fine to use. React requires extra libraries to do lots of things, but it is much more beginner-friendly.
* [Tone.js](https://tonejs.github.io/)
  * This is a framework for sound generation built on Web Audio API
  * [A handy demo](https://medium.com/dev-red/tutorial-lets-make-music-with-javascript-and-tone-js-f6ac39d95b8c)

### Backend
* [Chess UCI](https://ucichessengine.wordpress.com/description/) (Universal Chess Interface)
  * This is a protocol for accessing chess engines
  * Its documentation is extremely poor and lacks tutorials, but fortunately we're only using a small, simple part of its functionality (retrieving centipawn loss scores given FEN strings)
* Chess Engine
  * There are quite a few options. Some notable free ones are former world champion [Stockfish](https://stockfishchess.org/) and [Komodo](https://komodochess.com/)
* [Python](https://www.python.org/downloads/) or [Java](https://www.java.com/en/)
* [Git](https://git-scm.com/)
  * [Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Oracle](https://www.oracle.com/index.html) (maybe)
  * Whether a database is needed depends on what the music generation algorithm looks like and whether we will implement a browse feature. We will discuss more on Design Day!
