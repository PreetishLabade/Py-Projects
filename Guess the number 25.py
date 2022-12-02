"""We have selected number 25
Accept an input number from user
1.If this number is less than 25, print("Please select a greater number")
2.If this number is greater than 25, print("Please select a lesser number")
3.Total number of guesses allowed is 9
4.Print the number of guesses left after every input from user
5.If guesses are finished, print("Game Over")
6.If user guesses the number correctly, print("You won")"""

a = int(input("Welcome to our game!\nYou have 5 guessses\nPlease enter a number"))
i = 5

while(True):
    if a < 25 and i > 0:
        i = i - 1
        print("Please select a greater number")
        a = int(input())
        print("You have ", i, " guesses left")
    elif a > 25 and i > 0:
        i = i - 1
        print("Please select a lesser number")
        a = int(input())
        print("You have ", i, " guesses left")
    elif a == 25 and i > 0:
        print("Congrats!You won!")
        break
        continue
    else:
        print("Game Over")
        break
