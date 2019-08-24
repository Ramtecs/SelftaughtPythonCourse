#Author:  Ramses O'Murillo  Date:8-23-19
import random
print('Enter 1 for Rock. \nEnter 2 for Paper. \nEnter 3 for Scisors. \nEnter 4 to exit.')
choice = int(input('\nEnter your choice:'))

while ((choice > 0) and (choice < 4)):
    print('Enter 1 for Rock. \nEnter 2 for Paper. \nEnter 3 for Scisors. \nEnter 4 to exit.')
    choice = int(input('\nEnter your choice:'))

    Wordlist = ["Rock", "Paper", "Scissors"]
    word = random.choice(Wordlist)

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
  #executing code goes here
    if (choice == 1 and word == "Paper") or (choice == 3 and word == "Rock") or (choice == 2 and word == "Scissors"):
        print("Computer wins!")
    if (choice == 1 and word == "Scissors") or (choice == 2 and word == "Rock") or (choice == 3 and word == "paper"):
        print("You win!")
    if (choice == 3 and word == "Scissors") or (choice == 2 and word == "Paper") or (choice == 1 and word == "Rock"):
        print("Nobody wins!")

