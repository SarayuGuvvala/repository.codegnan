'''
mutable data type
-----------------
--> I can modify directly on the variable,which the datatype have taken
eg
-- list,dict
immutable data type
------------------
--> where can not be modified directly on the variable assigned to the datatype
eg
-- int,string
'''
num=9
num_2=10
print(num+num_2)
print(num)
print(num_2)
'''
integer or int
--------------
-->storing number or digit in the variable is called int or integer
num=90
float
-----
-->storing decimal value in the variable is called float
num_2=89.67

Indexing
---------
-->This is used to get a particular substring or item from string ,list and tuple by calling with index position
syntax
-------
variable_name[index_position]
'''
any=("python is a  programming language")
print(any[5])
'''
Concatenation
-------------
-->A + acts as different way, if we are adding 2 integers it acts like addition in other cases such as list,string and tuple it act like concatenation

num=[9,8]
num_2=[9,7]
print(num+num_2)
any="Python"
so="Language"
print(num+any)

string or str
-------------
-->string is a collection of character that are inclosed in '',"",''' '''
-->it is an immutable datatype
'''
any=",.@t9F"
print(any)
'''
Methods
-------
replace()-->this method is used to replace or change old substring with new string
syntax
-------
variable_name.replace("old string","new string")
'''
any="Python is a programming language"
print(any.replace("Python","Java"))
print(any)
'''
split()
-------
-->this is method is used to separate the string using a substring and it will split into list such as before the substring is one index after substring is another index
syntax
------
-->variable_name.split("substring")
'''
any="Python is a programming language"
print(any.split(" "))
any="Python is a programming language"
print(any.split(" a"))

'''
strip()
-------
-->this method is used to remove from 1st index position or from last index position
'''
any="Python is a programming language"
print(any.strip("e"))
'''
count()-->it is a buit-in method used mainly with strings,lists, and tuples to countbhow many times a value appears
-------
syntax-->variable_name.count()
'''
any=="Python is a programming language"
print(any.count("a"))
'''
capitalize()-->is a string method that converts the first character to uppercase and the rest to lowercase
-----------
syntax-->variable_name.capitalize()
'''
print("python".capitalize())
'''
isdecimal()-->is a string method that checks whether all characters in a string are decimal digits(0-9)
'''
print("123".isdecimal())
print("12.3".isdecimal())
print("123abc".isdecimal())
'''
join()-->used to join elements of a sequence (list/tuple) into a string
syntax-->"separator".join(iterable)
'''
print(" ".join(["python","is","a","language"]))
print("-".join(["python","is","a","language"]))
'''
islower()-->checks if all characters are lowercase
syntax-->variable_name.islower()
'''
any=("python is a programming language")
print(any.islower())
'''
isupper()-->checks if all characters in uppercase
syntax-->variable_name.isupper
'''
any=("python is a programming language")
print(any.isupper())
any=("PYTHON IS A PROGRAMMING LANGUAGE")
print(any.isupper())
'''
isalnum()-->checks if string contains only letters + numbers(no space/symbols)
'''
print("python123".isalnum())
print("python 123".isalnum())
'''
isalpha()-->checks if string contains only letters
'''
print("python123".isalpha())
print("python".isalpha())
'''
isdigit()-->checks if strings contains only digits
'''
print("python123".isdigit())
print("123".isdigit())


