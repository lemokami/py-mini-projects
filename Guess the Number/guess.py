import random

print("""Guess the Number
Instructions:
1.The computer guesses a number b/w 1 to 100
2.You have only 30 chances
3.Enter q to quit

---Best of Luck---""")

chnce=30
num = random.randint(1,100)

print("I Guessed a Number,",end='')

while(chnce):
    try:
        gus = int(input("Enter:>"))
    except:break
    chnce-=1
    if(gus==num):
        print("Wonderful Job")
        break
    print(f"You have {chnce} chances to go\n")
if(chnce==0):
    print(f"Number was {num}")