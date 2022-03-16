# This program calculates average grade for each course

try:
    f = open("grades.txt", "r")

    total_per_course = [0, 0, 0, 0, 0]
    num_students = 0

    # Read first students grade
    grades = f.readline()
    while grades != "":
        num_students += 1
        for col in range(0, 10, 2):
            grade = int(grades[col])
            total_per_course[col//2] += grade
        # Read next student's grade
        grades = f.readline()

    # Print Average grade of each subject
    for course in range(5):
        avg = total_per_course[course]/num_students
        print("Average of Course {} = {}".format(course+1, avg))

    f.close()
except OSError:
    print("Failed to open file")
