import random,os

ch = int(input("Whats your OS\n1.WIN\t2.LINUX\n:>"))

if(ch==1):
    fn="cls"
else:
    fn="clear"

os.system(fn)    

print("""----WELCOME TO HANGMAN----
Instructions:
1.The computer guesses a word from the words text
2.You will get the chances till the man dies
""")

input()

os.system(fn)
if (os.path.exists("Hangman/words.txt")):
    pth = "Hangman/words.txt"
else:
    pth = "words.txt"
    
with open(pth,"r") as f:
    wordlist = [x[:-1] for x in f if len(x)>=2]

word = wordlist[random.randint(0,len(wordlist))].lower()

print(f"""I Guessed a word. What is it?
It has {len(word)} letters.
Guess it before your choices make him the
H A N G M A N""")

wordg = ['_' for i in range(len(word))]

hangman = ["|","0","/","|","\\","/","\\"]

man = ['' for i in range(7)]

ind = 0

while(1):
    correct = 0
    print(f"""___________
|     {man[0]}
|     {man[1]}
|    {man[2]}{man[3]}{man[4]}
|    {man[5]} {man[6]}   
|
-----------""")

    if(ind!=7):
        
        for i in wordg:
            print(f"{i} ",end='')
        
        if "_" not in wordg:
            print()
            break
        
        gus = input("\nGuess a letter:>")
        
        for i in range(len(word)):
            if(gus.lower() == word[i]):
                correct = 1
                wordg[i] = gus
                
    else:
        print(f"The word was {word}")
        print("YOU ARE HANGED")
        break
    if(not correct):
        man[ind] = hangman[ind]
        ind+=1

    

    
    os.system(fn)
    
        


# This is how a hangman looks like
# ___________
# |     |
# |     0
# |    /|\\
# |    / \   
# |
# -----------