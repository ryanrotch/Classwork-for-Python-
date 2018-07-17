# applying concepts learnt, design a virtual login system
# with input from the user
# considering the following rules
#   1.password must  be eight or more characters
#   2.on successful login allow the user  to implement calculator operations by
#    inputting two values and specify the operation to be performed
#   3.print the answer
print("USERNAME:")
USERNAME=str(input())
print("PASSWORD")
PASSWORD=str(input())
# print(len(PASSWORD))

if len(PASSWORD)<8:
    print("the PASSWORD is too short")
    print("please add more characters")
else:
    print("login successful")
    print("enter the first number")
    f1=int(input())
    print("enter the second number")
    f2=int(input())
    print("Enter an operation sign")
    operant=str(input())
if operant== "-":
    dif = f1-f2
    print(dif)
elif operant== "+":
    total = f1+f2
    print(total)
elif operant== "*":
    mult = f1*f2
    print(mult)
elif operant== "/":
    div = f1/f2
    print(div)
