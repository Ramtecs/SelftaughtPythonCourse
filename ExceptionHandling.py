_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

x = datetime.datetime.now()
print("File created", x)

'''Write a program that asks the user to type a number, convert it to an integer, and print it. If you can't convert their input to an integer, print a message that says "Please type an integer."'''


a=input("enter a number for variable 'a': ")

try:
    a=int(a)

except ValueError:
   print("Error in data type, input for 'a' can only be numbers!")

else:
    print( a,"The was converted to integer" )

