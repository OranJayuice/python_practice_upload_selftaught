import random
name = str(input("enter your name(totally not relevant): "))
secu_lev = int (input ("enter the security level(1-3) of the password: "))
pass_num = ""
password = ""
lower_sample = str("abcdefghijklmnopqrstuvwxyz")
upper_sample = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_sample =str("1234567890")
sign_sample = str("!@#$%-.")
word_sample = [f"{name}IsCool", "NugggetHead","BirdAvid", "Birdbrain", "IdkIHateMakingPassword" ,"TheOriginal"]
if secu_lev == 1 :
    for i in range(3):
        pass_num = pass_num + num_sample[random.randrange(0,len(num_sample))]
    password = word_sample[random.randrange(6)] + pass_num
elif secu_lev == 2:
    for i in range(12):
        pass_key = random.randint(1,3)
        if pass_key == 1:
            password = password + lower_sample[random.randrange(len(lower_sample))]
        elif pass_key == 2:
            password = password + upper_sample[random.randrange(len(upper_sample))]
        else:
            password = password + num_sample[random.randrange(len(num_sample))]
else:
    for i in range(16):
        pass_key = random.randint(1,4)
        if pass_key == 1:
            password = password + lower_sample[random.randrange(len(lower_sample))]
        elif pass_key == 2:
            password = password + upper_sample[random.randrange(len(upper_sample))]
        elif pass_key == 3:
            password = password + num_sample[random.randrange(len(num_sample))]
        else:
            password = password + sign_sample[random.randrange(len(sign_sample))]
print (password)