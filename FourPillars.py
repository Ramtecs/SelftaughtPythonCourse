
'''

1. Create Rectangle and Square classes with a method called calculate_perimeter that calculates the perimeter
of the shapes they represent. Create Rectangle and Square objects and call the method on both of them.

'''

#1

class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def perimeter(self):
        return  (self.width * self.length ) * 2



class Square():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def perimeter(self):
        return  (self.width * self.length ) * 2



rectangle = Rectangle(2,4)

print("The perimeter  for the rectangle is: ",rectangle.perimeter())


square = Square(4,4)

print("The perimeter for the square is: ",square.perimeter())







'''
2. Define a method in your Square class called change_size that allows you to pass in a number that increases or decreases
(if the number is negative) each side of a Square object by that number.
'''

class Square():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def perimeter(self):
        return  (self.width * self.length ) * 2

    def change_size(self, l, w):
        self.length = l
        self.width = w

square = Square(4,4)
print("The perimeter for the square is: ",square.perimeter())


square.change_size(5,5)
print("The increased perimeter for the square is: ",square.perimeter())

square.change_size(2,2)
print("The reduced perimeter for the square is: ",square.perimeter())

'''
3. Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called.
Change your Square and Rectangle classes from the previous challenges to inherit from Shape,
create Square and Rectangle objects, and call the new method on both of them.
'''


class Shape():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def what_am_I(self):
        if (self.width == self.length) :
           print("I am a Square ")
        else:
           print("I am a a rectangle ")

thisshape = Shape(2,4)
thisshape.what_am_I()

thisshape = Shape(4,4)
thisshape.what_am_I()


'''
output:

C:\Users\code\AppData\Local\Programs\Python\Python37\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/Files/FourPillars.py
The perimeter  for the rectangle is:  16
The perimeter for the square is:  32
The perimeter for the square is:  32
The increased perimeter for the square is:  50
The reduced perimeter for the square is:  8
I am a a rectangle 
I am a Square 
'''
