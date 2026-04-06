
from matplotlib.pylab import randint


num = randint(1, 100)
guess = 0
counter = 0
while guess != num:
    guess = input("Enter your guess or 'exit' to quit: ").lower()
    if guess == "exit":
        print("Game exited.")
        break
    guess = int(guess)
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
    counter += 1

print(f"You made {counter} guesses.") 
