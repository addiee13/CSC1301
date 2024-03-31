with open("poem.txt", "r") as infile:
    with open("poem_result.txt", "w") as outfile:
        for line in infile:
            words = line.split()
            for word in words:
                word = word.rstrip(" .?,.")
                print(word, file=outfile)