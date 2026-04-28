'''
Tuple
-----
-->tuple is a collection of different data types that are represented by () and the items in the tuple is separated by commas
'''
any=(2,"Python",[7,8],(5,1),1)
print(any)

any=(2,"Python",[7,8],(5,1),1)
print(any[4])#index

so=(1,2,3,4)
any=(5,6,7,8)
print(so+any)#concatenation
'''
dictionary
----------
-->dict is a collection of key:value pair . where keys are unique are immutable data types,such as (strings,int and tuple) and values are any data type and is represented by curly brackets
Methods
-------
keys()-->this method is used to acces only keys in the dictionary
syntax-->dict.keys()
eg-
'''
my={"Name":"Sarayu","age":21,"education":"B.Tech"}
print(dict.keys(my))
'''
value()-->This is used to access only values in the dictionary
syntax-->dict.values()
'''
my={"Name":"Sarayu","age":21,"education":"B.Tech"}
print(dict.values(my))
'''
items()-->This method is used to access key : value pair in the dictionary
syntax-->dict.items()
'''
my={"Name":"Sarayu","age":21,"education":"B.Tech"}
print(dict.items(my))
'''
clear()--> this method is used to delete all the items in the dict
syntax-->dict.clear()
'''
my.clear()
print(my)

'''
update-->this method is used to add new(key : value) into the dictionary
syntax-->dict,update({key:value})

'''
my={"Name":"Sarayu","age":21,"education":"B.Tech"}
my.update({"role":"Python developer"})
print(my)


