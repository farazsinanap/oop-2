class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
class Student(Person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id = id

s1 = Student("leo",21,17)

print(s1.name,s1.age,s1.id)