'''
elif statement
---------------
-->This statement gives more options to get result of thet program

marks_stu =int(input("Enter marks:"))
if(marks_stu >=90):
    print("A+")
elif marks_stu >=80:
    print("A")
elif marks_stu >=70:
    print("B+")
elif marks_stu >=60:
    print("B")
elif marks_stu >=50:
    print("C+")
elif marks_stu <=35 :
    print("fail")

Nested if
---------
-->if statement inside another if statement called as nested if statement

user_SBI_info={"ATM PIN":"9900"}
user_pin = input("Enter your ATM PIN:")
if len(user_pin)==4:
  if user_pin in user_SBI_info("ATM PIN"):
     print("Welcome to SBI ATM")
  else:
     print("please enter the correct pin")
else:
     print("please enter the 4 digit pin")

for loop statement
------------------
-->A for statements used to iteration over items like (string,list,tuple,)with fixed number of iterations

else statement in for
---------------------
-->After completing all iterations this else statement will execute 
'''
any=[23,45,67,88]
for j in any:
    print(j)
else:
    print("loop finished")

so = "madam"
empty_=""
for j in so:
    empty_ = j + empty_
if empty_ == so:
     print("Palindrom")
else:
     print("not palindrom")
        

