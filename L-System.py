import turtle
from turtle import *

rules = {
    "Fl": "Fr[+Fl][-Fl]",  # Fl:
    "Fr": "FrFr"             # Fr:FrFr 使其主幹不斷上升
}


def draw(path, d, angle):
    stack = []
    lst = path_split(path)
    for symbol in lst:
        if symbol == "Fl" or symbol == "Fr":
            turtle.forward(d)
        elif symbol == "-":
            turtle.left(angle)
        elif symbol == "+":
            turtle.right(angle)
        elif symbol == "[":
            #處存位置
            stack.append((turtle.position(), turtle.heading())) 
        elif symbol == "]":
            #回歸上次處存位置並刪除此位置
            pos, head = stack.pop() 
            turtle.penup() 
            turtle.setposition(pos)
            turtle.setheading(head)
            turtle.pendown()


def path_split(path):
    i = 0
    lst = []
    while i < len(path):
        if path[i] == "F":
            lst.append(path[i:i+2])
            i += 2
        else:
            lst.append(path[i])
            i += 1
    return lst


def apply_rules(rules, path):
    lst = path_split(path)
    np_lst = []
    for i in range(len(lst)):
        symbol = lst[i]
        if symbol in rules:
            np_lst.append(rules[symbol])
        else:
            np_lst.append(symbol)
    return "".join(np_lst)


path = "Fl"
n = 7
d = 2
angle = 45


for i in range(n):
    path = apply_rules(rules, path)
print(path)
turtle.left(90)
turtle.speed(0)
turtle.delay(0)

draw(path, d, angle)
turtle.exitonclick()
