import random
import string
from os import system, name
from time import sleep

def Get_Word():
    link = open('sowpods.txt')
    dictionary = list(link)
    dictionary = [x.rstrip() for x in dictionary]
    return random.choice(dictionary)

def clear():
    if name == 'nt':
        _ = system('cls')

def Play_Again():
    ans = input("Do you want to play again? Y/N").lower()
    if ans == 'y' or ans == 'yes':
        clear()
        Play_Game()
    else:
        print("GoodBye! Signing off...")
        exit()

def Play_Game():
    alphabets = string.ascii_letters
    word = Get_Word()
    l_guessed = []
    chances = 6
    guessed = False

    print(f"The Word contains {len(word)} letters")
    print(len(word) * '*')
    while guessed == False and chances > 0:
        print(f"You have {chances} left!")
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1:
            if guess not in alphabets:
                print("No Letter Detected!")
            elif guess in l_guessed:
                print('Letter has been already guessed!')
            elif guess not in word:
                print('Sorry, Letter is not part of the word')
                l_guessed.append(guess)
                chances -= 1
            elif guess in word:
                print("Good Work")
                l_guessed.append(guess)
            else:
                print("Unknown Error Detected!")
        elif len(guess) == len(word):
            if guess == word:
                print("Congratulations, You have guessed the word!")
                print(f"The Word is {guess}")
                guessed = True
            else:
                print("Sorry, This isn't the word we are looking for!")
                chances -= 1
        else:
            print("Length of Word Mismatch!")

        status = ''
        if guessed == False:
            for letter in word:
                if letter in l_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)
        if status == word:
            print("Well Done, You have guessed the word!")
            guessed = True
        elif chances == 0:
            print("You are out of chances!")
            print(word)

    Play_Again()

Play_Game()
