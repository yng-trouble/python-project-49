from random import randint

import prompt

import brain_games.engine as ngin


def b_gcd():
    a = randint(0, 20)
    b = randint(0, 20)
    gcd = 'something'
    numbers = [a, b]
    print('Find the greatest common divisor of given numbers.')
    while ngin.counter < 3:
        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')
        if b == 0:
            gcd = a
        elif a == 0:
            gcd = b
        # might as well get some rest    
        while b != 0 and a != 0:
            if max(numbers) % min(numbers) == 0:
                gcd = min(numbers)
            rem = a % b
            a = b
            b = rem
        if b == 0:
            gcd = a
        if answer == str(gcd):
            print('Correct!')
            a = randint(0, 20)
            b = randint(0, 20) 
            numbers = [a, b]
            ngin.counter += 1
        else:
            print(
                f"{answer} is wrong answer ;(. " 
                f"Correct answer was {gcd}\n."
                f"Let's try again, {ngin.name}!"
                )
            quit()

