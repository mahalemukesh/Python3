height = input('Please enter your Height,')

if int(height) < 1:
   print('You cannot irde, under 1M')
elif int(height) > 5:
   print('You cannot ride, above 5M')
else:
   print('You can ride!!!!')
    


##Sample output
$ python3.10 else.py 
Please enter your Height,1
You can ride!!!!

$ python3.10 else.py 
Please enter your Height,2
You can ride!!!!

$ python3.10 else.py 
Please enter your Height,5
You can ride!!!!

$ python3.10 else.py 
Please enter your Height,6
You cannot ride, above 5M
