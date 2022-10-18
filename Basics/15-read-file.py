file = open('text.txt', 'r')
f = file.readlines()
file.close()

print(f)

##Sample output
$ python3.10 read_file.py 
['adsd\n', 'mbaslnfslk\n', 'bfcsds\n', 'nsdknsdkc\n', 'ndslkcdksnc\n', 'ncslkncsn\n', 'knjbos\n', 'nbsdkc\n']


## To remove all \n, try with below code
newList = []
for line in f:
    newList.append(line.strip())

print(newList)

##Sample output
$ python3.10 read_file.py 
['adsd', 'mbaslnfslk', 'bfcsds', 'nsdknsdkc', 'ndslkcdksnc', 'ncslkncsn', 'knjbos', 'nbsdkc']
