# QUESTION : make a game like rock paper scissors 

import random
options = [0,1,2]

def get_random_integer():  #random function
    """this is a random function which is return every time a integer that is either 0/1/2 """
    return random.choice(options)

def getName(choice):    # for better viewing 
    """it takes a number which is one of 0/1/2  and return 
    if given choice is 0 then return 'rock' 
    elif given choice is 1 then return 'paper'
    else given choiec is 2 then return 'scissors'  """
    for i in range(3):  
                if(choice  == 0):
                   return "rock"
                elif (choice == 1):
                   return "paper"
                else:
                    return "scissors"

drow = 0                   #drows count
win = 0                    #wins count
lost = 0                   #lose count
player_choice = ""         #only for best looking
computer_choice = ""       #only for best looking

while True:
    print("\n0. rock \n1. paper \n2. scissors  \n3. end the game \n\nenter options : ", end = "")
    try:
        player = int(input())  #user input

        if player == 3:  # if user input is 3 then break the loop to end the game
            break
        
        if player > 3 or player < 0:  # if user input invalid inputs (other than 0, 1, 2, 3) then skip this iteration
            print("ops, enter only (0, 1, 2, 3)")
            continue

        computer = get_random_integer()  # taking computer input randomly

        #logic
        """
                                computer input (col)
                                    r  p   s
                                    0  1   2
        user input (row)    r   0   D  L   W
                            p   1   W  D   L
                            s   2   L  W   D

        """
        if(player == computer):  
            drow += 1
        elif (( player == 0 and computer == 2) or (player == 1 and computer == 0 ) or (player == 2 and computer == 1) ):
            win += 1
        else :
            lost += 1

        player_choice = getName(player)
        computer_choice = getName(computer)

        print(f"\nyour choice : {player_choice}   <-->   computer's choice : {computer_choice}")
        print(f"\nwins : {win}  : drows : {drow}    : losts : {lost}")
    except :
        print("enter only (0, 1, 2, 3)")

print(f"\nfinal score \nwins : {win}  \ndrows : {drow}    \nlosts : {lost}\n\n_________________________________________________________________ thank you ________________________________________________________________\n")