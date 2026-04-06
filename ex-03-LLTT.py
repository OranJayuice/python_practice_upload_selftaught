my_list = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
add_list = [] 
user_list = []
count = 0
for j in my_list:
    count += 1
for i in range(count):
    if my_list[i] < 5:
        add_list.append(my_list[i])
add_list.sort()
print(add_list)

num = eval(input("input number to compare to the numbers in list: "))
for i in range(count):
    if my_list[i] < num:
        user_list.append(my_list[i])
user_list.sort()
print(user_list)