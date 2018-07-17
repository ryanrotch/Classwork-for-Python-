# Calculate the distances and areas of five circles respectively and display the output as:
    # 1.list
    # 2.tuples
    # 3.dictionary
# note: let distances be keys and ares to be values
# note: get input from the user
print("input the radius of the first circle")
r1=int(input())
area1=22/7*r1*r1
distance1=22/7*2*r1
print("input the radius of the second circle")
r2=int(input())
area2=22/7*r2*r2
distance2=22/7*2*r2
print("input the radius of the third circle")
r3=int(input())
area3=22/7*r3*r3
distance3=22/7*2*r3
print("input the radius of the fourth circle")
r4=int(input())
area4=22/7*r4*r4
distance4=22/7*2*r4
print("input the radius of the fifth circle")
r5=int(input())
area5=22/7*r5*r5
distance5=22/7*2*r5
print("output as a tuple")
area=(area1,area2,area3,area4,area5)
print( area)
print("output as a dictionary")
area={r1:area1,r2:area2,r3: area3 ,r4: area4,r5:area5}
print(area)
print("output as a list")
area=[area1,area2,area3,area4,area5]
print(area)
print("UPDATE a selection in the list")
area[1]=2000
print(area)
print("output as a tuple")
distance=(distance1,distance2,distance3,distance4,distance5)
print(distance)
print("TARGETING A SPECIFIC OUTPUT")
print(distance[1:3])
print("output as a list")
distance=[distance1,distance2,distance3,distance4,distance5]
print(distance)
print("output as a dictionary")
circleDetails={r1:distance1,r2:distance2,r3:distance3,r4:distance4,r5:distance5}
print(circleDetails)
print(circleDetails.keys())
print(circleDetails.values())
