students = set(["Adam", "Riyan", "Mahean", "Parsa", "Ayushman"])
cs_club = set(["Adam", "Riyan"])
math_club = set(["Mahean"])

'''Checks whether name is in class'''
# name = "Adam"
# if name in students:
#     print(f"{name} is in the class.")

'''Prints the students not in CS Club'''
for student in students.difference(cs_club):
    print(student)