'''
File Handling
--------------
-->File Handler is an object of a file to maintain several functions of a file like creating,reading,updating and deleting the file
2 Ways to open the File
-----------------------
1.open()
syntax: file handler = open("filename.txt","mode")
        --------------------
        --------------------
        file handler.close()
        
2.with open()
syntax: with keyword open("file name","mode") as file handler:
'''
any = open("demo.txt","r")
print(any.read())
any.close()

with open("demo.txt","r") as so:
    print(so.read())

'''
with keyword
------------
-->Using this with keyword no need to close the file in the lines, it will close the file automatically
Modes:
-----
r-->to the file and throught error if the file does not exist......
a-->used to add the text at last, if the file does not exist it will create
'''
with open("demo.txt","a") as so:
    print(so.write("I Completed my Graduation"))

with open("demo.txt","w") as so:
    print(so.write("I am currently Building my skills in Data Analytics"))# to replace old text with new text
'''
with open("dem.txt","x") as so:
    print(so.write("hi"))# file creation

any = open("demo.txt","r")
print(any.read())


read()
------
--> the read method can read the entire file chunk by chunk where we can specify the size.
'''
with open("demo.txt","r") as so:
    print(so.read(4))

'''
read line()
-----------
--> this method can read one line at a time
note
-----
-->the "w" mode and "a" mode we will use write() method

eg: User defined Exception
--------------------------
'''
class myerror(Exception):
    pass
age = int(input("enter age:"))
try:
    if age < 18:
        raise myerror("age must be 18 or above")
    else:
        print("eligible to vote")

except myerror:
    print("logical error")

          
