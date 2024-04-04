## Simple dictionary statements
#
gradeCounts = { "C": 10, "A": 6, "B": 7, "D": 1, "F": 3 }
print("The keys: ")
for key in gradeCounts.keys():
    print(key)
print()
print("The values: ")
for value in gradeCounts.values():
    print(value)
print()
print("The key and value pairs: ")
for key, value in gradeCounts.items():
    print(f"{key}: {value}")
print()
print("The ordered key an value pairs: ")
for key, value in sorted(gradeCounts.items()):
    print(f"{key}: {value}")
