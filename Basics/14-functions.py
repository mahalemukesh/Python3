def addTwo(x):
    return x + 2
  
def substractTwo(x):
    return x - 2

newNumber = addTwo(9)
print(newNumber)

subNumber = substractTwo(9)
print(subNumber)

def printString(string):
    print(string)

printString('Hello')



##Sample output
$ python3.10 functions.py        <---- By using x = 9
11
7

$ python3.10 functions.py        <---- With string = 'Hello'
11
7
Hello
