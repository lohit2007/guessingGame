import random
number = (random.randint(0,9))
print("Number Guessing Game")
print("Guess a Number (between 1 and 9):")
count = 0
while count < 5:
    guess = int(input("Enter your guess: "))
    if (guess < number):
        print("Too Low")
        count=count+1
    elif(guess > number):
        print("Too High")
        count=count+1
    else:
        print("You're Right")
        count = count+5
    

    