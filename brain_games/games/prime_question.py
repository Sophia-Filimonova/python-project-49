import prompt
from random import randint


def is_prime(number):
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
        if divider % 2 == 0:
            divider += 1
        if divider % 3 == 0 and divider > 3:
            divider += 2
    return True


def prime_one_question():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')
    return (correct_answer, user_answer)
