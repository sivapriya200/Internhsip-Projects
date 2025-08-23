import random 

randomNum=random.randint(1,10)

while True:
    guessnum=int(input("Guess the number: "))
    if(randomNum==guessnum):
        print("Correct Guess")
    elif(randomNum>guessnum):
        print("Your guess is too small...")
    else:
        print("Your guess is too large")