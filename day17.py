'''
list comprehension-->list comprehension offers shortest syntax when we want to create a new list based on the value
of an existing list
syntax: [expression loop condition]
----------------------
old_1=[12,3,5,68,90]
new_1=[i if i%2 != 0 else "even"  for i in old_1]      
print(new_1)

Dictionary Comprehension
------------------------
-->dictionary comprehension offers shortest syntax that we want to create in new dictionary based on the values
of an existing dictionary

an_1 ={"a":2,"b":3,"c":5}
an_2 = {i:j for (x,y) in an_1}
print(an_1)

Generators:
-----------
-->Generator in python is enable lazy evolution for producing sequence of values effectively.
-->They actually differ from regular functions by execution and resuming on demand.
-->Generators create iterators that yield values one at a time using the yield keyword.
'''
for i in range(1,10):
 print(i)
'''
Functions VS Generators:
------------------------
-->The general regular functions execute fully upon call and return a single value , and terminates afterwards,
-->Generators use yield to produce multiple values lazily,acting like iterators without building the entire
sequence in memory.

Yield:
------
-->Yield pauses the generator function, saves its state (local variable,position), and returns the yielded value
to the caller.

Next(Keyword):
--------------
-->This advances the generator by executing until the next yield, returning that value, subsequent calls resume
from there.
'''
def add(num,num_1):
    print(num+num_1)
add(10,20)
add(20,30)

def count_(num):
    i = 1
    while i <=num:
     yield i
     i +=1
Gene_ = count_(3)
print(next(Gene_))
print(next(Gene_))
print(next(Gene_))

def message_gen():
    yield "First Message"
    yield "Second Message"
    yield "Done"
gen_ = message_gen()
print(next(gen_))
print(next(gen_))
print(next(gen_))









      
      
