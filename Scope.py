_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

x = datetime.datetime.now()
print("File created", x)


x=2
y=3
z=8

def f():
    global y
    y += 1
    global x
    global z

    print(x)
    print(y)
    print(z)

f()

x=200
if x > 100:
    print("x is > 100")