import random
print("I will play Snake, Water, Gun with you stay ready👋")
u=input("enter your choice:")
c=random.choice(["snake","water","gun"])
print(c)
y=u.lower()
if (c==y):
    print("its a tie")
elif (c=="snake" and y=="gun") or (c=="water" and y=="snake") or (c=="gun" and y=="water"):
    print("you won")
else:
    print("Computer wins")