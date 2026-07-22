'''any = eval(input("enter list:"))
empty_=[]
for i in any:
    if i not in empty_:
           empty_.append(i)
print(empty_)
'''
nums=[20,30,50,66]
max_1=0
max_2=0
for num in nums:
    if num > max_1:
        max_2=max_1
        max_1=num
print(f"{max_2} is the second maximum number in the list of {nums}")

