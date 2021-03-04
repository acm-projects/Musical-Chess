from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def render_index():
    render_template('index.html')


@app.route('/board')
def render_board():
    render_template('board.html', board='insert board here')