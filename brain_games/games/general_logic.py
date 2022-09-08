def general_logic(user_name, one_question):
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
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")
