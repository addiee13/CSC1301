##Says hello to the person
#   @param name the name to which it greets
#   
def greeting(name):
    print(f"Hello, {name}!")
name = input("Please enter your name: ")
greeting(name.title())
# OUTPUT
# Please enter your name: Addiee
# Hello, Addiee!