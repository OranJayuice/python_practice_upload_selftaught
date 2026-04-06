import random
def GG_2():
    g_count = 0
    result = False
    a=1
    b=101
    while result == False:
        guess = random.randrange(a+1,b)
        result = str(input(f"is {guess} your number?\nIs the number greater/lesser/yes: "))
        if result == "greater":
            a = guess
            result = False
        elif result == "lesser":
            b = guess
            result = False
        else:
            result = True
        g_count += 1
    print(f"I win! {guess} is your number, and I guessed {g_count} times!")
GG_2()