import random

rand = random.randint(10,200)
a = 1
while True:
    user_num = int (input("Guess my number [0,200]"))  
    if rand == user_num:
        print ("***Ahsant***")
        break
    elif rand < user_num:
        print ("Bia paeein⬇")
    elif rand > user_num:
        print ("Boro Bala")
    a+=1
print ("You tried ",a," Times, Try again later")

