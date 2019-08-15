
_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)
'''

insert the random function
then capitalize all the words to avoid isues with casing
do the same thing for the input so that thae casing match in the letters
'''
import random
Wordlist =["Cat","Mouse", "dog"]
word =random.choice(Wordlist)
word = word.upper()
#print(word)

#1. Modify the game, so a word is selected randomly from a list of words.
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        char = char.upper()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman(word)

'''
output:

C:\Users\code\PycharmProjects\SelftaughtPythonCourse\venv\Scripts\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/Files/hangman.py
File run 2019-08-14 22:17:05.204081
Welcome to Hangman


Guess a letterd
__ __ __ __ __

________        


Guess a letterd
__ __ __ __ __

________        
|               


Guess a letterd
__ __ __ __ __

________        
|               
|        |      


Guess a letterm
M __ __ __ __

________        
|               
|        |      


Guess a lettero
M O __ __ __

________        
|               
|        |      


Guess a letteru
M O U __ __

________        
|               
|        |      


Guess a letters
M O U S __

________        
|               
|        |      


Guess a lettere
M O U S E

________        
|               
|        |      
You win!
M O U S E

Process finished with exit code 0
'''
