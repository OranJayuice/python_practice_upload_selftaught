import datetime
name = str(input("please enter your name: "))
age = int(input("please enter your age: "))
curr = datetime.datetime.now()
print(f"{name} will turn 100 in {curr.year - age + 100}")