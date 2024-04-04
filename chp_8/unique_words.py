def clean(word):
    result = ""
    for char in word:
        if char.isalpha():
            result += char
    return result
            
with open("speech.txt", "r") as infile:
    for line in infile:
        words = line.split()
    for word in set(words):
        word = clean(word)
        # word = word.strip('"“”.,-')
        print(word)
    print(f"The Gettysburg Address has {len(set(words))} unique words.")
    
