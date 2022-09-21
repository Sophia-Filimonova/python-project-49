from random import randint, choice


RULES = 'What is the result of the expression?'


def generate_question():
    operator = choice('+-*')
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    elif operator == '*':
        first_number = randint(1, 25)
        second_number = randint(1, 10)
        correct_answer = first_number * second_number
    question = f'Question: {first_number} {operator} {second_number}'
    return (str(correct_answer), question)
