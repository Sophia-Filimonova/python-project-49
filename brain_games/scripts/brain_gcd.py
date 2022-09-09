#!/usr/bin/env python3

from brain_games.games.welcome_user import welcome_user
from brain_games.games.gcd_question import gcd_one_question
from brain_games.games.general_logic import general_logic


def main():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    general_logic(user_name, gcd_one_question)


if __name__ == '__main__':
    main()
