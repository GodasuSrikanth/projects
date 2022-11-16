#Rolling the dice
import random

def roll_dice():
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes". lower():
        dice1 = random.randint(1, 6) #3
        dice2 = random.randint(1, 6) #4

        print("dice rolled: {} and {}". format(dice1, dice2))
       
        roll = input("Roll again? (Yes/no): ")
roll_dice()