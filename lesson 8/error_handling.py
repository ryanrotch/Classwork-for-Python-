try:
    file=open("brio.txt","w")
    file.write("this is my file")

except IOError:
    print("error : Can't find file or read data ")
else:
    print("File created and written data successfully")
    file.close()

try:
    story=open("Tom and Jerry.txt","w")
    try:
        story.write("This is a very funny storybook \n"
                    "It details a cat and mouse scenario")
    finally:
        print("Successful. Closing file")

except IOError:
    print("Error: Can't find file or write data")

try:
    file=open("rotch.txt","w")
    file.write("this is simple")
except IOError:
    print("cant create file")
else:
    print("successful")