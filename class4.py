class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
class Student(Person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.year = year

    def greetings(self):
        print("welcome mr.",self.name,"to the class of year ",self.year)


s1 = Student("leo",21,2024)


print(s1.name,s1.age)

s1.greetings()