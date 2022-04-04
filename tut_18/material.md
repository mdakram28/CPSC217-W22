---
marp: true
---

# Tutorial 18

### Date: April 04, 2021

### Email: mohdakram.ansari@ucalgary.ca

---

## Agenda

1. Classes & Objects in python
2. Special functions
   1. `__str__`
   2. `__lt__`
   3. `__eq__`
    
---

## 1. Classes & Objects in python

An object is simply a collection of data (variables) and methods 
(functions) that act on those data. Similarly, a class is a blueprint 
for that object.

**Defining a Class in Python**

```python
class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
```

---
**Example**

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)
```

---
**Creating an Object in Python**

```python
travis = Person()
```

---
**Example**

```python
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Another One')

# create a new object of Person class
drake = Person()

# Calling object's greet() method
# Output: Hello
drake.greet()
```

---
### Constructors in Python

`__init__()` function: This special function gets called 
whenever a new object of that class is instantiated.

---
**Example**

```python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
num2 = ComplexNumber(5)

# Output: 5 0
print(num2.real, num2.imag)
```

---

## 2. Special functions

### `__str__`

The `__str__` method in Python represents the class objects as a string – 
it can be used for classes. 

The `__str__` method is called when the following functions are invoked on the object and return a string:

    print()
    str()

```python
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

myObject = MyClass(12345, "Hello")

print(myObject.__str__())
# <__main__.MyClass object at 0x7fafc20d81f0>
print(myObject)
# <__main__.MyClass object at 0x7fafc20d81f0>
```

**Custom `__str__` method**

```python
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        return 'MyClass(x={} ,y={})'.format(self.x, self.y)

myObject = MyClass(12345, "Hello")

print(myObject.__str__())
# MyClass(x=12345 ,y=Hello)
print(myObject)
# MyClass(x=12345 ,y=Hello)
print(str(myObject))
# MyClass(x=12345 ,y=Hello)
```

### `__lt__`

**`__lt__` is a special method that describes the less-than operator in python.**

We can define it as follows:

    `__lt__`(self, other)

```python
class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def area(self):
        return self.w * self.h
    def __lt__(self, other):
        return self.area() < other.area()

a = Rectangle(2,5)
b = Rectangle(3,4)

print(a<b)
# True
```

### `__eq__`

**`__eq__` is a special method that describes the equal-to operator in python.**

We can define it as follows:

    `__eq__`(self, other)

```python
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
```
