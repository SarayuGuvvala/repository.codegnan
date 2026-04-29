'''
set data type
-------------
-->set is a collection of unordered elements or unique elements unlike list or tuple set is not permit duplicates in side.
-->indexing will wont work in sets
-->set is mutable
ex:
'''
sa={1,2,3,3,4}
print(sa)
'''
Methods
-------
1.add()
-------
-->This method id used to add new item into the set
syntax-->variable_name.add(item)
ex:
'''
sa={1,2,3,}
sa.add(4)
print(sa)
'''
2.Remove()
----------
-->This method is used to delete an item in the set
syntax-->variable_name.remove(value)
ex:
'''
sa={1,2,3,}
sa.add(4)
sa.remove(3)
print(sa)
'''
3.pop()
-------
-->This is also used to delete elements in the set,but we can't specify the element
syntax-->variable_name.pop(no arguments)
ex:

sa={1,2,3,}
sa.add(4)
sa.pop(2)
print(sa)
'''
sa={1,2,3,}
sa.add(4)
sa.pop()
print(sa)
'''
4.clear()
---------
-->This method is used to delete all elements in the set
syntax-->variable_name.clear()
ex:
'''
sa={1,2,3,}
sa.clear()
print(sa)
'''
5.update()
-----------
-->same like add,but this method will add more than one element
syntax-->variable_name.update()[elements]
ex:
'''
sa={1,2,3}
sa.update([4,5,6],[7,8,9])
print(sa)
'''
6.union()
---------
-->This method will return a set all elements from both sets,but not duplicaates
syntax-->set_1.union(set_2) or set_1 | set_2
ex:
'''
sa={1,2,3}
va={2,4,6}
print(sa.union(va))
print(sa|va)
'''
7.intersection()
-----------------
-->This method will give only the common elements from both sets
syntax-->set_1.intersection(set_2) or set_1 & set_2
ex:
'''
sa={1,2,3}
va={2,4,6}
print(sa.difference(va))
print(sa&va)
'''
8.difference()
---------------
-->This methid is used to get the different elements from both sets
syntax-->set_1.difference(set_2)
ex:
'''
sa={1,2,3}
va={2,4,6}
print(sa.difference(va))
print(sa-va)
'''
Type Conversions
-----------------
-->Converting one data type into another data type
-int-->string ad float
ex:
'''
a=8
b=str(a)
c=float(b)
print(c)
'''
-float-->string and int
ex:
'''
z=56.78
d=int(z)
e=str(z)
print(e)
print(type(e))
'''
-str-->int,flost.tuple,list
ex:
'''
z="56"
g=list(z)
print(g)
print(type(g))
