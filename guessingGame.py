# Write a small game which picks a random number, and has the user 
#guess until they get it right. The game should give hints about the
#user needs to guess lower or higher.
import random 
num = random.randint(1,10) 
guess = int(input("What is your guess from 1-10?"))
if guess == num:
    print("Congratulations, youve guessed it!")
if guess != num:
   while guess != num:
        print("try again!")
        if guess > num:
            print("try lower this time")
        if guess < num:
            print("try higher this time")
        guess = int(input(""))


