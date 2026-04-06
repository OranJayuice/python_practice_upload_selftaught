num = eval(input("Please, input a number here: "))
check = eval(input("Please, provide a number to divide the first one by: "))
if num % 4 ==0: 
    print(f"{num} is a multiple of four!")
elif num % 2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")

if num % check == 0:
    print(f"{num} can be divided evenly by {check}!")
else:
    print(f"{num} can't be divided evenly by {check}!")