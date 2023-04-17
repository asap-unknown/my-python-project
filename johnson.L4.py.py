'''

NAME:   elijah johnson

DATE:   march 2, 2023

ASSN:   LAB ASSIGNMENT L3

DESC:   THE FOLLOWING PYTHON MODULE IMPLEMENTS THE FAMOUS ROCK,
        PAPER, SCISSORS GAME.  THE RULES OF THE GAME ARE SIMPLE.
        EACH PLAYER CHOOSES A ROCK (0), PAPER(1), OR SCISSORS (2).
        THE FOLLOWING ARE WINNING PLAYS:
        
        ROCK BEATS SCISSORS
        PAPER BEATS ROCK
        SCISSORS BEATS PAPER

'''

# COMPUTER CHOOSES ROCK, PAPER, OR SCISSORS BASED ON A RANDOM
# INTEGER CHOICE USING THE RANDINT() FUNCTION.
import random
game = ["0","1",'2']
computer_choice = random.choice(game)


# GET THE USER CHOICE, user_choice, USING THE input() function
# AS AN INTEGER

choice=input("enter your choice(rock = 0, paper = 1, sissors = 2): ")

# IMPLEMENT THE RULES OF THE GAME USING IF-ELIF-ELSE STATEMENTS
# IF PLAYER 1 CHOOSES ROCK AND PLAYER 2 CHOOSES SCISSORS, OR
# IF PLAYER 1 CHOOSES PAPER AND PLAYER 2 CHOOSES ROCK, OR
# IF PLAYER 1 CHOOSES SCISSORS AND PLAYER 2 CHOOSES PAPER, THEN
# PLAYER 1 WINS
#
# ELSE IF PLAYER 1 AND PLAYER 2 CHOOSES THE SAME OBJECT, THEN
# IT'S A TIE
#
# OTHERWISE, PLAYER 2 WINS

if choice == 2 and computer_choice == 1:
    print("player one wins")
elif choice == 1 and computer_choice == 0:
    print("player one wins")
elif choice == 0 and computer_choice == 2:
    print("player one wins")
elif choice == computer_choice:
    print("tie")
else:
    print("player two wins")
# PRINT THE WINNER AND THEIR CHOICE

print(f"player one picked {choice} ")

###############
### THE END ###
###############


