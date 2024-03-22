numExams = int(input("Enter the number of subjects: "))
more_grades = "Y"
total = 0

while more_grades == "Y":
    total = 0
    min = 1000
    for i in range(1, numExams + 1):      
        grade = int(input("Enter a grade between 0 and 100: "))
        if grade < min:
            min = grade
        total += grade
    average = (total - min) / (numExams -1 )
    print(f"The average is {average:.1f}")
    more_grades = input("Do you want to add more grades: ").upper()
print("Thank you for using!")

# Enter the number of subjects: 3
# Enter a grade between 0 and 100: 100
# Enter a grade between 0 and 100: 100
# Enter a grade between 0 and 100: 0
# The average is 100.0
# Do you want to add more grades: y
# Enter a grade between 0 and 100: 34
# Enter a grade between 0 and 100: 45
# Enter a grade between 0 and 100: 2
# The average is 39.5
# Do you want to add more grades: n
# Thank you for using!