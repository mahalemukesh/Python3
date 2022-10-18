fruits = ['mango', 'apple']
print(fruits)

fruits.append('banana')
print(fruits)



## List always defined in square brackets i.e. []

##Sample output
$ python3.10 list.py 
['mango', 'apple']

$ python3.10 list.py             <------- Add new iten to the list 
['mango', 'apple']
['mango', 'apple', 'banana']


$ python3.10 list.py             <------ Replace item frm list like 'fruits[1] = 'new item'
['mango', 'apple']
['mango', 'pear']


$ python3.10 list.py             <-------- Print specific iten from the list like 'print(fruits[2])' 
apple
banana

