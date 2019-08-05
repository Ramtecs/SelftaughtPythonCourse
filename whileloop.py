_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)

'''
while loop
continue 
break
nested loops

x=10
while x>0:
    print('{}'.format(x))
    x -= 1
    print("Happy New Year")


#example 2
for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)

#example 3
list1 =[1,2,3,4]
list2 =[5,6,7,8]
added =[]
for i in list1:
    for j in list2:
        added.append(i+j)
        print(added)

#example 4

while input('y or n')!="n":
    for i in range(1,6):
               print(i)
               
               
#1. Write a program with an infinite loop (with the option to type q to quit) and a list of numbers. 
# Each time through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly.

#2. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83], and append each result to a third list.

'''
#1
numbers2guess = [4, 3, 7, 9, 1,11,8,5]

while True:
    response = input("Enter e number between 1 and 11 or type q to quit.")
    if response == "q":
        print("You have chosen to quit, thanks for playing... good bye!")
        break
    try:
        response = int(response)
    except ValueError:
        print("please type a number or q to quit.")
    if (response > 11) or (response < 1):
        print("Number out of bound! it must be between 1 and 11.")
    else:
        if response in numbers2guess:
            print(response,'Exists in the list so you quessed correctly.')
        else:
            print("You guessed incorrectly; that number is not in the list!")



#2
listA =[8, 19, 148, 4]
listB =[9, 1, 33, 83]
Multiplied =[]


for i in listA:
    for j in listB:
        Multiplied.append(i*j)
        print(Multiplied)


number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      pass    # pass here

   print('Number is ' + str(number))

print('Out of loop')


'''
output:
C:\Users\xxxx\PycharmProjects\SelftaughtPythonCourse\venv\Scripts\python.exe C:/Users/xxxx/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/WhileLoops.py
File run 2019-08-04 17:16:04.924186
Enter e number between 1 and 11 or type q to quit.2
You guessed incorrectly; that number is not in the list!
Enter e number between 1 and 11 or type q to quit.4
4 Exists in the list so you quessed correctly.
Enter e number between 1 and 11 or type q to quit.7
7 Exists in the list so you quessed correctly.
Enter e number between 1 and 11 or type q to quit.2
You guessed incorrectly; that number is not in the list!
Enter e number between 1 and 11 or type q to quit.12
Number out of bound! it must be between 1 and 11.
Enter e number between 1 and 11 or type q to quit.0
Number out of bound! it must be between 1 and 11.
Enter e number between 1 and 11 or type q to quit.q
You have chosen to quit, thanks for playing... good bye!
[72]
[72, 8]
[72, 8, 264]
[72, 8, 264, 664]
[72, 8, 264, 664, 171]
[72, 8, 264, 664, 171, 19]
[72, 8, 264, 664, 171, 19, 627]
[72, 8, 264, 664, 171, 19, 627, 1577]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284, 36]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284, 36, 4]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284, 36, 4, 132]
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284, 36, 4, 132, 332]
Number is 1
Number is 2
Number is 3
Number is 4
Number is 5
Number is 6
Number is 7
Number is 8
Number is 9
Number is 10
Out of loop

Process finished with exit code 0
'''
