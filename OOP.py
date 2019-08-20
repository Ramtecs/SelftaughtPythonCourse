_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)

'''
1. Define a class called Apple with four instance variables that represent four attributes of an apple.

attributes: red, weight, type
'''
class Apple():
    def __init__(self, w, t, c, st):
        self.weight = w
        self.type = t
        self.color = c
        self.state_of_procedence = st

        print("List of Apples and features:")



apple = Apple("10","red delicious","Red","WA")
print(apple.color, apple.weight, apple.type,apple.state_of_procedence)
'''
2. Create a Circle class with a method called area that calculates and returns its area. Then create a Circle object,
call area on it, and print the result. Use Python's pi function in the built-in math module.
Area = 2pir**2
'''


import math
class Circle():
    def __init__(self,r):
        self.width = r

    def area(self):
        return math.pi * self.width**2


circle = Circle(8)

print("The area (2Pi R^2) of the circle is: ",circle.area())


'''
3. Create a Triangle class with a method called area that calculates and returns its area. Then create a Triangle object,
call area on it, and print the result.

'''
class Triangle():
    def __init__(self,h,b):
        self.height = h
        self.base = b

    def area(self):
        return  (self.base * self.height )/2


triangle = Triangle(8,4)

print("The area (b*h/2 ) of the circle is: ",triangle.area())



'''
4. Make a Hexagon class with a method called calculate_perimeter that calculates and returns its perimeter.
Then create a Hexagon object, call calculate_perimeter on it, and print the result.
'''

_author_ = 'Ramses Murillo'

class Hexagon:
    def __init__(self, length=0):

        self.length = length

    def perimeter(self):
        return self.length * 6



a = Hexagon(6) #create an instance
print("The perimeter  of a hexagon of 6 inches per side is " ,a.perimeter())#call the properties of the instance


#################output############################


'''
File run 2019-08-19 23:28:00.915923
List of Apples and features:
Red 10 red delicious WA
The area (2Pi R^2) of the circle is:  201.06192982974676
The area (b*h/2 ) of the circle is:  16.0
The perimeter  of a hexagon of 6 inches per side is  36
'''
