'''
list data type
-------------
-->list is a collection of different data types and it is represented by [] and it is separated by comma.
'''
any=[1,"Python is a language",[2,"this is 5th class",4],67]
print(any[2][1][10]]

any=[1,"Python is a language",67,68,[34,["this is a python class "],78,"i am looking for good bat"],[2,"this is 5th class",4],56]
print(any[4][1][0][18])

so="Python is a programming language"
print(so.replace("Python","Java"))
print(so)

'''
Methods
-------
1.append()
-->this is used to add new item into the list, but it will add in the last index position

syntax-->variable_name.append(item)
'''
any=[1,2,3,4]
any.append(45)
print(any)
any.append(30)
print(any)

any=[1,2,3,4]
any.append([45,10])
print(any)
'''
2.extend()
-->this method is also used to add new item into list,but this extend add as each position into each index in the list
-->extend only take iterables
syntax-->variable_name.extend(index position)
'''
any=[1,2]
any.append([2,3])
any.extend([2,3])
print(any)
      
any=[1,2]
any.append("python")
any.extend("language")
print(any)
''' 
3.pop()
-->thia is used to delete an item from a list ,this pop() remove based on the index position mentioned in the parameters.if nothing is mentioned in parameters then it will remove last index position
syntax-->variable_name.pop(index position)
'''
any=[1,2,3,4,5]
any.pop(4)
print(any)
'''
remove()
--------
-->this is also used to delete item from the list,but remove() method will remove the value
syntax-->variable_name.remove(value)
'''
any=[1,2,3,4,5]
any.remove(5)
print(any)
'''
slicing()
-------
-->this is used to get the particular part of the list.string or tuple
-->this will work based on index position
syntax-->variable_name([starting index:ending index])
'''
any=[1,2,3,4,5]
print(any[2:5])
'''
Length()
--------
--> the length method is used to find the length of items present in the list
syntax-->len(variable)
'''
any="python is a language"
print(len(any))
'''
count()
-------
-->this method is used to find how many times a value appears
syntax-->variable_name.count(value)
'''
any="python is a programming language"
print(any.count("p"))
'''
index()
------
this method is used to find the position of an element in a sequence like a string,list,or tuple
syntax--.variable_name.index()
'''
any="python is a programming language"
print(any[3])
'''
insert()
--------
-->this method is used to add an element at a specific position in a list
syntax-->variable_name.insert(index value,value)
'''
any=[1,2,3,4,5,6]
any.insert(1,3)
print(any)
any=[20,30,10,11]
any.sort()
print(any)



