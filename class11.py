class Outer:
    def __init__(self):
        self.name = "outer class"

    class Inner:
        def __init__(self):
            self.name = "inner class"
        def display(self):
            print("this is inner class")

out = Outer()
print(out.name)