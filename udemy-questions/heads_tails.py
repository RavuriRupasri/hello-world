#Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

import random
n=int(input("Enter the range : "))
tails=0
heads=0
x=1 
while(x<=n):
    r=random.randint(0,1)
    if(r):
        print("Heads")
        heads=heads+1 
    else:
        print("Tales")
        tails=tails+1 
    x=x+1
print("Number of heads and tails are {},{} respectively".format(heads,tails))