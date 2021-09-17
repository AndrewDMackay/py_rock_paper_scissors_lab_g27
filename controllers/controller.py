from flask import render_template, request
from models.player import Player
from models.game import Game
from app import app

@app.route('/player1')
def base():
    return render_template('base.html', title='Player1')