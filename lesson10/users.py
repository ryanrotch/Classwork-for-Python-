from peewee import *
from os import path

ROOT =path.dirname(path.realpath(__file__))
db=SqliteDatabase(path.join(ROOT,"persons.db"))

class Person(Model):
    name=CharField()
    email=CharField(unique=True)
    age=IntegerField()
    password=CharField()
    class Meta:
        database=db

Person.create_table(fail_silently=True)
Person.create(name=input() , email=input(), age=input(), password=input())
# Person.create_table(fail_silently=True)
# Person.create(name="dave" , email="davwqee@gmail.com", age=21, password="08may1776")

user1=Person.get(id=1)
print(user1.name,user1.email,user1.age,user1.password)
user2=Person.get(id=2)
print(user2.name,user2.email,user2.age,user2.password)