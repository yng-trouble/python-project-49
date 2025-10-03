from random import randint

import prompt

import brain_games.engine as ngin


def b_even():
    number = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while ngin.counter < 3:
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        real_answer = 'no'
        if number % 2 == 0:
            real_answer = 'yes'
        if answer == real_answer:
            number = randint(1, 100)
            print('Correct!')
            ngin.counter += 1      
        else:
            print(
                f"{answer} is wrong answer ;(." 
                f"Correct answer was {real_answer}.\n"
                f"Let's try again, {ngin.name}"
                )
            quit()

       
       
      


