import os.path
name_counts = {}
with open(os.path.join("C:/Users/arp10/OneDrive/桌面/practice","nameslist.txt")) as f:
    for line in f:
        name = line.strip() 
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

for name, count in name_counts.items():
    print(f"{name}: {count}")