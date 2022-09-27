#!/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"""Hello, {name}
What is the result of the expression?""")
    count = 0
    operators = ['+', '-', '*']

    while count < 3:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        rand_op = random.choice(operators)
        rand_expression = f'{number_1} {rand_op} {number_2}'

        print(f'Question: {rand_expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(eval(rand_expression)):
            print('Correct!')
            count += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{eval(rand_expression)}'.""")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
