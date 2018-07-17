class User:
    pass
user1=User()
user1.first_name="brio"
user1.second_name="rotich"
user1.age=21
user1.hobby="gaming"
pass
user2=User()
user2.first_name="dan"
user2.second_name="anto"
user2.job="guru"
user2.hobby="writer"
print(user1.first_name,user1.second_name,user1.age,"loves",user1.hobby)
print(user2.job,user2.hobby,user2.first_name,user2.second_name)

class Student:
    def __index__(self,full_name,birthday):
        self.name=full_name
        self.birthday=birthday
Student=Student("brio rotich","19-4-2001")
print(Student.full_name)
print(Student.birthday)


