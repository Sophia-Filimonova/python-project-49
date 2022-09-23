from random import randint
import math


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, int(math.sqrt(number) + 1)):
        if number % divider == 0:
            return False
    return True


def generate_question():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (correct_answer, str(random_number))
