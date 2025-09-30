from random import randint

import prompt


def b_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    number = randint(1, 100)
    counter = 0
    while counter < 3:
        print(f'''Answer "yes" if the number is even, otherwise answer "no". 
    Question: {number}''')
        answer = prompt.string('Your answer: ')
        real_answer = 'no'
        if number % 2 == 0:
            real_answer = 'yes'
        if answer == real_answer:
            number = randint(1, 100)
            print('Correct!')
            counter += 1      
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {real_answer}. Let's try again, {name}")
            break
    if counter == 3:        
        print(f'Congratulations, {name}!')      


