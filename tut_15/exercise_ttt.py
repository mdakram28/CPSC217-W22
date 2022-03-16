
try:
    f = open("tic-tac-toe.txt", "r")

    r = int(input("Enter row: "))
    c = int(input("Enter column: "))

    line = ""
    for i in range(r):
        line = f.readline()

    box = line[c-1]
    print("Content of box at {},{} : '{}'".format(r, c, box))

    f.close()
except OSError:
    print("Failed to open file")
