class Person:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age
    def get_age(self):
        return self.__age 
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("age must be positive")


p1 = Person("leo",21)
print(p1.name)
print(p1.get_age())


p1.set_age(23)
print(p1.get_age())
        