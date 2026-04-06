RPS = ["rock", "paper", "scissors"]
def compare(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        print ("It's a tie!");
    elif user1_choice == RPS[0]:
        if user2_choice == RPS [1]:
            print (f"{user2} won!")
        elif user2_choice == RPS [2]:
            print (f"{user1} won!")
        else:
            pass
    elif user1_choice == RPS[1]:
        if user2_choice == RPS [2]:
            print (f"{user2} won!")
        elif user2_choice == RPS [0]:
            print (f"{user1} won!")
        else:
            pass
    elif user1_choice == RPS[2]:
        if user2_choice == RPS [0]:
            print (f"{user2} won!")
        elif user2_choice == RPS [1]:
            print (f"{user1} won!")
        else:
            pass
    else:        pass            
        
                        
    

user1 = str(input("enter player 1's name: "))
user2 = str(input("enter player 2's name: "))

user1_choice = str(input(f"{user1}, enter rock, paper, or scissors: ").lower())
user2_choice = str(input(f"{user2}, enter rock, paper, or scissors: ").lower())

compare(user1_choice , user2_choice)

    