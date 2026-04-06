import random
gen_ans = list(str(random.randrange(1000, 10000)))
bulls = 0
print(gen_ans)
while bulls != 4:
    user_ans = list(input("please, enter a four digit number: "))
    cows = 0
    bulls = 0
    for i in range(len(user_ans)):
        if user_ans[i] == gen_ans[i]:
            bulls += 1
        else:
            if user_ans[i] in gen_ans:
                cows += 1
            else:
                pass
    print(f"cows:{cows}, bulls:{bulls}")
print("you did it!")
