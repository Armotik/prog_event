import os
import time
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


symbols = ["#", "?", "~", "$"]  # The symbols on the reels

user = ""
random.seed()
test = int(4 * random.random())

while (user != "exit"):

    a=""
    b=""
    c=""

    for i in range (0,20):
        # take care, sleep needs an argument in seconds, not millis
        time.sleep( (50 + 25 * i)/1000)   # slow down while the loop runs

        c = symbols[random.randint(0, 3)]
        if( i < 10 ):
            a = symbols[random.randint(0, 3)]
        if( i < 15 ):
            b = symbols[random.randint(0, 3)]
        cls()
        print( "Spin: " + a + b + c )
    
    if((a == b) and (b == c)) :
        user = input("You win the jackpot. Press enter to play again or type \"exit\" to exit")    

    # le test ternaire condition ? a : b s'ecrit en pyhton a if condition else b
    elif (((1 if (a == "$") else 0) + (1 if (b == "$") else 0) + (1 if (c == "$") else 0)) == 2) :  # check if at least two $
    	user = input("You win. Press enter to play again or type \"exit\" to exit")    
    else :
        user = input("You lose. Press enter to play again or type \"exit\" to exit")        


