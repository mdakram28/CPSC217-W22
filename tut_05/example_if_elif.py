# Name: example_if_elif.py
# Author: Akram Ansari
# Tutorial : CPSC 217 T01/02
# Date: Jan 26, 2022

marks = int(input("Enter your final marks out of 100: "))
grade = ""

if marks > 90 and marks <= 100:
    grade = "A"
elif marks > 80 and marks <= 90:
    grade = "B"
elif marks > 70 and marks <= 80:
    grade = "C"
elif marks >= 0  and marks <= 70:
    grade = "D"
else:
    grade = "Invalid"

# Check if marks are within valid range
if marks >= 0 and marks <= 100:
    print("Calculated Grade : {0}".format(grade))
else:
    print("Marks should be between 0 and 100")
