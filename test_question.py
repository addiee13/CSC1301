# word = input("Enter a word: ")
# vowel = False
# i = len(word) - 1
# while i >= 0:
#     if word [i].lower() in "aeiouy":
#         print(f"There is a vowel at postion {i}")
#         vowel = True
#     i -= 1
# if vowel == False:
#     print(f"There are no vowels.")

# phrase = input("Enter a word: ")
# i = len(phrase) - 1
# is_vowel = False
# for char in phrase:
#     if char.lower() in "aeiouy":
#         is_vowel = True
# if is_vowel:
#     while i >= 0:
#         if phrase[i].lower() in "aeiouy":
#             is_vowel = True
#     i -= 1
# if is_vowel:
#     while i >= 0:
#         if phrase[i].lower() in "aeiou":
#             print(f"There is a vowel of psoi {i}")
#         else:
#             pass
#     i -= 1
# else:
#     print("No vowel")


inputstr = input("enter a sentence or a phrase: ")
uppervowel = 'AEIOU'
lowervowel = 'aeiou'
for i in range(0,len(inputstr)):
    if inputstr[1] in uppervowel or inputstr[i] in lowervowel:
        print(i)
