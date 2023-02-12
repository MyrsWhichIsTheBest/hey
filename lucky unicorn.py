import random


def int_check(integer):
    try:
        float(integer)
    except:
        raise Exception("Is not type INT")


def prize(number):
    int_check(number)
    if number <= 100:
        x = "Donkey"
        moni = 0
    elif number <= 170:
        x = "Horse"
        moni = 1
    elif number <= 185:
        x = "Zebra"
        moni = 2
    elif number <= 199:
        x = "Pegasus"
        moni = 4
    else:
        x = "Unicorn"
        moni = 11
    return {'x': x, 'moni': moni}


def lucky_unicorn(credit):
    flop = 0
    for loops in range(credit):
        credit -= 1
        dic = prize(random.randint(0, 200))
        print(f"You got a {dic['x']}! You get ${dic['moni']} back!")
        credit += dic['moni']
        print(credit)
        flop += 1
        print(f"iteration {flop}")


lucky_unicorn(int(input()))
