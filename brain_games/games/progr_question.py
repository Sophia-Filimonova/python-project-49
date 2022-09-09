import prompt
from random import randint


def progr_one_question():
    progr_beginning = randint(1, 20)
    progr_step = randint(2, 5)
    index_miss_number = randint(1, 10)
    progr_string = ''
    current_number = progr_beginning
    i = 1
    while i <= 10:
        if i != index_miss_number:
            progr_string = progr_string + str(current_number) + ' '
            current_number = current_number + progr_step
            i += 1
        else:
            correct_answer = current_number
            progr_string = progr_string + '.. '
            current_number = current_number + progr_step
            i += 1
    progr_string = progr_string.strip()
    print(f'Question: {progr_string}')
    user_answer = prompt.integer('Your answer: ')
    return (correct_answer, user_answer)
