with open("name.txt", "r") as infile:
    for line in infile:
        print(line.strip(" \n.?"), " Hello!")