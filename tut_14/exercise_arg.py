import sys

num_args = len(sys.argv) - 1
total = 0

for i in range(1, num_args+1):
    total += int(sys.argv[i])

average = total / num_args

print("Average = {}".format(average))
