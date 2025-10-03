from random import randint

import prompt

import brain_games.engine as ngin


def b_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while ngin.counter < 3:
        num = randint(1, 100)
        div_counter = 0
        possible_divs = range(1, num // 2)
        for i in possible_divs:
            if num % i == 0:
                div_counter += 1
        real_answer = 'yes'
        if div_counter >= 2:
            real_answer = 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == real_answer:
            print('Correct!')
            ngin.counter += 1
            num = randint(1, 100)
            div_counter = 0 
        else:
            print(
                f"{answer} is wrong answer ;(." 
                f"Correct answer was {real_answer}.\n"
                f"Let's try again, {ngin.name}"
                )
            quit()