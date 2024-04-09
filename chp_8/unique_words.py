def clean(word):
    result = ""
    for char in word:
        if char.isalpha():
            result += char
    return result
            
with open("speech.txt", "r") as infile:
    data = infile.read()
    words = data.split()
    for word in (words):
        word = clean(word)
        # word = word.strip('"“”.,-')
        print(clean(word))
    print(f"The text has {len(set(words))} unique words.")
    
