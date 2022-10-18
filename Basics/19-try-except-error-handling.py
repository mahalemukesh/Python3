#This is useful in error handling
text = input('Username: ')

try:
    number = int(text)
    print(number)

except:
    print('Invalid Username')
    
##Sample output
$ python3.10 try_except.py 
Username: mukesh                <-------------- With Username as string
Invalid Username

$ python3.10 try_except.py 
Username: 1234                 <-------------- With Username as number
1234
