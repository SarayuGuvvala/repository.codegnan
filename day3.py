'''
 Operators
---------
1.Arihmetic Operator
2.Assignment Operator
3.Comparison Operator
4.Logical Operator
5.Identity Operator
6.Membership Operator
7.Bitwise Operator

1.Arithmetic Operator-->+,-,%,*,**,//
'''
num=78
num_2=89
num_3=90
print(num+num_2+num_3)
'''
-
'''
num=78
num_2=3
print(num-num_2)
'''
%
'''
num=80
num_2=8
print(num%num_2)

num=80
num_2=8
print(num%num_2==0)
'''
*
'''
num=66
num_2=9
print(num*num_2)
'''
**
'''
num=66
num_2=9
print(num**num_2)
'''
Assignment Operator-->=,+=,-=,*=,%=,//=.**=,&=
'''
num=9
num+=8
print(num)

num=9
num-=8
print(num)

num=9
num*=8
print(num)

num=9
num**=8
print(num)

num=9
num%=8
print(num)

num=9
num//=8
print(num)

num=9
num&=8
print(num)
'''
Comparison Operator-->==,!=,>,<,>=,<=
'''
num=9
num_2=9
print(num==num_2)

num=9
num_2=10
print(num!=num_2)

num=9
num_2=10
print(num>num_2)

num=9
num_2=8
print(num<num_2)

num=9
num_2=9
print(num>=num_2)

num=9
num_2=88
print(num<=num_2)
'''
Logical Operators:
-->and: the 2 conditions should be true
-->or : any one condition should be true
-->not: it is used to reverse the output
'''
A=8
B=9
print(A<10 and B<10)

A=8
B=90
print(A<10 or B<10)

a=8
b=90
print(a<10 not b<10)

'''
Identity Operators:
is--> This operator is used to check the object
is not-->this operator is used to check the object is not same
'''
a=10
b=10
print(a is b)

list_=[1,2]
list_2=[1,2]
print(list_ is list_2)
print(list_ == list_2)

list_=[1,2]
list_2=[1,2]
list_3=list_
print(list_ is list_3)
print(list_ == list_2)

list_=[1,2]
list_2=[1,2]
print(list_ is not list_2)
print(list_ == list_2)

'''
Membership Operator:in , not in
in--> is used to check, if present init
not in-->is used to check , it is not there then also it showsthat it present
'''
list_=[1,2,3]
print(9 in list_)

list_=[1,2,3]
print(2 in list_)

list_=[1,2,3]
print(9 not in list_)

'''
Bitwise Operator:
&-->Bitwise AND
5-->0101
3-->0011
--------
1-->0001
'''
print(5&3)
'''
|-->Bitwise OR
5-->0101
3-->0011
---------
7-->0111
'''
print(5|3)

'''
^-->Bitwise XOR
5-->0101
3-->0011
--------
6-->0110
'''
print(5^3)












