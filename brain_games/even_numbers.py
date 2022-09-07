import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def one_question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: ', random_number)
    user_answer = prompt.string('Your answer: ')
    return (correct_answer, user_answer)


def even_game():
    user_name = welcome_user()
    i = 1
    while i <= 3:
        (correct_answer, user_answer) = one_question()
        if correct_answer == user_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            i = 10
    if i == 4:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")
