from random import randint

import brain_games.engine as ngin

import prompt


def b_gcd():
    a = randint(0, 20)
    b = randint(0, 20)
    gcd = 'something'
    numbers = [a, b]
    print('Find the greatest common divisor of given numbers.')
    while ngin.counter < 3:
        gcd_question = print(f'Question: {a} {b}')
        answer = input('Your answer: ')
        while b != 0:
            if max(numbers) % min(numbers) == 0:
                gcd = min(numbers)
            rem = a % b
            a = b
            b = rem
            
            if b == 0:
                gcd = a
        if answer == str(gcd):
            print('Correct')
            a = randint(0, 20)
            b = randint(0, 20) 
            ngin.counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {gcd}. Let's try again, {ngin.name}")
            quit()

