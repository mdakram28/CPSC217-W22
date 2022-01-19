# Tutorial 3

---

### Date: Jan 19, 2021

### Email: mohdakram.ansari@ucalgary.ca

---

### Agenda

1. Exercises in Pycharm
2. Intro to python (variables/expressions/IO)
3. Exercise of getting input/casting/math/print
4. Introduction to Assignment 1

---

### 1. Exercises in PyCharm (Optional)

PyCharm Edu has some interactive courses which give you exercises to practice programming concepts.

For opening the interactive learning course. 

1. Click on `File` in the toolbar. 
2. Goto `learn` > `Browse Crouses`. 
3. Select a course from the list and click on `start` button on the right panel.

---

### 2. Intro to python

	1. **Variables**

    - Variables allow us to store some data in the computers memory for later use.

    - Variables are created with a name and can be accessed using that name later in the code. e.g.:

      ```python
      my_variable = 123
      ```

    - Variables are destroyed when the program terminates

    - Variables can hold data of different types. eg:

      ```python
      # Integer 
      a = 5
      # Floating Point
      b = 3.12
      # String
      s = "Custom String"
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
      print("Welcome to CPSC 217")
      print("The user's name is", user_name)
      ```

	4. **Casting**

    - In order to convert from one data type to another we use casting functions in python: **int(), float(), str(), bool()**, etc

    - When we call the input() function, it evalutes to a string data type. If we need to take in floating point input we will have to wrap the input() function inside a float() casting function. e.g.:

      ```python
      number = float(input("Enter a number"))
      ```

      

---

### 3. Exercise

Write a python program to 

1. Get the current temperature in farenheit from the user
2. Convert it to celcius
3. Print the converted temperature

$$
C = \frac{(F - 32) * 5}{9}
$$



---

### 4. Intro to Assignment 1

D2l > CPSC 217 > Content > Assignment 1