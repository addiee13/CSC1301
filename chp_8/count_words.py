with open("mary.txt", "r") as infile:
    data = infile.read()
    words = data.split()
    for word in sorted(set(words)):
        count = 0
        count += words.count(word)
        print(f"{word} : {count}")
            