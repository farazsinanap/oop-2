class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age

p1 = Person("leo",21)
print(p1.name)