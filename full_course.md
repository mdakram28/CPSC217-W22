# Introduction
### Author - Akram Ansari (https://mdakram.com/)

I teach Python to university students. This article is meant to teach the basics to programming using python to an absolute beginner with no programming experience. After following this article you will be able to understand and write your own intermediate level python code.

The source code for the examples and exercise solutions can be found in the repo: https://github.com/mdakram28/CPSC217-W22.

### How to follow the course?
Try to run the code given as examples and also attempt to solve the exercises. Complete a minimum of 1 chapter per day. Do not. Cover the material at the suggested pace along with exercises to get maximum retention of the concepts.


# Table of Contents

1. Tutorial 1: Setup
2. Tutorial 2: Getting Started
    1. Running python code
3. Tutorial 3: Intro to Python
    1. Exercises in PyCharm (Optional)
    2. Variables, Expressions, IO & Casting
    3. Exercise
4. Tutorial 8: While Loop
    1. While Loop
    2. Flag based loop
    3. Nested while loop
5. Tutorial 9: Sequence & For Loop
    1. Sequence
    2. For Loop
    3. Nested for loop
    4. Exercise
6. Tutorial 10: Comments and Functions
    1. Commenting Best Practices
    2. Functions
    3. Main Function
    4. Exercise
7. Tutorial 12: Dictionaries and Lists
    1. Dictionaries
    2. Lists
8. Tutorial 14: Command Line Arguments
    1. Running a python file from the terminal
    2. Taking arguments from the terminal
    3. Exercise
9. Tutorial 15: File I/O and Error Handling
    1. File I/O
    2. Error Handling
    3. Exercise
10. Tutorial 16: Object Oriented Programming
    1. Classes & Objects
11. Tutorial 17: Tic-Tac-Toe
12. Tutorial 18: Special Class Function

# Tutorial 1: Setup

## 1. Setup

### Installing Pycharm Edu

> **IDE:** An integrated development environment (IDE) is software for building applications that combines common development tools into a single graphical user interface (GUI).
>
> <small>- https://www.redhat.com/en/topics/middleware/what-is-ide</small>
>
> Example: Idle, **PyCharm**

1. https://www.jetbrains.com/edu-products/download/#section=pycharm-edu

### Installing Python 3

1. https://www.python.org/downloads/

---












# Tutorial 2: Getting Started

## 1. Running python code

Type your code in the .py file.

```python
print("Hello World")
```

#### PyCharm

1. Click on the green play button on the top left of your code window.
   A tab will open at the bottom of the IDE with the output of your program, or errors if any.

#### PyCharm Terminal

1. Click on the tab `Terminal` at the bottom of the IDE
   A prompt will open up where we will type the commands
2. Type `python main.py` and press enter.
   The output of your program will be printed on the terminal

#### Outside PyCharm (Optional)

1. Right Click on the project name in the left sidebar
2. Go inside `Copy Path/Reference` in the dropdown
3. Click on Absolute Path
   The location of your project would be copied to your clipboard
4. Open Terminal (on Mac) or CMD (on Windows) from the start menu
5. Type `cd <space>` and paste your path after the space and press enter.
   You would now be inside your project directory
6. Type `python main.py` and press enter.
   The output of your program will be printed on the terminal

---













# Tutorial 3: Intro to Python

## 1. Exercises in PyCharm (Optional)

PyCharm Edu has some interactive courses which give you exercises to practice programming concepts.

For opening the interactive learning course. 

1. Click on `File` in the toolbar. 
2. Goto `learn` > `Browse Crouses`. 
3. Select a course from the list and click on `start` button on the right panel.

---

## 2. Intro to python

1. **Variables**

  - Variables allow us to store some data in the computers memory for later use.

  - Variables are created with a name and can be accessed using that name later in the code. e.g.:

    ```python
    my_variable = 123
    my_variable = 456
    ```

  - Variables are destroyed when the program terminates

  - Variables can hold data of different types. eg:

    ```python
    # Integer 
    a = 5
    # Floating Point
    b = 3.12
    # String
    s = "1.234"
    s_as_num = float(s)
    ```

2. **Expressions**

   - An expression is a combination of values, variables, operators, operands, and calls to functions which evaluate to some result during execution.
   - Expressions can appear at the right hand side of variable assignment. In that case the result of the expression is stored in the variable.
   - Operators: +, -, *, /, ** (exponentiation), // (integer division), % (remainder)
   - e.g.
     - `1+2`
     - `(2*a) + (3*b)`

3. **IO**

   - Input: Take input from the user using the in built input() function. e.g.:

     ```python
     user_name = input("Enter your name")
     ```

   - Output: Print using the in built print() function. e.g.: 

     ```python
     print("Welcome to CPSC 217", "Good Morning")
     print("The user's name is", user_name)
     ```

4. **Casting**

   - In order to convert from one data type to another we use casting functions in python: **int(), float(), str()**, etc

   - When we call the input() function, it evalutes to a string data type. If we need to take in floating point input we will have to wrap the input() function inside a float() casting function. e.g.:

     ```python
     number = float(input("Enter a number"))
     ```

---

### 3. Exercise

Write a python program to 

1. Get the current temperature in fahrenheit from the user
2. Convert it to celsius
3. Print the converted temperature

$$
C = \frac{(F - 32) * 5}{9}
$$

**Solution**

```python
# 1. Get the current temperature in fahrenheit from the user
temp_f = float(input("Enter the temperature in fahrenheit: "))
# 2. Convert it to celsius
temp_c = ((temp_f - 32) * 5) / 9
# 3. Print the converted temperature
print("Temperature in celsius:", temp_c)
```

---










# Tutorial 8: Loops

## 1. While Loop

*With the while loop we can execute a set of statements as long as a condition is true.*

**Example**

Print i as long as i is less than 6:

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

**Output**

```
1
2
3
4
5
```



### The break Statement

*With the break statement we can stop the loop even if the while condition is true:*

**Example**

Exit the loop when i is 3:
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
```
**Output**

```
???
```

**Example**

*An input loop terminated when user enters "q"*

```python
power = 5

while power > 0:
    print("Available power : {0}".format(power))
    user_choice = input("Press enter to proceed or q to quit")
    if user_choice == "q":
        break
    power -= 1

print("Game Over")
```





---
## 2. Flag based loop

We can use a boolean variable in place of the boolean expression in a while loop. The value of the boolean variable will be checked each time before loop executes.

**Example**

*Flag based loop to print first 5 positive integers*

```python
flag = True
i = 1
while flag:
    print(i)
    if i == 5:
        flag = False
    i += 1
```

**Output**
```
1
2
3
4
5
```


---
## 3. Nested while loop

Python programming language allows the use of a while loop inside another while loop.

The syntax of the nested- while loop in Python as follows:

**Syntax**
```python
while expression:
    ...					# Outer Loop
    while expression:
        ...				# Inner Loop
    ...					# Outer Loop
```

---



**Example**

```python
i=1
while i<=3 :
    print("i = {0}".format(i))
    j=1
    while j<=3:
        print("    j = {0}".format(j))
        j+=1
    i+=1

```

---












# Tutorial 9: Sequence & For Loop

## 1. Sequence

A sequence in python is a <mark>collection of items in an order</mark>.

**Strings**

```python
# A String (sequence of characters)
text = "Python"
print(list(text))
```

| 'P'  | 'y'  | 't'  | 'h'  | 'o'  | 'n'  |
| ---- | ---- | ---- | ---- | ---- | ---- |

**List** *(more on this later)*

```python
# A list of languages
languages = ["English", "French", "Spanish"]
print(languages)
```

| "English" |  "French" | "Spanish" |
| --- | --- |-----------|

**Range**

Range in python is used for generating a sequence of integers.

**Syntax**

```python
range(start, stop, step)
```

Note: The start is optional with a default value of 0. Step is optional with a default value of 1

**Example**

```python
# A range of numbers from 0 to 9
numbers = range(0, 10)
print(list(numbers))
```

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |-----|

**Examples**

```python
# empty range
print(list(range(0)))
# Output: []

# using range(stop)
print(list(range(10)))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# using range(start, stop)
print(list(range(5, 10)))
# Output: [5, 6, 7, 8, 9]

# using range(start, stop, step)
print(list(range(1, 10, 2)))
# Output: [1, 3, 5, 7, 9]

# Negative step
print(list(range(2, -2, -1)))
# Output: [2, 1, 0, -1]

# Bad range
print(list(range(2, -2)))
# Output: []
```

---
## 2. For loop

A for loop is used to iterate over a sequence.

**Syntax**

```python
for variable in sequence:
    # loop body
```

**Example**

```python
# Print numbers from 0 to 9

# Using while loop
i = 0
while i < 10:
    print(i)
    i += 1

# Using for loop
for i in range(0, 10):
    print(i)
```

**Example**

Print the multiplication table of a number entered by the user

```python
number = int(input("Enter an integer: "))

# Count from 1 to 10
for count in range(1, 11):
    product = number * count
    print("{0} x {1} = {2}".format(number, count, product))
```

**Example**

Write a program to check whether an integer entered by the user is prime or not.

```python
number = int(input("Enter an integer: "))

# The number is assumed to be prime
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

# Print result
if is_prime == True:
    print("PRIME")
else:
    print("COMPOSITE")

```



---

## 3. Nested for loop

We can write a for/while loop inside the body of another for/while loop. This is known is nesting of loops.

**Example**

Print prime numbers from 1 to 99

```python
# 1 is not a prime number
for number in range(2, 100):
    # The number is assumed to be prime
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    # Only print the number if it is prime
    if is_prime == True:
        print("{} is a prime number!".format(number))
```



#### 4. Exercise

Can you write a program to find the sum of odd numbers from 1 to 99.

Result should be equal to:

*result = 1 + 3 + 5 + 7 + ... + 97 + 99*

**Solution**

```python
result = 0
for i in range(1, 100, 2):
    result += i

print("Sum of odd numbers from 1 to 99: {}".format(result))
```

**Extra**

Python is pretty powerful and has handy utilities that can make your program much compact.

The above program can be written in just 1 line! Pretty cool right?

```python
print(sum(range(1, 100, 2)))
```

---





















# Tutorial 10: Comments and Functions

## 1. Commenting Best Practices

To write a comment in Python, simply put the hash mark # before your desired comment:

```python
# This is a comment
```

Python ignores everything after the hash mark and up to the end of the line. 
You can insert them anywhere in your code, even inline with other code:

```python
print("This will run.")  # This won't run
```

Tip: Comments should be short, sweet, and to the point.

#### Multiline comments

If you don't want to put a `#` at the start of each line in a multiline comment,
you can enclose your comment lines in tripple quote (single or double).

```python
"""
If I really hate pressing `enter` and
typing all those hash marks, I could
just do this instead
"""
```

#### Indented Comments

Have your comments indented at the same level as your code

```python
# Do This
if grade == 4:
    # Perfect grade
    print("Congratulation!")

# Do Not This
if grade == 4:
# Perfect grade
    print("Congratulation!")
```


#### Commenting Shortcut in PyCharm
Clicking each and every line to comment it out could take a lot of time! 
In these cases, you’ll want to toggle comments instead. 
Simply select the desired code and press `Ctrl`+`/` on PC, or `Cmd`+`/` on Mac:


---

## 2. Functions

#### What is a function in Python?

In Python, a function is a group of related statements that perform a specific task.

Syntax of Function
```python
def function_name(parameters):
    """docstring"""
    statement(s)...
```

Example:
```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
```

#### How to call a function in python?
Once we have defined a function, we can call it from another function, program, 
or even the Python prompt. 
To call a function we simply type the function name with appropriate parameters.

Example:
```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

# This is how you call a function
greet('Paul')
```

#### The `return` Statement

The return statement is used to exit a function and go back to the place from where it was called.

Syntax:
```python
return [expression_list]
```

Example:
```python
def compound_interest(principal, rate, time):
    """This function will return the compound interest on the principal amount"""
    amount = principal * (pow((1 + rate / 100), time)) 
    interest = amount - principal
    return interest 

amount = float(input("Enter the invested amount"))
rate = 14
years = 8
ci = compound_interest(amount, rate, years)
print("{0} will yield an interest of {1:.2f} in {2} years".format(amount, ci, years))
```

We can also return more than 1 value using the return statement

Example:
```python
def add(num1, num2):
    total  = num1 + num2
    return 'SUM', total, [num1, num2]

a, b, c = add(5, 6)

print(a)
# SUM
print(b)
# 11
print(c)
# [5, 6]
```

You can also have multiple return statements in your code

Example:
```python
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))
```

#### Exercise

Convert the program to print all prime numbers to use the function.
Create the function to check if a number is prime or not if needed.

Starting code: `tut_09/example_for_all_primes.py`


---

## 3. Main Function

It is a best practice in python to start your program from the main function.

Example:
```python
def add(a, b):
    return a+b

def main():
    print("Total of 2 and 3 is", add(2,3))

main()
```

---

## 4. Exercise

*<small>Do not use any inbuilt function</small>*

Define a function that accepts 3 numbers are arguments and returns the maximum of the three numbers.
Test your function using combination of different values from the main function.

```python
def maximum(a, b, c):
    """This function returns the max of a,b,c"""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def main():
    print(maximum(10,22,14))
    print(maximum(100,-22,14))
    print(maximum(0,0,1))

main()
```
---



















# Tutorial 12: Dictionaries

## 1. Dictionaries

### Creating Python Dictionary

Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.

```python
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

---

### Accessing Elements from Dictionary

Keys can be used either inside square brackets [] or with the get() method.

```python
# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])
```

### Changing and Adding Dictionary elements

Dictionaries are mutable. We can add new items or change the value of existing items 
using an assignment operator.

```python
# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
```

### Checking if dictionary has a key

Use the `in` and `not in` operator to check if dictionary has a key.

```python
numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
 
print("one" in numbers)
print("one" not in numbers)
 
print(3 in numbers)
print(3 not in numbers)
 
print(5 in numbers)
print(5 not in numbers)
```

### Exercise

Make a program to count the number of each letter in a word entered by the user.
Print the frequency as a dictionary

```python

frequency = {}
word = input("Enter a word ")
for letter in word:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)

```

## 2. Lists

A list in python is a sequence of zero or more elements of any data type (including lists itself).
```python
# a list of programming languages
['Python', 'C++', 'JavaScript']
```

### Create Python Lists

A list is created by placing elements inside square brackets [], separated by commas.

```python
# list of integers
my_list = [1, 2, 3]

# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
```

### Access List Elements

We can use the index operator [] to access an item in a list. In Python, indices start at 0.

```python
my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
nested_list = [["queen", "king", "joker"], [2, 0, 1, 5]]

# Nested indexing
print(nested_list[0][1])

print(nested_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])
```

### Add/Change List Elements

We can use the assignment operator = to change an item.

```python
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            
# odd: [1, 4, 6, 8]

# Add an item
odd.append([999, 55])
# odd: [1, 4, 6, 8, [999, 55]]
```

### Iterating Through a List

```python
fruits = ['apple','banana','mango']
for fruit in fruits:
    print(fruit)

length = len(fruits)
for i in range(len(fruits)):
  print(fruits[i]) 

```

---


























# Tutorial 14: Command Line Arguments

## 1. Running a python file from the terminal

1. Open a terminal
   1. PyCharm Integrated Terminal
   2. Cmd (Windows) / Terminal (MacOS)
2. Go in the directory where your python file is.
   1. Type `pwd` to print the current working directory.
   2. For changing directory type `cd <directory>`
3. Type `python <my_python_file.py>` (with the extension)

![img.png](img.png)
---
## 2. Taking arguments from the terminal

When running a python file from the terminal you can pass 
input to your program as arguments.

Sytax
```commandline
python my_file.py <arg_1> <arg_2> <arg_3> ...
```

The arguments can be accessed inside your program using 
`sys.argv` pre-created list. Make sure you have `import sys`
line before you access `sys.argv`.

The first element of this list is the python file name.

The next elements of this list are space separated arguments 
passed to the program.

All arguments are of the str type.

Example:
```python
import sys
print(sys.argv)
```

Output:
```commandLine
$ python example_arg.py arg 1234 test 43.0
['example_arg.py', 'arg', '1234', 'test', '43.0']
```

---
## 3. Exercise

Write a program to calculate the average of all 
numbers passed as argument to the python program.
Expect all arguments to be integers.

```python
import sys

num_args = len(sys.argv) - 1
total = 0

for i in range(1, num_args+1):
    total += int(sys.argv[i])

average = total / num_args

print("Average = {}".format(average))

```

---















# Tutorial 15: File I/O and Error Handling

## 1. File IO

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

1. Open a file
2. Read or write (perform operation)
3. Close the file

---
### Opening Files in Python


```python
f = open("test.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path

f = open("test.txt",'w')  # write in text mode
```

**Modes**

1. `r`: Opens a file for reading. (default)
2. `w`: Opens a file for writing. 
Creates a new file if it does not exist or truncates the file if it exists.

---
### Closing Files in Python

```python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```

---
### Writing to Files in Python

```python
# Open
f = open("test.txt",'w')
# Perform File IO
f.write("my first file\n")
f.write("This file\n\n")
f.write("contains three lines\n")
# Close
f.close()
```

---
### Reading Files in Python

```python
f = open("test.txt",'r')
line = inputFile.readline() # Read whole line as a str

# Go Over all lines in file
for line in f:
    print(line, end = '')
```
> In this program, the lines in the file itself include a newline character \n. 
> So, we use the end parameter of the print() function to avoid two newlines when printing.

---
## 2. Error Handling

Python uses the try-except-finally block to control exceptions.

Without Exception Handling
```python
print(6/0) # This will crash the code
print("This will not be printed")
```

With Exception Handling
```python
try:
    print(6/0)
    print("This will not be printed")
except:
    print("An error occurred")

print("This will always be printed")
```

---
### Handling file IO errors

File IO can crash due to many reasons.
Surround File IO inside a try-except block

```python
import sys

try:
    f = open("non_existent_file.txt", 'r')
    line = f.readline()
    print(line)
    f.close()
except OSError:
    print("Some error occurred during opening file")
    sys.exit(1)

```
---
## 3. Exercise

Write a python program to read tic-tac-toe board from
a text file and print the content of box at some
row, column entered by the user.


```python
try:
    f = open("tic-tac-toe.txt", "r")

    r = int(input("Enter row: "))
    c = int(input("Enter column: "))

    line = ""
    for i in range(r):
        line = f.readline()

    box = line[c-1]
    print("Content of box at {},{} : '{}'".format(r, c, box))

    f.close()
except OSError:
    print("Failed to open file")

```

---












# Tutorial 16: Object Oriented Programming

## 1. Classes & Objects

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







# Tutorial 17: Tic-Tac-Toe

### Setup

Install the library `PySimpleGUI` using pycharm.

---

### Problem

1. Start from file `ttt_gui_starter.py` from D2L.
2. Complete the function `check_player_won()`. Return "X" or "O" if
a player has won the game. Return None otherwise.
3. The board state is stored in the 2D list `board`. Each element of the
2D list is either "X" or "O" or " ".

---

### Solution

`ttt_gui.py` on D2L.

---






















# Tutorial 18: Special Class Function

## 1. Special functions

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
---