import random

guess_no = random.randint(0,20)
print("Chances given: 3")
user_no = int(input("Enter your guess: \n"))
if user_no == guess_no:
    print("Correct Guess")
else:
    if(user_no > guess_no):
        print("Guess is too high!")
        print(f"Correct guess was {guess_no}")          
    else:
        print("Guess is too low!")
        print(f"Correct guess was {guess_no}")
    
