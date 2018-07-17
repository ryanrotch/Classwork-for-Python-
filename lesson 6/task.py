# Define a class in python with its respective methods  to print
# out the details of five students in the following manner;
# 1.Name
# 2.Class
# 3.Admission Number
# Also, display the count of the students
class Students:
    stdCount=0
    def __init__(self,Name,Class,Admission_Number):
        self.Name=Name
        self.Class=Class
        self.Adm=Admission_Number

        Students.stdCount+=1

    def displayCount(self):
        print("Total students =%d"% Students.stdCount)

    # def displayEmployee(self):
    #     print("Name= ", self.Name + "\nclass= ", self.Class)

print("Enter Names,classes and admission number of student 1 ")
student1=Students(str(input()),str(input()),str(input()))

print("Enter Names,classes and admission number of student 2")
student2=Students(str(input()),str(input()),str(input()))

print("Enter Names,classes and admission number of student 3 ")
student3=Students(str(input()),str(input()),str(input()))

print("Enter Names,classes and admission number of student 4")
student4=Students(str(input()),str(input()),str(input()))

print("Enter Names,classes and admission number of student 5 ")
student5=Students(str(input()),str(input()),str(input()))

print(student1.Name)
print(student1.Class)
print(student1.Adm)

print(student2.Name)
print(student2.Class)
print(student2.Adm)

print(student3.Name)
print(student3.Class)
print(student3.Adm)

print(student4.Name)
print(student4.Class)
print(student4.Adm)

print(student5.Name)
print(student5.Class)
print(student5.Adm)

Students.displayCount(Students)