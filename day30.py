'''
Date and Time
-------------
-->To work with date and time we use date and time module
'''
import datetime
today = datetime.date.today()
print(today)
'''
time

import datetime
time = datetime.datetime.now()
print(now.time())

common format code
------------------
%d ------> date
%y ------> year
%m ------> month
%h ------> hours
%s ------> sec
'''
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))


import datetime
date_1 = datetime.date(2026,1,26)
date_2 = datetime.date(2026,2,26)
diff = date_1 - date_2
print(diff.days)

import datetime
any = datetime.datetime.now()
print(any.hour)
print(any.minute)
print(any.second)
print(any.microsecond)
import math

num = 25

print("Square root:", math.sqrt(num))
print("Power:", math.pow(5, 2))
print("Factorial:", math.factorial(5))


