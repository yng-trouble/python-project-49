#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if not answer == 'no' and number % 2 != 0:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
            break
        elif not answer == 'yes' and number % 2 == 0:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
            break
        elif ((answer == 'no' and number % 2 != 0) or
                (answer == 'yes' and number % 2 == 0)):
            print('Correct!')

            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
