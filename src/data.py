from random import randint


class User:
    user_name = 'Anna'
    email = 'anpobeg12555@gmail.com'
    password = 'Zxcvbnm091555'


class TestUser:
    user_name = f'test{randint(0, 999)}'
    email = f'test{randint(0, 999)}@gmail.com'
    password = f'pass{randint(0, 999)}word'
