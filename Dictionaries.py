_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)


capitals = dict()
capitals={"Costa Rica": "San Jose","Puerto Rico": "San Juan"}
print(capitals)
answer =capitals["Costa Rica"]
print(answer)

#dictionary keys must be immuttable, that is why Tuples can be dictionary keys but not Lists
# key , Value
# you can check if there is a kew in a dictionary but not a value
print("Costa Rica" in capitals)
print("Costa Rica" not in capitals)

#delete a key value pair
del capitals ["Costa Rica"]
print(capitals)

rhymes = {"1": "fun","2": "blue","3": "me","4": "floor","5": "live",}
n= input("Type a number between 1 and 5:")

if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found")


'''
1. Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.

2. Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary you created in challenge 1.


'''

aboutme ={"hieght": "5.7","favorite color": "blue","favorite author": "Garcia Marquez"}
print(aboutme)

q1 =input("Please, ask about my height?")

answer =aboutme["hieght"]
print ("I am ",answer," feet tall")

q2 =input("Please, ask about my favorite color? ")

answer =aboutme["favorite color"]
print ("My favorite color is ",answer)


q3 =input("Pelase, ask about my  favorite author? ")
answer =aboutme["favorite author"]
print ("My favorite author is ",answer)

#3. Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.

MyFavMus={"Cat Stevens": "Wild world","Stevie Wonder": "I just called to say","Joan Manuel Serrat": "Pueblo blanco"}

print("My favorite music by author and favorite song are: ")

answer = MyFavMus["Cat Stevens"]
print("1.Cat Stevens with the song '",answer,"'")
answer = MyFavMus["Stevie Wonder"]
print("2.Stevie Wonder with the song '",answer,"'")
answer = MyFavMus["Joan Manuel Serrat"]
print("3.Joan Manuel Serrat with the song '",answer,"'")