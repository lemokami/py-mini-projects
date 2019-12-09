import random,os
print("""
-----Roll the Dice-----
Instructions:: 
press [Enter] to roll again
Enter '0' to exit the program\n""")
o = int(input("What OS are you using\n1.WIN\t2.OS-X\LINUX\n>>"))
while(1):
    if(o==1):
        os.system('cls')
    else:
        os.system('clear')
    
    print(f"--\n|{random.randint(1,6)}|\n--")
    
    try:
        y=int(input("Roll Again[Enter] or Quit[0]:>"))
        break
    except:continue
    