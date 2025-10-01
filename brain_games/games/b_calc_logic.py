from random import randint, choice

import brain_games.engine as engine

import prompt

def b_calc():
    num1 = randint(0, 30)
    num2 = randint(0, 30)
    operators = ['+', '-', '*']
    action = choice(operators)
    exp = eval(str(num1) + action + str(num2))
    
    print('What is the result of the expression?')
    while engine.counter < 3:
        print(f'Question: {str(num1)} {action} {str(num2)}')
        answer = prompt.string('Your answer: ')
        if answer == str(exp):
            engine.counter += 1
            print('Correct!')
            num1 = randint(0,30)
            num2 = randint(0,30)
            action = choice(operators)
            exp = eval(str(num1) + action + str(num2))
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {exp}. Let's try again, {engine.name}")
            quit()