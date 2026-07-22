class Student:
    def __init__(self, student_id, name,age):
        self.student.id = student_id
        self.name = name
        self.age = age
    def display_student(self):
        print("Student ID:",self.student_id)
        print("Name:",self.name)
        print("Age:",self.age)
class University:
    def __init__(self,university_name,faculty_name):
        self.university_name = university_name
        self.faculty_name = faculty_name
        self.students=[]
    def add_student(self, student):
        self.students.append(student)
    def display(self):
        print("University:",self.university_name)
        print("Faculty:",self.faculty_name)
        print("\nstudent details:")
        for student in self.students:
            student.display_student()
            print()
# Main Program
university = university("Andhra University","Computer Science")
n = int(input("Enter number of students:"))
for i in range(n):
    print("\nEnter details for student",i+1)
    student_id = input("enter student ID:")
    name = input("enter name:")
    age = int(input("enter age:"))

    student = Student(student_id,name,age,subject)
    uni.add_Student(student)
uni.display()
    
        



        
        
