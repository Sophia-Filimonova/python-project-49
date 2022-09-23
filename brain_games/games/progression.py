from random import randint


RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_question():
    progr_start = randint(1, 20)
    progr_step = randint(2, 5)
    index_miss_number = randint(0, PROGRESSION_LENGTH - 1)
    progression = []
    for i in range(PROGRESSION_LENGTH):
        current_number = progr_start + i * progr_step
        if i == index_miss_number:
            correct_answer = current_number
            progression.append('..')
        else:
            progression.append(str(current_number))
    progr_string = " ".join(progression)
    return (str(correct_answer), progr_string)
