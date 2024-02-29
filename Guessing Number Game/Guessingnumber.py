"""
Number Guessing Game
"""
import random
rand_num=random.randint(1,30)
chance=5
print("***************NUMBER GUESSING GAME*****************")
print("You Have Only 5 Chances......")

while(chance!=0):
    guess=int(input("Enter the Number:"))
    if(guess==rand_num):
        print("Congratualations...... \n-----YOU WON-----")
        print("Your Score:",chance)
        break
    else:
        chance-=1
        print("You Have only",chance,"chances")
        if(guess>rand_num):
            print("Your Guess has Higher then Target")
        else:
            print("Your Guess has Lower then target")
if(chance==0):
    print("Better Luck Next Time \n-----YOU LOST-----")
print("I Hope You Enjoy it \n%%%THANK YOU%%%")
