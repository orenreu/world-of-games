import datetime

from forex_python.converter import CurrencyRates
from utils import is_number, get_number_from_user, generate_number


def get_dollar_rate():
    rates = CurrencyRates()
    d = datetime.date(2023, 4, 28)

    rate = rates.get_rate("USD", "ILS", d)

    return rate


def get_money_interval(difficulty, random_number):
    dollar_rate = get_dollar_rate()
    actual_value = dollar_rate * random_number

    return {'bottom': actual_value - (5 - difficulty), 'top': actual_value + (5 - difficulty)}


def get_guess_from_user(number):
    user_guess = get_number_from_user(0, 500, f'Can you guess the value of ${number} dollars in Shekels?')
    return user_guess


def play(difficulty):
    if not is_number(difficulty):
        return print('Error, difficulty is not a number')

    random_number = generate_number(100)

    interval = get_money_interval(difficulty, random_number)

    user_guess = get_guess_from_user(random_number)

    actual_value = random_number * get_dollar_rate()

    print(f'Actual value is {actual_value}')

    if interval['bottom'] < user_guess < interval['top']:
        print(f'You were right. Top is {interval["top"]}, Bottom is {interval["bottom"]}')
        return True
    else:
        print(f'Your were wrong. Top is {interval["top"]}, Bottom is {interval["bottom"]}')
        return False
