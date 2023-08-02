from flask import Flask
from score import get_score


def score_content(score):
    return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{score}</div></h1></body></html>'


def error_content(error_code):
    return f'<html><head><title>Scores Game</title></head><body><h1><div id="score" style="color:red">{error_code}</div></h1>/body></html>'


def score_server():
    app = Flask(__name__)

    @app.route('/')
    def home():
        score = get_score()

        if score['success']:
            return score_content(score['score']), 200
        else:
            return error_content(score['error_code'])

    app.run(port=3000)
