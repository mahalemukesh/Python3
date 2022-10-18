loop = True

while loop:
  name = input('insert something, ')
  if name == 'stop':
    loop = False
    break
    
    
## Sample output
$ python3.10 while.py 
insert something, czlkc
insert something, n,sdlk'nv
insert something, 1924
insert something, stop

$ python3.10 while.py    <----- By removing 'break' on last line, still it will run with 'loop = False' statement 
insert something, dds
insert something, sdf
insert something, stop


$ python3.10 while.py    <---- By removing 'loop = False' on line 6,it will run with 'break' on last line
insert something, c slm
insert something, cnsd
insert something, stop
