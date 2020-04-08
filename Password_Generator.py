import random
import string
while True:
    pass_len = int(input("Enter the Password length: (minimum 6 characters long) \n"))
    if pass_len > 6:
        letters = int(input("How many letters do you want: \n"))
        if letters > pass_len and letters < pass_len:
            print("Error.. Try Again!")
            pass
        else:
            print("Processing..")
        print("Rest of the characters will contain numbers, symbols, etc")
        break
    else:
        print("Length is too short! Try again")
        pass
alphabets = list(string.ascii_lowercase)    
alphabets.extend(string.ascii_uppercase)
random.shuffle(alphabets)
alphabets = random.choices(alphabets, k=letters)
diff = int(pass_len - letters)
num = [1,2,3,4,5,6,7,8,9,0]
num.extend(string.punctuation)
random.shuffle(num)
num = random.choices(num, k=diff)
alphabets.extend(num)
random.shuffle(alphabets)
password = "".join(map(str,alphabets))
print(f"Your generated password is:  {password}")
