from random import randint

def id_generator():
    return int(''.join([str(randint(1, 9)) for number in range(5)]))
