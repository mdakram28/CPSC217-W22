# Name: exercise_leap.py
# Author: Akram Ansari
# Tutorial : CPSC 217 T01/02
# Date: Jan 26, 2022

year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0):
    print("It is leap year")
else:
    print("It is not leap year")
