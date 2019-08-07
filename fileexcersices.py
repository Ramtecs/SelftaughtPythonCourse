_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())

import datetime

#example1
todaysdate = datetime.datetime.now()
print("File run", todaysdate)
st =open("st.txt","w")
st.write("hello everyone!")
st.close()


import os
os.patj.join("users","bob","st.txt")
"r"  #read
"w"  #write
"w+"  #read and write


with open([file_path],[ mode]) as [variable_name]:
    [your code]
with open("st.txt", "w") as f:
     f.write("hi from python!")


with open("c:\\users\\paven....st.txt","r") as f:
     print(f.read())


my_list = list()
with open("Path","r") as f
     my_list.append(f.read())
print(my_list)




#1. Find a file on your computer and print its contents using Python.
'''
#filename ="C:\Users\code\Documents\python.txt"
filename ="ingredients.txt"

with open(filename,'r') as filex:
    x=filex.read()
    print(x)

#2. Write a program that asks a user a question, and saves their answer to a file.
response =input("Express yourself and write a sentence")
filename ="st.txt"
with open(filename,'w') as filex1:
    print(response,file=filex1)

filename = "st.txt"

with open(filename, 'r') as filex1:
    x = filex1.read()
    print(x)

'''
output:

C:\Users\xxx\PycharmProjects\SelftaughtPythonCourse\venv\Scripts\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/Files/FileExcersices.py
onions
garlic
tomatoes
etc
Express yourself and write a sentenceLife is good regarless of politics, I assure you!
Life is good regarless of politics, I assure you!


Process finished with exit code 0
'''

