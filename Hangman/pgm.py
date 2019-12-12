import random
print("""----WELCOME TO HANGMAN----
Instructions:
1.The computer guesses a word from the words text
2.You will get the chances till the man dies
""")

with open("Hangman/words.txt") as f:
    wordlist = [x[:-1] for x in f]

print(wordlist[random.randint(0,len(wordlist))])