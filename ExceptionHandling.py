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
    print( a," was converted to integer" )

'''output:
C:\Users\code\PycharmProjects\SelftaughtPythonCourse\venv\Scripts\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/ExceptionHandling.py
File created 2019-07-27 16:35:03.911052
enter a number for variable 'a': word
Error in data type, input for 'a' can only be numbers!

Process finished with exit code 0

output 2:

C:\Users\code\PycharmProjects\SelftaughtPythonCourse\venv\Scripts\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/ExceptionHandling.py
File created 2019-07-27 16:40:02.144858
enter a number for variable 'a': 232322
232322  was converted to integer

Process finished with exit code 0

'''
