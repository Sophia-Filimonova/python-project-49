import prompt
from random import randint


def even_one_question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: ', random_number)
    user_answer = prompt.string('Your answer: ')
    return (correct_answer, user_answer)
