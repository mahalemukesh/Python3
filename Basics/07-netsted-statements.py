x = 2
y = 3

if x == 2:
  if y == 3:
    print('x = 2, y = 3')
  else:
    print('x = 2, y != 3')
else:
  print('x != 2')
  
  
## Sample output
$ python3.10 nested.py      <----- When x=2 and y=3
x = 2, y = 3

$ python3.10 nested.py      <----- When x=2 and y=4
x = 2, y != 3

$ python3.10 nested.py      <----- When x=3 and y=4
x != 2
