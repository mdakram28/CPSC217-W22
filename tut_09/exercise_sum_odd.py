# Can you write a program to find the sum of odd numbers from 1 to 99.
# Result should be equal to:
# result = 1 + 3 + 5 + 7 + ... + 97 + 99

result = 0
for i in range(1, 100, 2):
    result += i

print("Sum of odd numbers from 1 to 99: {}".format(result))
