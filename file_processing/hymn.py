with open("hymn.txt", "r") as infile:
    for line in infile:
        words = line.rstrip().split()
        previous = ""
        for word in words:
            if word != previous:
                print(word,end=" ")
                previous = word