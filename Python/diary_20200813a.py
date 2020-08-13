Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> int
<class 'int'>
>>> type(a)
<class 'int'>
>>> a
10
>>> 10 == int
False
>>> type(a) == int
True
>>> if type(a) == int:
	print("labi")

	
labi
>>> 
>>> a=10
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
else:
	print(slikti)

	
Traceback (most recent call last):
  File "<pyshell#22>", line 4, in <module>
    print(slikti)
NameError: name 'slikti' is not defined
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
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

>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> 
>>> 
>>> 
>>> a=10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> a=fg
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a=fg
NameError: name 'fg' is not defined
>>> a="fdsfs"
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
slikti
>>> print("aaa\n bbb\n ccc")
aaa
 bbb
 ccc
>>> print("aaa\t bbb\v ccc\nddd")
aaa	 bbb ccc
ddd
>>> 
