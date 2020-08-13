Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
SyntaxError: multiple statements found while compiling a single statement
>>> fruit = "banana"
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> fruit = "banana"
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 
>>> 
>>> 
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> 
>>> s = "Monty Python"
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> fruit = "banana"
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit = "banana"
>>> fruit[3:3]
''
>>> fruit = "banana"
>>> fruit [:]
'banana'
>>> greeting = "Hello World"
>>> new_greeting = "J" + greeting[1:]
>>> print(new_greeting)
Jello World
>>> word = "banana"
>>> count = 0
>>> for letter in word"
SyntaxError: EOL while scanning string literal
>>> for letter in word:
	if letter == "a":
		count = count + 1

		
>>> print(count)
3
>>> "a" in "banana"
True
>>> "seed" in "banana"
False
>>> if word == "banana";
SyntaxError: invalid syntax
>>> if word == "banana":
	print("All right, bananas.")

	
All right, bananas.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if word < "banana":
	print("Your word," + word + ", comes before banana.")
elif word > "banana":
	print("Your word," + word + ", comes after banana.")
else:
	print("All right, bananas.")

	
All right, bananas.
>>> if word < "banana":
	print("cucumber," + word + ", comes before banana.")
elif word > "banana":
	print("orange," + word + ", comes after banana.")
else:
	print("All right, bananas.")

	
All right, bananas.
>>> if word < "banana":
	print("Your word," + cucumber + ", comes before banana.")
elif word > "banana":
	print("Your word," + orange + ", comes after banana.")
else:
	print("All right, bananas.")

	
All right, bananas.
>>> if word < "banana":
	print("Your word," + cucumber + ", comes before banana.")
elif word > "banana":
	print("Your word," + sea + ", comes after banana.")
else:
	print("All right, bananas.")

	
All right, bananas.
>>> if word < "banana":
	print("Your word," + cucumber + ", comes before banana.")
elif word > "banana":
	print("Your word," + sea + ", comes after banana.")
else:
	print("All right, bananas.")

	
All right, bananas.
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'char', 'count', 'fruit', 'greeting', 'index', 'last', 'length', 'letter', 'new_greeting', 's', 'word']
>>> word = "banana"
>>> new_word = word.upper()
>>> print(new_word)
BANANA
>>> word = "banana"
>>> index = word.find("a")
>>> print(index)
1
>>> index = word.find("banana")
>>> 
>>> print(index)
0
>>> index = word.find("bana")
>>> print(index)
0
>>> word = "banana"
>>> index = word.find("banana")
>>> print(index)
0
>>> word = "banana"
>>> index = word.find("n")
>>> print(index)
2
>>> 
