# q4
# Write a python program to implement  a login system and hence,
#  implement a python calculator. Define the login system on an external module on a function
# Note:all inputs from the user

from login import log

print("ENTER TWO VALUES TO BE CALCULATED:")

a=int(input())
b=int(input())
sum=(a+b)
division=(a/b)
multiplication=(a*b)
subtraction=(a-b)
print("SUM:\t",sum)
print("SUBTRACTION\t",subtraction)
print("DIVISION\t",division)
print("MULTIPLICATION\t",multiplication)