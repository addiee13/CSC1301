with open("name.txt", "r") as infile:
    data = infile.read()

lines = data.splitlines()

for line in lines:
    print(line.strip(" .?"))