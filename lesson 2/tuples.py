#tuples can hold more than one item or data
names=("brayo","dan","king","anto")
marks=(98,95,94,93)
print(names)
print(marks)
#target a specific name or marks
print(names[2])
print(marks[0:4])
#target from a certain name/position or mark to the end of the list
print(marks[1:])
#print marks multiple times
print(marks*3)
#specified positions to appear
print(names[2],names[1])
print(marks+names)
#updating cannot happen in tuples
#the one below gives an error
# names[2]=joy
# print(names)