_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)
'''
lesson summary:
print('she said "it was ok."')
print("today is today\ntomorrow is tomorrow")

#slice method
StringName ="Ramses Jimenez"
x=StringName[0:4]
print(x)
StringName ="Ramses Jimenez"
x=StringName[:]
print(x)
StringName ="Ramses Jimenez"
x=StringName[7:14]
print(x)
StringName ="Ramses Jimenez"
x=StringName[7:]
print(x)
StringName ="Ramses Jimenez"
x=StringName[:7]
print(x)
print('Ramses'.index('m'))
1.Find dialogue in your favorite book (containing quotes) and turn it into a string.
2.Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the characters before the comma
3.Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammatically correct string. There should be a space 
between each word, but no space between the word fence and the period that follows it. (Don't forget, you learned a method that
 turns a list of strings into a single string.)
'''

#1:
Hemingway ='"There is nothing noble in being superior to your fellow man;\ntrue nobility is being superior to your former self."'
print(Hemingway)
#2"It was a bright cold day in April, and the clocks were striking thirteen."
x="It was a bright cold day in April, and the clocks were striking thirteen."
print(x[0:33])
#3
words=["The", "fox", "jumped", "over", "the", "fence", "."]
seperator = ','
words =seperator.join(words)
words=words.replace(","," ")
words=words.replace(" .",".")
print(words)

''''
output:
C:\Users\\\\PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/StringsII.py
File run 2019-08-02 23:00:56.472432
"There is nothing noble in being superior to your fellow man;
true nobility is being superior to your former self."
It was a bright cold day in April
The fox jumped over the fence.

Process finished with exit code 0
'''
