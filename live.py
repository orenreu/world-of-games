import guess_game
import currency_roulette_game
import memory_game
from score import add_score, get_score


def get_user_name():
    name = input('Hi, what is your name?')
    return name


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.'


def load_game():
    games = [memory_game, guess_game, currency_roulette_game]
    try:
        selected_game = int(input('Please choose a game to play: \n1. Memory Game - a sequence of numbers will '
                                  'appear for 1 second and you have to guess it back \n2. Guess Game - guess a number '
                                  'and see if you chose like the computer \n3. '
                                  'Currency Roulette - try and guess the value of a random amount of USD in ILS'))

        selected_difficulty = int(input('Please choose game difficulty from 1 to 5:'))
    except ValueError:
        print('Error, value is not a number.')
        return load_game()

    if selected_game < 1 or selected_game > 4:
        return print('Error: Not a valid game.')

    if selected_difficulty < 1 or selected_difficulty > 5:
        return print('Error: Not a valid difficulty.')

    game_result = games[selected_game - 1].play(selected_difficulty)

    if game_result:
        add_score(selected_difficulty)

    score = get_score()
    print(f'Your score is: {score["score"]}')

    try:
        play_again = int(input('Would you like to play another game? 1: yes, 2: no'))
    except ValueError:
        print('Error, value is not a number.')
        return load_game()

    if play_again == 1:
        load_game()
    else:
        return print('Bye Bye')
