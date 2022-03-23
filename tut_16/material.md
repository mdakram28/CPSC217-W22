---
marp: true
---

# Tutorial 16

### Date: March 21, 2021

### Email: mohdakram.ansari@ucalgary.ca

---

## Agenda

1. Classes & Objects in Python

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
