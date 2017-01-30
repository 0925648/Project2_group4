import random

number = random.randint(1,6)
print("This is a dice rolling program!")
print("Press enter to roll")
input()
x = 1
y = 1
''' 
een = (x == 5 and y == 5)
twee = (y == 4 and x == 4 or y == 6 and x == 6)
drie = (y == 3 and x == 3 or y == 5 and x == 5 or y == 7 and x == 7)
vier = (y == 3 and x == 3 or y == 3 and x == 7 or y == 7 and x == 3 or y == 7 and x == 7)
vijf = (y == 3 and x == 3 or y == 3 and x == 7 or y == 7 and x == 3 or y == 7 and x == 7 or y == 5 and x == 5)
zes = (y == 3 and x == 3 or y == 5 and x == 3 or y == 7 and x == 3 or y == 3 and x == 7 or y == 5 and x == 7 or y == 7 and x == 7)

def dice(numberofdots):
    global x
    global y 
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif numberofdots:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")
'''
if number == 1:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif x == 5 and y == 5:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")

if number == 2:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif y == 4 and x == 4 or y == 6 and x == 6:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")
        
if number == 3:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif y == 3 and x == 3 or y == 5 and x == 5 or y == 7 and x == 7:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")

#Derek Banas - C#
if number == 4:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif y == 3 and x == 3 or y == 3 and x == 7 or y == 7 and x == 3 or y == 7 and x == 7:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")

if number == 5:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif y == 3 and x == 3 or y == 3 and x == 7 or y == 7 and x == 3 or y == 7 and x == 7 or y == 5 and x == 5:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")

if number == 6:
    y = 1
    while y <= 9:
        x = 1
        while x <= 9:
            if y == 1 or y == 9 or x == 1 or x == 9:
                print("x", end=" ")
            elif y == 3 and x == 3 or y == 5 and x == 3 or y == 7 and x == 3 or y == 3 and x == 7 or y == 5 and x == 7 or y == 7 and x == 7:
                print("x", end=" ")
            else:
                print(" ", end=" ")
            x = x + 1
        y = y + 1
        print("")

    



