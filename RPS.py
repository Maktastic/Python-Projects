import random

user_wins = 0
comp_wins = 0

#Getting user input
def UserChoice():
    user_choice = input("Select Rock, Paper or Scissors: ")
    if user_choice in ['Rock', 'rock', 'r', 'R']:
        user_choice = 'r'
    elif user_choice in ['Paper', 'paper', 'p', 'P']:
        user_choice = 'p'
    elif user_choice in ['Scissors', 'scissors', 's', 'S']:
        user_choice = 's'
    else:
        print("Invalid Option, Try Again!")
        UserChoice()
    return user_choice

#Randomize Computer input
def CompChoice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = 'r'
    elif comp_choice == 2:
        comp_choice = 'p'
    elif comp_choice == 3:
        comp_choice = 's'
    return comp_choice

while True:
    user_choice = UserChoice()
    comp_choice = CompChoice()

    if user_choice == 'r':
        if comp_choice == 'r':
            print("User choice: Rock \t Computer Choice: Rock")
            print("Draw")
        elif comp_choice == 'p':
            print("User choice: Rock \t Computer Choice: Paper")
            print("Comp Wins!")
            comp_wins += 1
        elif comp_choice == 's':
            print("User choice: Rock \t Computer Choice: Scissors")
            print("User Wins!")
            user_wins += 1

    if user_choice == 'p':
        if comp_choice == 'r':
            print("User choice: Paper \t Computer Choice: Rock")
            print("User Wins!")
            user_wins += 1
        elif comp_choice == 'p':
            print("User choice: Paper \t Computer Choice: Paper")
            print('Draw')
        elif comp_choice == 'r':
            print("User choice: Paper \t Computer Choice: Scissors")
            print("Computer wins")
            comp_wins += 1

    if user_choice == 's':
        if comp_choice == 'r':
            print("User choice: Scissors \t Computer Choice: Rock")
            print("Computer Wins!")
            comp_wins += 1
        elif comp_choice == 'p':
            print("User choice: Scissors \t Computer Choice: Paper")
            print('User Wins!')
            user_wins += 1
        elif comp_choice == 'r':
            print("User choice: Scissors \t Computer Choice: Scissors")
            print("Draw")
    
    print("")
    print(f"User Score : {user_wins} \t Computer Score : {comp_wins}")
    print("")

    user_choice = input("Do you want to play again? (y/n) \n")
    if user_choice in ['Yes', 'y', 'Y', 'yes']:
        pass
    elif user_choice in ['No', 'n', 'no', 'N']:
        print("Thank you for Playing!")
        break
    else:
        print("Thank you for playing!")
        break
