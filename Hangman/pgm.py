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

word = wordlist[random.randint(0,len(wordlist))]

print(f"""I Guessed a word. What is it?
It has {len(word)} letters.
Guess it before your choices make him the
H A N G M A N
{'_ '*len(word)}""")

print(word)

# This is how a hangman looks like
# ___________
# |     |
# |     0
# |    /|\\
# |    / \   
# |
# -----------