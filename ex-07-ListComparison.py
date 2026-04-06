a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# List comprehension solution no.1
b = []
for i in a :
    if i % 2 == 0:
        b.append(i)
    else:        pass
print(b)
# List comprehension solution no.2
c = [i for i in a if i % 2 == 0]
print(c)