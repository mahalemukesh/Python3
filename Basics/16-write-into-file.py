file = open('text.txt', 'w')

file.write('Hello\n')
file.write('I am learning basics of Python')

file.close()

##Sample output
$ cat text.txt               <--------------Current contets of file
adsd
mbaslnfslk
bfcsds
nsdknsdkc
ndslkcdksnc
ncslkncsn
knjbos
nbsdkc


$ python3.10 write_file.py   <--------- Run above python code

$ cat text.txt               <-------- After running python, its overwrite the file
Hello
I am learning basics of Python
