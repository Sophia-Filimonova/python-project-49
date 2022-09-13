from random import randint


RULES_OF_GAME = 'What is the result of the expression?'


def generate_question():
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
    return correct_answer
