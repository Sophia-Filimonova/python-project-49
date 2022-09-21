from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {random_number}'
    return (correct_answer, question)
