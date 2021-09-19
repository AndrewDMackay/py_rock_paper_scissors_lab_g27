from flask import render_template, request
from models.player import Player
from models.game import *
from app import app


@app.route('/')
def home():
    return render_template('index.html', title='home')

@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html', title='welcome')

@app.route('/rock', methods=['GET'])
def rock():
    return render_template('rock.html', title='rock')

@app.route('/scissors', methods=['GET'])
def scissors():
    return render_template('scissors.html', title='scissors')

@app.route('/paper', methods=['GET'])
def paper():
    return render_template('paper.html', title='paper')

@app.route('/<player_choice_1>/<player_choice_2>')
def play_game(player_choice_1, player_choice_2):
    player_1 = Player("Player 1", player_choice_1)
    player_2 = Player("Player 2", player_choice_2)
    game = Game(player_1, player_2)
    game.play()
    result = game.play()
    return render_template("result.html", result = result)

    # Alternate, previously returned formatted string in browser.. 

    # return (f"Player 1 chose {player_choice_1}!  Player 2 chose {player_choice_2}! {result}")

@app.route('/cpu', methods=['GET'])
def cpu():
    return render_template('cpu.html', title='cpu')

@app.route('/cpu', methods=['POST'])
def play_game_cpu():
    input_player_name = request.form["player-name"]
    input_player_choice_1 = request.form['player-choice']
    possible_choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(possible_choices)
    cpu_name = "RPS.BOT.v1.01"
    player_1 = Player(input_player_name, input_player_choice_1)
    player_2 = Player(cpu_name, cpu_choice)
    game = Game(player_1, player_2)
    game.play_cpu()
    result = game.play_cpu()
    return render_template("result.html", result = result)