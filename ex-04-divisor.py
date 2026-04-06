num = eval(input("input a number to for its divisors: "))
divisors = []
for i in range (1,num + 1):
    if num%i == 0:
        divisors.append(i)
print(f"the divisors of {num} : {divisors}")
