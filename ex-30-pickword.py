import random
import os.path
words = []
with open(os.path.join("C:/Users/arp10/OneDrive/桌面/practice","SOWPODS.txt")) as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)
rand_index = random.randint(0,len(words) - 1)
print(f"random word: {words[rand_index]}")
