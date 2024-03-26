# strip() function removes emptyh whitespace from a string
greeting = "   Hello    "
name = "   Adam"
name2 = "Parsa"
# Normal print
print(greeting)

# Prints without space
print(greeting.strip())

# lstrip() and rstrip() remove whitespace only from left or right
print(name.lstrip())

# strip() can also remove characters at extremes mentioned as arguments
print(name2.strip("P"))