from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
        if divider % 2 == 0:
            divider += 1
        if divider % 3 == 0 and divider > 3:
            divider += 2
    return True


def generate_question():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {random_number}')
    return correct_answer
