import os
from time import sleep

from utils import generate_number, is_number, get_number_from_user, clear_screen


def generate_sequence(length_of_list):
    sequence = []

    for element in range(0, length_of_list):
        sequence.append(generate_number(100))

    return sequence


def get_list_from_user(length_of_list):
    user_sequence = []
    user_first_number = get_number_from_user(0, 100, 'Please enter the first number in the list')
    user_sequence.append(user_first_number)

    for element in range(0, length_of_list - 1):
        user_next_number = get_number_from_user(0, 100, 'Please enter the next number in the list')
        user_sequence.append(user_next_number)

    return user_sequence


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    if not is_number(difficulty):
        return print('Error, difficulty is not a number')

    sequence = generate_sequence(difficulty)
    print(sequence)

    clear_screen()

    user_sequence = get_list_from_user(difficulty)
    result = is_list_equal(sequence, user_sequence)

    print(sequence, user_sequence)
    print(f'Your answer is {result}')
    return result
