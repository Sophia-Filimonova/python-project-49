#!/usr/bin/env python3

from brain_games.games.welcome_user import welcome_user
from brain_games.games.even_question import even_one_question
from brain_games.games.general_logic import general_logic


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    general_logic(user_name, even_one_question)


if __name__ == '__main__':
    main()