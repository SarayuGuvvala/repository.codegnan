'''
Polymorphism
------------
-->polymorphism is many ways or many forms the same method operator or a function can perform a different actions depending upon from
the object on a datatype

Methods-
---------
1.Method Overloading - defining multiple methods with the same name but with different parameters (different number or type of arguments)
in a class
2.Method overiding
3.Operator overriding
eg-1
'''
class Addition:
    def add(self,a,b=0,c=0):
     return a+b+c
obj = Addition()
print(obj.add(30,90))
'''
eg-2
'''
class power:
    def pow(self,a,b):
     return a**b
obj = power()
print(obj.pow(3,6))
'''
Method Overriding-
-----------------
-->
'''
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("dog barks")
ani = dog()
ani.sound()
'''
Operator Overloading
---------------------
-->
'''
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,any_):
        return self.marks + any_marks
so = student(89)
how = student(88)
print(so+how)
'''
Abstraction
-----------
-->
'''
class abc import ABC abstractmethod
class vehicle (ABC):
    abstractmethod
    def start(self):
        pass
class car(vehical)
