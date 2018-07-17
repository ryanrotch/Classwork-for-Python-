# using your own defined function, write a program to calculate
# 1. volume of a cylinder
# 2 area of a triangle
# 3. area of a circle
# note: get all the inputs from the user
#     -use math formulae

import math
def cylinder_volume(r,h):
    print("the volume of the cylinder is:",math.pi*math.pow(r,2)*h)
    return
print("please input the radius and height of the cylinder")
print("radius:\n")
r=int(input())
print("height:\n")
h=int(input())
cylinder_volume(r,h)

def triangle_area(b,h):
    print("the area of the triangle is:",1/2*b*h)
    return
print("please input the base and height of the cylinder")
print("base:\n")
b=int(input())
print("height:\n")
h=int(input())
triangle_area(b,h)

def area_circle(r):
    print("the area of the circle is:",math.pi*math.pow(r,2))
    return
print("please input the radius of the circle")
print("radius:\n")
r=int(input())
area_circle(r)