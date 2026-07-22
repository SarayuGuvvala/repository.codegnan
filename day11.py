'''
Patterns
'''
# '*' in triangle shape
def right_triangle(num):
 for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
right_triangle(4)
# numbers in triangle shape
num = int(input("Enter a number: "))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end=" ")
    print()

# '*' in reverse triangle
num = int(input("Enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()    
# reverse number
num = int(input("Enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()      

# Pyramid
num = int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(num-i, 0, -1):
        print(" ", end=" ")
    for k in range(1,2*i):
        if k == 1 or k == 2*i-1 or i == num:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()        
'''
#calculater
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a numner: "))
choice = int(input("\n1.+ \n2.- \n3.*"))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
else:
    print("choose the valid option ")
