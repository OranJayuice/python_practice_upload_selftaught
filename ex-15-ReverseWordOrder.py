My_sen = str(input("input a sentence:"))
def Reverse_sen(a):
    O_list = a.split(" ")
    R_list = []
    for i in range(-1, -len(O_list) - 1,-1):
        R_list.append(O_list[i])
    R_str = " ".join(R_list)
    return R_str
print(Reverse_sen(My_sen))