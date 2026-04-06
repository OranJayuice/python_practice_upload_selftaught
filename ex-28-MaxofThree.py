a = []
for i in range(3):
    a.append(int(input(f"number {i + 1}: ")))
def Num_sort(list):
    max_num = 0
    for i in list:
        if i > max_num:
            max_num = i
        else:  continue    
    return max_num
print(f"the max number is {Num_sort(a)}")