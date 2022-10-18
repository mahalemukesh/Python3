# .strip()  ---> To remove white spaces
# len()     ---> To count lenth of string
# .lower()  ---> To convert into lower cases
# .upper()  ---> To convert into upper cases
# .split()  ---> Split by delimiter like . , ; / or any letter

text = input('Insert your name')
print(text.strip())

## Sample output
$ python3.10 string_methods.py                  <--------------- With .strip()
Insert your name    dfjkskd                     <--- Here I have enterned string with some spaces at start and end
dfjkskd

$ python3.10 string_methods.py                  <--------------- With len() [print(len(text))]
Insert your name: Mukesh
6

$ python3.10 string_methods.py                  <--------------- With .lower() i.e.[print(text.lower())]
Insert your name: MUKESH
mukesh

$ python3.10 string_methods.py                  <--------------- With .upper() i.e.[print(text.upper())]
Insert your name: mukesh
MUKESH

$ python3.10 string_methods.py                  <--------------- With .split() i.e.[print(text.split('.'))]
Insert your name: my.name.is.mukesh
['my', 'name', 'is', 'mukesh']
