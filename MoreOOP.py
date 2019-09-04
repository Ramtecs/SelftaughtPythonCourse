'''
1. Add a square_list class variable to a class called Square so that every time you create a new Square object, the new object gets added to the list.


3. Write a function that takes two objects as parameters and returns True if they are the same object, and False if not.
'''
#1
class Square():

    square_list= []

    def __init__(self, w, l):
            self.width = w
            self.len = l
            self.square_list.append((self.width, self.len))

    def print_size(self):
            print("""{} by {}""".format(self.width, self.len))
print("Number 1:")
square1 = Square(10,10)
square2 = Square(5,5)
square3 = Square(20,20)
print(Square.square_list)

#2. Change the Square class so that when you print a Square object, a message prints telling you the len of each of the four sides of the shape.
# For example, if you create a square with Square(29) and print it, Python should print 29 by 29 by 29 by 29.

class Square():

    def __init__(self, l):
        self.len = l

    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.len, self.len, self.len, self.len))
square1=Square(29)

print("Number 2:")
print(square1.print_size())



#3. Write a function that takes two objects as parameters and returns True if they are the same object, and False if not.

class Sphere:
    def __init__(self, Object1, Object2):
        self.type1 = Object1
        self.type2 = Object2
    def compare_sphere(self):
        if(self.type1 == self.type2):
         #print("They are the same")
         print("""{} is the same as {}""".format(self.type1, self.type2))
        else:
         #print ("They are not the same")
         print("""{} is not the same as {}""".format(self.type1, self.type2))


print("Number 3:")
#sphereinstance =Sphere('baseball', 'football')
sphereinstance =Sphere('baseball', 'baseball')
print(sphereinstance.compare_sphere())
sphereinstance =Sphere('baseball', 'basketball')
print(sphereinstance.compare_sphere())


'''
output:
C:\Users\code\AppData\Local\Programs\Python\Python37\python.exe C:/Users/code/PycharmProjects/SelftaughtPythonCourse/SelftaughtPythonCourse/Files/MoreOOPs.py
Number 1:
[(10, 10), (5, 5), (20, 20)]
Number 2:
29 by 29 by 29 by 29
None
Number 3:
baseball is the same as baseball
None
baseball is not the same as basketball
None

Process finished with exit code 0



'''
