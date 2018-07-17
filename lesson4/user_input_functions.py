import math

def area(radius):
    area=1/2*math.pi*math.pow(radius,2)
    print("the area of your circle is",area)
    return
print("enter radius")
radius=int(input())
area(radius)

def areas(radius):
    print("the area of your circle is",1/2*math.pi*math.pow(radius,2))
    return
print("enter radius")
radius=int(input())
areas(radius)