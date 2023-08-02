import random
from utils import get_number_from_user, generate_number, is_number


def compare_results(user_guess, secret_number):
    return user_guess == secret_number


def play(difficulty):
    if not is_number(difficulty):
        return print('Error, difficulty is not a number')

    user_guess = get_number_from_user(0, difficulty,
                                      f'The computer will select a number between 0 and {difficulty}, '
                                      f'can you guess what that number is?')
    secret_number = generate_number(difficulty)

    print(f'Your nuber was {user_guess}, and the computer selected {secret_number}')

    return compare_results(user_guess, secret_number)
