'''
User input
----------
'''
so= int(input("enter the number:"))
print(so)

any=input("enter the words:")
print(len(any))

so=(input("enter any words:"))
print(type(so))

a,b=map(int,input("enter the numbers:"))
print(a,b)
'''
passing two  values
-------------------
'''
a,b=map(int,input("enter the numbers:"))
print(a)
print(type(a))
print(b)
print(type(b))
'''
list data type
--------------
'''
a,b=list(map(int,input("enter the numbers:").split()))
print(a)
print(type(a))
print(b)
print(type(b))
'''
tuple data type
---------------
'''
a,b=tuple(map(int,input("enter the numbers:").split()))
print(a)
print(type(a))
print(b)
print(type(b))

a=89
b=89
print("Added a and b and the result is",a+b)
'''
Statements
-----------
if statement
------------
-->if stsement is used to check if the condition is true or not
'''
an=9
if an == 9:
    print(f"an is equal to (9)")
    
an=9
if an >= 9:
    print(f"an is equal to (9)")
'''    
else statement
--------------
-->else is a fall-back statement,incase if statement becomes false,it can enter into else
'''
an=9
if an >9:
    print(f"an is equal to (9)")
else:
    print(f"an is not equal to (9)")

a=90
b=90
if a>b:
    print(f"a is greater than b")
else:
    print(f"a is equal to b")

a=90
b=30
if a>b:
    print(f"a is greater than b")
else:
    print(f"a is not greater than  b")    
    
n= eval(input("enter:"))
print(type(n))
print(n)

age=int(input("enter your age:"))
if(age>=18):
    print("you are elgible to vote")
else:
    print("you have to wait (18-age) more years")

marks=int(input("enter your marks:"))
if(marks>=35):
    print("pass")
else:
    print("fail")


