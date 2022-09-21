from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, int(number / 2 + 1)):
        if number % divider == 0:
            return False
    return True


def generate_question():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {random_number}'
    return (correct_answer, question)
