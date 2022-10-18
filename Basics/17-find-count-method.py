# .find()  --> To find out the str, it will give response as first index of word/letter
# .count() --> To count the word/letter, how many times it occured in given string
#.find()
string = 'hello'
print(string.find('o'))

##Sample output
$ python3.10 find_count.py 
4


###########
#.count()
string = 'hello'
print(string.count('l'))

##sample output
$ python3.10 find_count.py 
2

###
#.count() to verify _ is present in input text
string = input('Please type password: ')

if string.count('_') > 0:
    print("Please try to avoid '-' ")
else:
    print('All good')

##Sample output
$ python3.10 find_count.py        <---------------With normal input
Please type password: Hellow
All good


$ python3.10 find_count.py        <--------------- With _ input
Please type password: _hello
Please try to avoid '-' 
