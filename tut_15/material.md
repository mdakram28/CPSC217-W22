# Tutorial 15

---

### Date: March 16, 2021

### Email: mohdakram.ansari@ucalgary.ca

---

## Agenda

1. File IO
2. Error Handling

---
## 1. File IO

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

1. Open a file
2. Read or write (perform operation)
3. Close the file


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

### Closing Files in Python

```python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```

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

### Exercise

Write a python program to read tic-tac-toe board from
a text file and print the content of box at some
row, column entered by the user.
