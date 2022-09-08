import prompt
from random import randint


def calc_one_question():
    random_operation = randint(1, 3)
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    if random_operation == 1:
        correct_answer = first_number + second_number
        print(f'Question: {first_number} + {second_number}')
    elif random_operation == 2:
        correct_answer = first_number - second_number
        print(f'Question: {first_number} - {second_number}')
    else:
        first_number = randint(1, 25)
        second_number = randint(1, 10)
        correct_answer = first_number * second_number
        print(f'Question: {first_number} * {second_number}')
    user_answer = prompt.integer('Your answer: ')
    return (correct_answer, user_answer)
