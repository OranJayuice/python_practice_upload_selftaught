def first_Last (a, b):
    for i in range(0, -2, -1):
        b.append(a[i])
    print("This is the first and last element of the list: ", b)
import random
rand_list = list(random.sample(range(100), random.randint(2,15)))
print(rand_list)
fl_list= []
first_Last(rand_list, fl_list)
