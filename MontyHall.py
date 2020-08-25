import random

ans = random.randint(1, 3)
choice = random.randint(1, 3)
print("You have chosen door %d" % choice)
opendoor = 0
change = random.randint(1, 2)
for x in range(1, 3):
    if x != ans and x != choice:
        print("%d does not have the prize. Do you want to change your choice?" % x)
        opendoor = x
        break
        
if change == 2:
    for x in range(1, 3):
        if x != opendoor and x != choice:
            choice = x
            print("You have changed your door to door %d" % choice)
            break
else:
    print("You have not changed your choice.")
 
if choice == ans:
    print("We have a winner!")
else:
    print("The prize was in door %d. Better luck next time!" % ans)
