
USER= 0
RAND=0
from random import *

list = ("R", "P", "S")
while True:
    user = input("R,P,S")
    rand = choice(list)
    print(rand)
    if user == "R" and rand == "P":
        print("you lose")
        RAND+=1
    if user == "P" and rand == "S":
        print("you lose")
        RAND +=1
    if user == "S" and rand == "R":
        print("you lose")
        RAND +=1
    if user == "P" and rand == "R":
         print("you win ")
         USER +=1
    if user == "S" and rand == "P":
         print("you win")
         USER +=1
    if user == "R" and rand == "S":
         print("you win")
         USER +=1
    if user == "S" and rand == "S":
        print("TIE")
    if user == "P" and rand == "P":
        print("TIE")
    if user == "R" and rand == "R":
        print("TIE");

    print("бали енемі",RAND)
    print("Твої бали",USER)
