'''
Inheritance
-----------
-->inheriting  the attributes or methods from base class to child class
eg
'''
class parent:
    pass
class child(parent):
    pass
'''
single inheritance
------------------
-->a child class inherits from one base class
'''
class Animal:
    def sound(self):
        print("Animals  make sounds")

class dog(Animal):
    def bark(self):
        print("dog bark")

D = dog()
D.sound()
D.bark()

'''
multiple inheritance
--------------------
-->a child class inherits properties from more than one parent class
'''
class Father:
    def skills_1(self):
        print("Driving")

class Mother:
    def skill_2(self):
        print("cooking")

class child(Father,Mother):
    def All_skills(self):
        print("coding")

c = child()
c.skills_1()
c.skill_2()
c.All_skills()
'''
single inheritance 2nd example
'''
class Animal:
    def sound(self):
        print("Animals make sounds")

class cat(Animal):
    def sound_2(self):
        print("meow meow")

c= cat()
c.sound()
c.sound_2()
'''
multiple inheritance example2
'''
class python:
    def skills_1(self):
        print("coding in python")
class aptitude:
    def skills_2(self):
        print("tricks to solve mathematical problems")
class softskills:
    def skills_3(self):
        print("communication skills")
class child(python,aptitude,softskills):
    def all_skills(self):
        print("learning")
c = child()
c.skills_1()
c.skills_2()
c.skills_3()
c.all_skills()

'''
multi-level inheritance
-----------------------
--> collects properties from another child class
.
'''
class grandfather:
    def house(self):
        print("Grandfathers house")
class Father(grandfather):
    def land(self):
        print("Fathers land")
class son(Father):
    def property(self):
        print("property")

s = son()
s.house()
s.land()
s.property()
'''
Hierarchical inheritance
------------------------
-->multiple child classes inherits the properties from same parent class
'''
class father:
    def property(self):
        print("fathers property")
class child_1(father):
    def car(self):
        print("first child car")
class child_2(father):
    def house(self):
        print("second child house")
c1 = child_1()
c2 = child_2()
c1.property()
c1.car()
c2.property()
c2.house()
'''
Hybrid inheritance
-----------------
-->
'''
class A:
    def methodA(self):
        print("class A")
class B(A):
    def methodB(self):
        print("class B")
class C(A):
    def methodC(self):
        print("class C")
class D(B,C):
    def method(self):
        print("class D")
so = D()
so.methodA()
so.methodB()
so.methodC()
so.method()
'''
supper class
------------
-->
'''
class parent:
    def __init__(self):
        print("Parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
c = child()
