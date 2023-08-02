import random
import os
from time import sleep


def is_number(var):
    return type(var) == int


def generate_number(top_number):
    return random.randint(0, top_number + 1)


def get_number_from_user(start, end, message):
    try:
        user_number = int(input(message))
        if user_number > end or user_number < start:
            print('The value you entered is not in range, please try again')
            return get_number_from_user(start, end)

        return user_number
    except ValueError:
        print('The value you entered is not a number, please try again')
        return get_number_from_user(start, end)


score_file_path = 'user_score.txt'

bad_return_code = 400


def clear_screen():
    sleep(0.7)
    os.system('clear')
