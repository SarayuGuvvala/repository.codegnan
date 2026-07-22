'''
Fibonacci
'''
num = 0
num_1 = 1
any = int(input("Enter a number:"))
print(num+num_1,end=" ")
for j in range(1,any+1):
 num_2 = num+num_1
 num = num_1
 num_1 = num_2
 print(num_2,end=" ")

'''
Amstrong
'''
Amstrong_ = int(input("Enter a number:"))
total = 0
length_ = len(str(Amstrong_))
for j in str(Amstrong_):
    total += int(j) ** length_
    print(total)
if total == Amstrong_:
    print(f"(Amstrong_) is a Amstrong number")
else:
    print(f"(Amstrong_) is not an Amstrong number")

'''
Divisibility for 2 numbers
'''
num =100
for j in range(1,num+1):
  if j % 3 == 0 and j % 5 == 0:
    print(f"{j} is divisible by 3 and 5")

'''
'''
any = [35,68,60,2,3,8]
def sum_even(any):
    total = 0
    for j in any:
        if j %2 == 0:
            total += j
        print(total)
sum_even(any)
'''
Lambda Function
---------------
-->A Lambda function is a small Anonymous function (a single line expression).This lambda function can take a n
number of arguments but can only have a one expression.
Syntax-->lambda keyword (arguments): expression
'''
num = lambda a,b : a/b
print(num(186,20))

num = lambda a,b : a*b
print(num(18,14))

num = lambda a : a+a
print(num(80))

num = lambda a : a**a
print(num(80))

      
