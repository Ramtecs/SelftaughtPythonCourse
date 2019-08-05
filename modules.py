_author_ = 'Ramses Murillo'
'''import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
#1. Call a different function from the statistics module.

#2. Create a module named cubed with a function that takes a number as a parameter, and returns the number cubed.
# Import and call the function from another module.


#1
'''
The mean() method calculates the arithmetic mean of the numbers in a list.
The median() method returns the middle value of numeric data in a list.
The mode() method returns the most common data point in the list.
stdev() method calculates the standard deviation on a given sample in the form of a list.
'''


#1
print("n\Excercise 1:\n")
import module_cubed
x = input("Enter a number to get the volume of a cube")
x = int (x)
module_cubed.cubed(x)

print("\nExcercise 2:\n")
#2

numbers = [4, 3,4 ,7,19,4,18,11,8,5,3]
import statistics

print("The mean for the number list is: ",statistics.mean(numbers))
print("Which meann it calculates the arithmetic mean of the numbers in a list")

print("The mean for the number list is: ",statistics.median(numbers))
print("Which meann it calculates the middle value the numbers in a list")

print("The mean for the number list is: ",statistics.mode(numbers))
print("Which meann it calculates the most common value in the  numbers in a list")

print("The mean for the number list is: ",statistics.stdev(numbers))
print("Which meann it calculates the standad deviation numbers in a list")