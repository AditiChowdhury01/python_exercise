import random                                  
int_num,guess_num = random.randint(1,10),0
while int_num!=guess_num:
    guess_num = int(input("enter the right num until you get it right"))

print("you guessed it right")