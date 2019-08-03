_author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)

name = "ramses"
for letter in name:
    print(letter)


'''  
1. Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].

2. Print all the numbers from 25 to 50.

3. Print each item in the list from the first challenge and their indexes.
'''
#1
list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for item in list:
    print(item)

#2
for x in range(25,51):
    print(x)

#3
list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for item in list:
    x = list.index(item)
    print("index for: " +"'"+ item+"'",x)
    
    
    '''
    output:
    File run 2019-08-02 23:26:36.628918
r
a
m
s
e
s
The Walking Dead
Entourage
The Sopranos
The Vampire Diaries
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
index for: 'The Walking Dead' 0
index for: 'Entourage' 1
index for: 'The Sopranos' 2
index for: 'The Vampire Diaries' 3

Process finished with exit code 0
'''


