f = open("inputFile.txt", "r")
passFile = open("PassFile.txt", "w")
failFile = open("FailFile.txt", "w")
# count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
        # print(line)
    elif line_split[2] == "F":
        failFile.write(line)
    # print(str(count) + line)
    # count = count + 1
f.close()
passFile.close()
failFile.close()
