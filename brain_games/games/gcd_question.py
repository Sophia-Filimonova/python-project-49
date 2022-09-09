import prompt
from random import randint


def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return number1


def gcd_one_question():
    number1 = randint(2, 50)
    number2 = randint(2, 50)
    correct_answer = gcd(number1, number2)
    print(f'Question: {number1} {number2}')
    user_answer = prompt.integer('Your answer: ')
    return (correct_answer, user_answer)
