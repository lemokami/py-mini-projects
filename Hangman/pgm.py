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

with open("Hangman/words.txt") as f:
    wordlist = [x[:-1] for x in f if len(x)>=2]

word = wordlist[random.randint(0,len(wordlist))].lower()

print(f"""I Guessed a word. What is it?
It has {len(word)} letters.
Guess it before your choices make him the
H A N G M A N""")

wordg = ['_' for i in range(len(word))]

hangman = ["|","0","/","|","\\","/","\\"]
space = "55440"
while(1):
    print("___________")
    for i in range(5):
        print(f"|{' '*int(space[i])}|")
    print("-----------")

    print(word)
    
    for i in wordg:
        print(f"{i} ",end='')
    
    if "_" not in wordg:
        print()
        break
    
    gus = input("\nGuess a letter:>")
    
    for i in range(len(word)):
        if(gus.lower() == word[i]):
            wordg[i] = gus
    

    
    os.system(fn)
    
        


# This is how a hangman looks like
# ___________
# |     |
# |     0
# |    /|\\
# |    / \   
# |
# -----------