print("DICE ROLLING GAME")
"""
           DICE ROLLING GAME
"""
import random
#import random number
count=0
score=0
total=0
roll_history=[]
score_history=[]
choice ='Y'
while choice=='Y':
    #roll dice
    die1=random.randint(1,6)
    #Generate a random number for dice 1
    die2=random.randint(1,6)
    #Generate a random number  for dice 2
    score=die1+die2
    #add score
    count+=1
    #count the roll
    total+=score
    #add score in total
    roll_history.append(count)
    score_history.append(score)
    print("Die 1:",die1)
    #Display result of dice 1
    print("Die 2:",die2)
    #Display result of dice 2
    choice=input("Would you like to roll again?(Y/N):")
    #Ask user if they want to roll again
    choice=choice.upper()
    while choice !='Y' and choice!='N':
        choice=input("PLease enter Y or N:")

print("Total score is:",total)
print("You rolled ",len(roll_history),"times")
print("Score history is:",score_history)

print("Game end")