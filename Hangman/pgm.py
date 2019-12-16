import random,os,json

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
if (os.path.exists("Hangman/words.json")):
    pth = "Hangman/words.json"
else:
    pth = "words.json"
    
with open(pth,"r") as fil:
    dictionary = json.loads(fil.read())
    word = random.choice(list(dictionary.keys()))
    meaning = dictionary[word]

print(f"""I Guessed a word. What is it?
It has {len(word)} letters.
Guess it before your choices make him dead""")

input()

os.system(fn)

wordg = ['_' for i in range(len(word))]

hangman = ["|","0","/","|","\\","/","\\"]

man = ['' for i in range(7)]
guslis = []
hman = "HANGMAN"
ind = 0

while(1):
    print(f"""
-----HINT-----
It has {len(word)} letters.
Meaning:{meaning}""")

    for i in range(ind):
        print(hman[i],end=" ")

    correct = 0
    print(f"""
___________
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
            print("\nCONGRATULATIONS!!!")
            break

        print("\nGuesses:",end='')
        for i in guslis:
            print(f"-> {i}",end='')
        

        gus = input("\nGuess a letter:>")
        
        guslis.append(gus)
        

        for i in range(len(word)):
            if(gus.lower() == word[i]):
                correct = 1
                wordg[i] = gus
                
    else:
        print("H A N G E D")
        print(f"The word was {word}")
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