# Name: example_if.py
# Author: Akram Ansari
# Tutorial : CPSC 217 T01/02
# Date: Jan 26, 2022
# Description: Example of if statement in python

marks = int(input("Enter your final marks out of 100: "))
grade = ""

if marks > 90 and marks <= 100:
    grade = "A"
if marks > 80 and marks <= 90:
    grade = "B"
if marks > 70 and marks <= 80:
    grade = "C"
if marks >= 0  and marks <= 70:
    grade = "D"

# Check if marks are within valid range
if marks >= 0 and marks <= 100:
    print("Calculated Grade : {0}".format(grade))
else:
    print("Marks should be between 0 and 100")
