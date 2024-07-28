from random import randint
r=randint(1,5)
t=0
while(1): 
    print("Guess a number: from 1 to 5:")
    a=int(input('enter your number:'))
    if(a<r):
        t=t+1
        print("guess something higher")
    elif(a>r):
        t=t+1
        print("guess something lower") 
    else:
        t=t+1
        print(f"your guess is correct,number is {r} your guess is correct in {t} attempt")
        break
