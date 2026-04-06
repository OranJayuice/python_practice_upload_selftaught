a, n, d = eval(input("input three number for Arimetic Progression the (start , the end , common difference):"))
total = 0
amount = 0
print("the progression:", end=" ")
for i in range(a, n+1, d):
    amount += 1
    total += i
    print(i, end=" ")
print("")
print("amount of number=", amount)
print("the sum of ap:", total)

