#!/usr/bin/env python3

from brain_games.games.welcome_user import welcome_user
from brain_games.games.calc_question import calc_one_question
from brain_games.games.general_logic import general_logic


def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    general_logic(user_name, calc_one_question)


if __name__ == '__main__':
    main()
