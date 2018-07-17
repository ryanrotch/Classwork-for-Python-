# q2
# In q1 above, write a python program to grade the students
marks=int(input("scores"))
if marks<40:
    print("your grade is an :\t E")

elif marks>=40 and marks <50:
    print("your grade is a : \t D")
elif marks>=50 and marks <60:
    print("your grade is a : \t C")
elif marks>=60 and marks <70:
    print("your grade is a : \t B")
elif marks>=70 and marks <100:
    print("your grade is an : \t A")
elif marks>100 or marks <0:
    print("please input a valid grade")