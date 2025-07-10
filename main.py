import random

n=random.randint(1,100)
a=-1
guesses =1

while(a != n):
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number pls!")
        guesses+=1
    elif(a<n):
        print("Higher number pls!")
        guesses+=1
print(f"Your guessed number {n} correctly in {guesses} attempts")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore2.txt", "w") as f:
        f.write(str(guesses))
