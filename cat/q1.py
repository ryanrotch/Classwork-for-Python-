       # question 1
# Write a python program to calculate the average scores of five classes
# with 10 students 10 each and display the output as a :
# 1. tuple()
# 2.list[]
# 3.dictionary{}
class scores_average:
    def average(self,classes):
        self.class1= classes
        self.class2= classes
        self.class3 = classes
        self.class4 = classes
        self.class5 = classes
class1=[int(input("student1:\n")),int(input("student2\n")),int(input("student3\n")),
        int(input("student4\n")),int(input("student5\n")),int(input("student6\n")),
        int(input("student7\n")),int(input("student8\n")),int(input("student9\n")),
        int(input("student10\n")),]


class2=[int(input("student1:\n")),int(input("student2\n")),int(input("student3\n")),
        int(input("student4\n")),int(input("student5\n")),int(input("student6\n")),
        int(input("student7\n")),int(input("student8\n")),int(input("student9\n")),
        int(input("student10\n")),]

class3=[int(input("student1:\n")),int(input("student2\n")),int(input("student3\n")),
        int(input("student4\n")),int(input("student5\n")),int(input("student6\n")),
        int(input("student7\n")),int(input("student8\n")),int(input("student9\n")),
        int(input("student10\n")),]

class4=[int(input("student1:\n")),int(input("student2\n")),int(input("student3\n")),
        int(input("student4\n")),int(input("student5\n")),int(input("student6\n")),
        int(input("student7\n")),int(input("student8\n")),int(input("student9\n")),
        int(input("student10\n")),]


class5=[int(input("student1:\n")),int(input("student2\n")),int(input("student3\n")),
        int(input("student4\n")),int(input("student5\n")),int(input("student6\n")),
        int(input("student7\n")),int(input("student8\n")),int(input("student9\n")),
        int(input("student10\n")),]

sum1=sum(class1)
sum2=sum(class2)
sum3=sum(class3)
sum4=sum(class4)
sum5=sum(class5)

average1=sum1/10
average2=sum2/10
average3=sum3/10
average4=sum4/10
average5=sum5/10
print("OUTPUT OF THE AVERAGE OF THE SCORES AS A TUPLE VALUE")
average=(average1,average2,average3,average4,average5)
print(average)
print("OUTPUT OF THE AVERAGE OF THE SCORES AS A LIST VALUE")
average=[average1,average2,average3,average4,average5]
print(average)
print("OUTPUT OF THE AVERAGE OF THE SCORES AS A DICTIONARY VALUE")
average={sum1:average1,sum2:average2,sum3:average3,sum4:average4,sum5:average5}
print(average)