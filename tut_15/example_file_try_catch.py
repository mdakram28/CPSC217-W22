import sys

try:
    f = open("non_existent_file.txt", 'r')
    line = f.readline()
    print(line)
    f.close()
except OSError:
    print("Some error occurred during opening file")
    sys.exit(1)
