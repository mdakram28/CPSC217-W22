# Tutorial 8

---

### Date: Feb 6, 2021

### Email: mohdakram.ansari@ucalgary.ca

---

## Agenda

1. While loop
2. Flag based loops
5. Nested while loop

---
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

