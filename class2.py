class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def printname(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self,name,age)
s1 = Student("rason",23)

s1.printname()