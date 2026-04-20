'''
-->variables
----------
To define a variable, we have 2 rules
1.Good way to define a variable (no error)
2.Bad way to define a variable (will get error)
'''
_v = 80
print(_v)
'''
rule 2: Adding the special character or spaces then we will get the error's
-->Given examples are the bad way's that will get an error
'''
num = 90
num=59
num=34
'''
--> We are going to use meaningful words or name for defining variables
'''
_num=78
num_2=89
print(_num)
print(num_2)
'''
Keywords
--------
-->This Keywords not gonna use as a variable
-->We can also called as identifiers (or) reserved
--> if,else,for,while this we are not going to use
'''
a,b,c=60,89,90
print(a)
print(b)
print(c)
'''
Tokens
------
-->Nothing but a small program or code in python to complete the task
'''
a,b,c=20,36,78
print(a+b)
print(b-c)
print(a,b,c)
'''
Comments
--------
-->These are 2 types
1.single line comment
-->This is used to explain about that particular line in the code, for this we can use # simple
2.Multi-line comment
-->To comment more than single line we can use multi line commenting
"""double""",''' '''
-->that wont be consider by the cursor
'''
a,b,c=20,55,66 #here in the same line, i have assign 3 variable and 3 values
print(a+b)
'''
boolean type
-->This is used to find out the statement is TRUE or FALSE
'''
a=90
b=89
print(a !=b)
'''
--defining the even number
'''
num= 8
if num%2==0:
    print(f"(num) is even number")
else:
    print(f"(num) in odd number")
