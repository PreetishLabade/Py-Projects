"""Snake Water Gun Game
This is a single player game for a user
Other player will be computer
User will choose Snake or water or gun as input - S, W or G (IMP: ENTER IN CAPITALS ONLY)
Computer will also generate Snake or water or gun randomly
Game rules are:
Snake Vs Water - Snake drinks water. Snake wins
Snake vs Gun - Gun kills snake. Gun wins
Water vs Gun - Gun drowns in water. Water wins
This game will be played for 10 rounds
Every win in a round will credit 10 points to the winner
Finally, whoever will have max points in the 10 rounds, will be the winner
Winner and points of each user and computer will be displayed after each round
"""

import random
game = ["Snake", "Water", "Gun"]
computer = random.choice(game)

computer_points = 0
user_points = 0
counter = 0
user1 = ""
username = input("Hey user! Please enter you name to continue.")
print(f"Hi {username}!!Lets start the game!")

while counter != 10:
    computer = random.choice(game)
    user = input("Enter S for Snake, W for Water or G for Gun")
    if user == "S":
        user1 = "Snake"
    elif user == "W":
        user1 = "Water"
    elif user == "G":
        user1 = "Gun"
    if (computer == "Snake" and user == "W") or (computer == "Gun" and user == "S") or (computer == "Water" and user == "G"):
        computer_points = computer_points + 10
        counter = counter + 1
        print(f"{username} chose {user1}. Computer chose {computer}. Computer won this round!")
        print("Computer points ",computer_points)
        print("User points ",user_points)
        print(10 - counter, "rounds to go.")
    elif (computer == "Snake" and user == "S") or (computer == "Gun" and user == "G") or (computer == "Water" and user == "W"):
        computer_points = computer_points + 0
        user_points = user_points + 0
        print(f"{username} chose {user1}. Computer also chose {computer}. This was a tie!")
        print("Computer points ",computer_points)
        print("user points ",user_points)
        print(10 - counter, "rounds to go.")
    elif (computer == "Water" and user == "S") or (computer == "Snake" and user == "G") or (computer == "Gun" and user == "W"):
        user_points = user_points + 10
        counter = counter + 1
        print(f"{username} chose {user1}. Computer chose {computer}. {username} won this round!")
        print("Computer points ",computer_points)
        print("user points ",user_points)
        print(10 - counter, "rounds to go.")
    else:
        print("Please enter a valid input")
        print(10 - counter, "rounds to go.")

if computer_points > user_points:
    print("Computer wins!!")
elif computer_points == user_points:
    print("This game was tied!! Play again!")
else:
    print(f"{username} wins!!")