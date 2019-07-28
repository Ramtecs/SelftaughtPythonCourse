_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''

#   Declare Integer x
#
#   For x = 0 to 10
#       Display x
#   End For
#
#   Display "Goodbye"

for x in range(0,11):
    print(x)

print("Goodbye")

#------------------------------
print("----------------------")

#   Declare Integer x
#
#   For x = 10 to 1 Step -1
#       Display x
#   End For
#
#   Display "Blast off!"

for x in range(10, 0, -1):
    print(x)

print("Blast off!")

#------------------------------
print("----------------------")

#   Declare Integer x
#
#   Display "Even numbers between 2 and 20:"
#   For x = 2 to 20 Step 2
#       Display x
#   End For
#
#   Display "Goodbye"

print("Even numbers between 2 and 20:")
for x in range(2, 21, 2):
    print(x)

print("Goodbye")

#------------------------------
print("----------------------")

#   Declare num_times = 3
#
#   For x = 1 to num_times
#       Display "Go Team!"
#   End For

# Execute a loop a specified number of times
# (The counter goes from 0 to num_times-1)
num_times = 3

for x in range(num_times):
    print("Go Team!")