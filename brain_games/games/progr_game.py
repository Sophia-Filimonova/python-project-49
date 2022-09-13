from random import randint


RULES_OF_GAME = 'What number is missing in the progression?'


def generate_question():
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
    return correct_answer
