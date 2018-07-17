#
# print("area of the first circle is:",area1)
# print("the circumference of the first circle is:",distance1)
#
# print("area of the second circle is:",area2)
# print("the circumference of the second circle is:",distance2)
#
# print("area of the third circle is:",area3)
# print("the circumference of the third circle is:",distance3)
#
# print("area of the fourth circle is:",area4)
# print("the circumference of the fourth circle is:",distance4)
#
# print("area of the fifth circle is:",area5)
# print("the circumference of the fifth circle is:",distance5)
f1 = int(input())
print("enter the second number")
f2 = int(input())
add = f1 + f2
multiply = f1 * f2
divide = f1 / f2
subtract = f1 - f2
print("select an operant to be used from add,multiply,divide or subtract")
operant = str(input())
if operant == add:
    print(add)
elif operant == multiply:
    print(multiply)
elif operant == divide:
    print(divide)
elif operant == subtract:
    print(subtract)
