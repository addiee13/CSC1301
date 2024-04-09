def clean(word):
    result = ""
    for char in word:
        if char.isalpha():
            result += char
    return result
            
with open("speech.txt", "r") as infile:
    data = infile.read()
    words = data.split()
    for word in set(words):
        word = clean(word)
        # word = word.strip('"“”.,-')
        print(word)
    print(f"The text has {len(set(words))} unique words.")
    
