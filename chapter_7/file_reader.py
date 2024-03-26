infile = open("fruits.txt", "r")
# line = infile.readline()
# while line != "":
#     print(line, end="")
#     line = infile.readline()
# ------------------------------------
# Alternate way of reading file

for line in infile:
    line = infile.readline()
    print(line)
    
infile.close()