class Firefox:
    """This class is accepting input from the user and giving output""" #this is a doc-string to give help or guide user of the program
    def __init__(self,computer1,computer2):#function that accepts two parameters
        self.comp1Name=computer1
        self.comp2Name=computer2
print("Enter table 1 computer names ")
table1=Firefox(str(input()),str(input()))
print("Enter table 2 computer names ")
table2=Firefox(str(input()),str(input()))
print("the table 1 computers are:")
print(table1.comp1Name)
print(table1.comp2Name)
print("the table 2 computers are:")
print(table2.comp1Name)
print(table2.comp2Name)

help(Firefox)