_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)
'''

Rock paper scissors game:
Author:  Ramses Murillo
Stored the words in Wordlist[]
then selected random word using the random function
Created an index from 1-4 for the user to select the choices so I dont have to deal with casing
Choice 4 is to exit
If the selection is 0 or higher than 4 then the program tells the user it is outbound and must try again
If the game does not exit because the choices are in the right range of choices then  the user will get a stats table at the end
If the matches are greater than the wins by the computer and the user, then the random gods won the game unapologetically!
'''

import random
Wordlist =["Rock","Paper", "Scissors"]
#Wordlist =["Rock"]
word =random.choice(Wordlist)
#word = word.upper()
count =0
computerwins =0
userwins =0
nobodywins =0
print('\n\n')
print('Welcome you are in round',count +1)
print('\n\n')
print('Enter 1 for Rock. \nEnter 2 for Paper. \nEnter 3 for Scisors. \nEnter 4 to exit.')
choice = int(input('\nEnter your choice:'))
print('\n')

word = random.choice(Wordlist)  # so the random word is not the same
if (choice > 4) or (choice == 0):
    print("Select only numbers between 1 and 4, please try again!")
    exit()
if (choice == 4):
    print("your have chosen to quit,good bye!")
    exit()
else:
    print("your word choice was: ", Wordlist[choice - 1])
    print("The computer's word choice was: ", word)
    print('\n\n')

#the first round of executing code goes here
if (choice == 1 and word == "Rock"):
    print("Rock, paper, scisosrs...Rock and Rock... Nobody wins!")
    nobodywins = nobodywins + 1
if (choice == 1 and word == "Paper"):
    print("Rock, paper, scisosrs..Paper warps Rock... Computer wins!")
    computerwins = computerwins + 1
if (choice == 1 and word == "Scissors"):
    print("Rock, paper, scisosrs..Rock smashes Scissors... you win!")
    userwins = userwins + 1
if (choice == 2 and word == "Rock"):
    print("Rock, paper, scisosrs...Paper wraps Rock... You win!")
    userwins = userwins + 1
if (choice == 2 and word == "Paper"):
    print("Rock, paper, scisosrs..Paper and Paper... Nobody wins!")
    nobodywins = nobodywins + 1
if (choice == 2 and word == "Scissors"):
    print("Rock, paper, scisosrs..Scissors cut Paper... Computer Wins!")
    computerwins = computerwins + 1
if (choice == 3 and word == "Rock"):
    print("Rock, paper, scisosrs...Rock smaches Scissors... Computer wins!")
    computerwins = computerwins + 1
if (choice == 3 and word == "Paper"):
    print("Rock, paper, scisosrs..Scissors cuts Paper... You win!")
    userwins = userwins + 1
if (choice == 3 and word == "Scissors"):
    print("Rock, paper, scisosrs..Scissors and Scissors... Nobody wins!")
    nobodywins = nobodywins + 1


#code goes here for first time

while ((choice > 0) and (choice < 4)):


    count=count +1

    print('You are in round',count+1)
    print('\n\n')
    print('Enter 1 for Rock, \nEnter 2 for Paper. \nEnter 3 for Scisors. \nEnter 4 to exit.')
    print('\n\n')
    choice = int(input('\nEnter your choice for this round: '))
    print('\n')
    word = random.choice(Wordlist)  # so the random word is not the same
    if (choice > 4) or (choice == 0):
        print("Select only numbers between 1 and 4, please try again!")
        exit()
    if (choice == 4):
        print("your have chosen to quit,good bye!")
        break
    else:
        print("your word choice was: ", Wordlist[choice-1])
        print("The computer's word choice was: ", word)
        print('\n\n')

        #executing code goes here
        if (choice == 1 and word == "Rock"):
            print("Rock, paper, scisosrs...Rock and Rock... Nobody wins!")
            nobodywins = nobodywins + 1
        if (choice == 1 and word == "Paper"):
            print("Rock, paper, scisosrs..Paper warps Rock... Computer wins!")
            computerwins = computerwins + 1
        if (choice == 1 and word == "Scissors"):
            print("Rock, paper, scisosrs..Rock smashes Scissors... you win!")
            userwins = userwins + 1
        if (choice == 2 and word == "Rock"):
            print("Rock, paper, scisosrs...Paper wraps Rock... You win!")
            userwins = userwins + 1
        if (choice == 2 and word == "Paper"):
            print("Rock, paper, scisosrs..Paper and Paper... Nobody wins!")
            nobodywins = nobodywins + 1
        if (choice == 2 and word == "Scissors"):
            print("Rock, paper, scisosrs..Scissors cut Paper... Computer Wins!")
            computerwins = computerwins + 1
        if (choice == 3 and word == "Rock"):
            print("Rock, paper, scisosrs...Rock smaches Scissors... Computer wins!")
            computerwins = computerwins + 1
        if (choice == 3 and word == "Paper"):
            print("Rock, paper, scisosrs..Scissors cuts Paper... You win!")
            userwins = userwins + 1
        if (choice == 3 and word == "Scissors"):
            print("Rock, paper, scisosrs..Scissors and Scissors... Nobody wins!")
            nobodywins = nobodywins + 1


'''
    #code after the first time the loop runs





    if count >0:
        word = random.choice(Wordlist) # so the random word is not the same
        print('Round:',count)
        print('Enter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scisors. \nEnter 4 to exit 4.')
        choice = int(input('\nEnter your choice:'))
        print("your word choice was: ", Wordlist[choice-1])
        print("The computer's word choice was: ", word)
'''
print("\n\n\n\n\n")

print("############################STATS#################################")
print("Here are the stats for your game:")
print("Even Matches: ",nobodywins)
print("user won:",userwins," times")
print("Computer won:",computerwins," times")
print("Rounds played: ",count)

if (computerwins > userwins and  computerwins > nobodywins):
    print("########### The computer won the game!#############")

if (computerwins < userwins and  userwins > nobodywins):
    print("########### The user  won the game!#############")

if (nobodywins > userwins and nobodywins > computerwins):
    print("########### The random gods won! #############")


'''
############################STATS#################################
Here are the stats for your game:
Even Matches:  4
user won: 10  times
Computer won: 2  times
Rounds played:  16
########### The user  won the game!#############

############################STATS#################################
Here are the stats for your game:
Even Matches:  7
user won: 3  times
Computer won: 6  times
Rounds played:  16
########### The random gods won! #############

############################STATS#################################
Here are the stats for your game:
Even Matches:  3
user won: 2  times
Computer won: 5  times
Rounds played:  10
########### The computer won the game!#############

'''
