def search (ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
        else:   return False
if __name__=="__main__" :
     l = [2, 4, 6, 8, 10]
print(search(l, 5)) 
print(search(l, 10)) 
print(search(l, -1)) 
print(search(l, 2)) 