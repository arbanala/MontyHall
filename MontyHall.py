import random

ans = random.randint(1, 3)
choice = random.randint(1, 3)
opendoor = 0
change = random.randint(1, 2)
for x in range(1, 3):
    if x != ans & x != choice
        print("%d does not have the prize. Do you want to change your choice?", x)
        opendoor = x
        break
        
if change == 2
    for x in range(1, 3):
        if x != opendoor & x != choice
            choice = x
            break
 
if choice == ans
    print("We have a winner!")
else
    print("We don't have a winner. Better luck next time!")
