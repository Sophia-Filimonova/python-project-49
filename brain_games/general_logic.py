import prompt


QUESTIONS_AMOUNT = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def general_logic(module):
    user_name = welcome_user()
    print(module.RULES_OF_GAME)
    for n in range(QUESTIONS_AMOUNT):
        correct_answer = module.generate_question()
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
