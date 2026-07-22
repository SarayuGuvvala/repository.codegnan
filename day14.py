'''
print statement
---------------
-->This print statement shows output on the screen
return statement
----------------
-->sends a value back to the caller or calling function for the program to reuse

def great(name):
print(f"hello {name}")
result =great("bob")
print(result)

in-built functions
------------------
-->len()-this function is used to find out the length of the number of values present in iterables
eg:string,list,tuple
string="python"
print(len(string))

->max()
-------
-->this is used to get the maximum value
eg:list,tuple

list=[29,84,56]
print(max(list)) #could not able to use datatypes

min()
-----
-->this is used to get the minimum value
type()
range()
rescursion()-->a function calling itself called recursion function

def fact(num):
    if num == 0 or num == 1:
        return 1
    return num*fact(num-1)
print(fact(6))
'''
num=24
for j in range(1,11):
    print(f"{num} x {j} = {num*j}")

def table(num):
    for j in range(1,11):
        print(f"{num} x {j} = {num*j}")
table(num = int(input("enter a number:")))

        
