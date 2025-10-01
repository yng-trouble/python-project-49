from random import randint

import prompt

counter = 0
def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
    
name = greet_user()
    

def run(game):
    global counter
    game()
    if counter == 3:
        print(f'Congratulations, {name}!') 