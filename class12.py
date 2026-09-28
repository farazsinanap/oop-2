class Outer:
    def __init__(self):
        self.name = "outer class"
    class Inner:
        def __init__(self):
            self.name = "inner class"
        def display(self):
            print("hello from inner class")

ou = Outer()
inn = ou.Inner()
inn.display()              