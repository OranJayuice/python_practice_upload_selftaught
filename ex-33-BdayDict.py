birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Rowan Atkinson': '01/6/1955'}
print("Welcome to the Birthday dictionary. We know the birthday of:")
for name in birthdays:
    print (name)
check_name = str(input("Whose birthday you want to look up? : "))
if check_name in birthdays:
    print(f"{check_name}\'s birthday is {birthdays[check_name]}.")
else:
    print(f"sorry wee might not have {check_name}\'s birthday.")