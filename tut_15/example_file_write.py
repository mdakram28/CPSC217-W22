# Read lines from user and write to a file until the users enters q

try:

    line = input("Enter line [q to exit]: ")
    f = open("user_message.txt", "w")
    while line != "q":
        f.write(line)
        f.write("\n")
        line = input("Enter line [q to exit]: ")
    f.close()

except OSError:
    print("Failed to open file for writing")
