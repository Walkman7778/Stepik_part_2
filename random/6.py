# task here --- https://stepik.org/lesson/356380/step/7?unit=340495
from string import ascii_uppercase as AU
from random import choice as C
from random import randrange as R

def generate_index():
    return f'{C(AU)}{C(AU)}{R(100)}_{R(100)}{C(AU)}{C(AU)}'