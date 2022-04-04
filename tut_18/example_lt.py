class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def area(self):
        return self.w * self.h
    def __lt__(self, other):
        return self.area() < other.area()
    def __eq__(self, other):
        return self.area() == other.area()

a = Rectangle(2,5)
b = Rectangle(3,4)
c = Rectangle(2,6)

print(a<b)
# True
print(a==b)
# False
print(b==c)
# True
