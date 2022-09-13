from random import randint


RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {random_number}')
    return correct_answer