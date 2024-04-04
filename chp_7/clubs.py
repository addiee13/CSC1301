students = ["Adam", "Riyan", "MAhean", "Parsa", "Ayuuhman"]
cs_club = ["Adam", "Riyan"]
math_club = ["Mahean"]
for student in students:
    if student not in cs_club and student not in math_club:
        print(student)