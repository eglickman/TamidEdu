hello =5
print(hello)
hello = "Hello World"
class TestClass:
    def __init__(self, age, name):
        self.x = age
        self.y = name
    def __str__(self):
        return f"{self.x} is the age of {self.y}"
    def exFunc(self):
            print("My name is", self.y, "and I'm", self.x, "years old.")
t = TestClass(19, "Ethan")
print(hello)
print(t.x, t.y)
print(t)
t.exFunc()