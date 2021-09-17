from flask import render_template, request
from models.player import Player
from models.game import *
from app import app

@app.route('/rockpaperscissors')
def base():
    return render_template('base.html', title='Home')