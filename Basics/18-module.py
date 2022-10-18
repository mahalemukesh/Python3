import math

print(math.radians(60))
print(math.pi)

###Sample output
$ python3.10 module.py 
1.0471975511965976
3.141592653589793

## To define our own module with function
import myModule

print(myModule.myFunct(9))

## Sample output
$ python3.10 module.py 
14

##myModule defined in myModule.py file
def myFunct(x):
    return x + 5
