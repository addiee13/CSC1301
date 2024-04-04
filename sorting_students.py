parsa = {
    "name" : "Parsa",
    "age" : 19,
    "major" : "Computer Science"  
}
adam = {
    "name" : "Adam",
    "age" : 19,
    "major" : "Computer Science"  
}

john = {
    "name" : "John",
    "age" : 19,
    "major" : "Business"  
}
students = []
students.append(parsa)
students.append(adam)
students.append(john)

for student in students:
    if student["major"] == "Computer Science":
        print(student["name"])