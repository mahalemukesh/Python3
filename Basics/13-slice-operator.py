#Slice operator
#[::] ---> start:stop:step
#[:]  ---> start:stop

fruits = ['apple', 'banana', 'orange']
text = 'I like Fruits'

print(text[2:])

##Sample output
$ python3.10 slice.py           <----- By using [2:]
like Fruits

$ python3.10 slice.py          <----- By using [4:]
ke Fruits

$ python3.10 slice.py          <----- By using [:5]
I lik

$ python3.10 slice.py          <----- By using [3:7]
ike 

$ python3.10 slice.py          <----- By using [::2]
ike 
Ilk ris

$ python3.10 slice.py          <---- To add new iten  by  fruits[0:0] = 'b'
['apple', 'banana', 'orange']
['b', 'apple', 'banana', 'orange']

