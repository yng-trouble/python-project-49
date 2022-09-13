import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


def test_print():
    print('test')
