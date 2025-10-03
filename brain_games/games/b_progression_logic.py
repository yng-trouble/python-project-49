from random import randint, choice

import brain_games.engine as ngin

import prompt


def make_progression():
    length = randint(5, 12)
    step = randint(1, 15)
    a_progression = [randint(0, 50)]
    while len(a_progression) < length:
        a_progression.append(a_progression[-1] + step)
    return a_progression

def b_progression():
    print('What number is missing in the progression?')
    while ngin.counter < 3:
        seq = make_progression()
        missing_number = choice(seq)
        i = seq.index(missing_number)
        q_seq = seq
        q_seq.pop(i)
        q_seq.insert(i, '..')
        print(f'Question: {q_seq}')
        answer = prompt.string('Your answer: ')
        if answer == str(missing_number):
            print('Correct!')
            seq = make_progression()
            q_seq = seq
            q_seq.insert(i, '..')
            ngin.counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {missing_number}. Let's try again, {ngin.name}")
            quit()