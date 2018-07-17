number =0
while number<=10:
    print("The numbers are ", number)
    number+=1

while number>10 and number <=20:
    print(number)
    number+=1
    pass


for characters in "Python":
    print(characters)
#prints the letters based on positions 0,1,2 etc. as in a list format

for names in ["KIng","Dan","Brio","Lesson"]:
    print(names)
fruits=["mango","pineapple","orange","juice","avocado"]
for item in fruits:
    if len (item) ==5:
      print(item)
      print(item.upper())