class Student:
    def __init__(self,name,mark):
        self.name = name 
        self.__mark = mark 
    def get_mark(self):
        return self.__mark
    def get_status(self):
        if self.__mark >= 40:
            return "passed"
        else:
            return "failed"


s1 = Student("leo",97)
print(s1.name)
print(s1.get_mark())
print(s1.get_status())      