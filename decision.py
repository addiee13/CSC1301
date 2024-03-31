# # Python equivalent of the Java program to check voting eligibility based on age

# # Prompting the user to enter their age
# age = int(input("Enter your age: "))

# # Checking the age and printing the eligibility status
# if age >= 18:
#     print("You are eligible to vote.")
# elif age >= 0 and age < 18:
#     print("You are not eligible to vote. You must be 18 or older.")
# else:
#     print("Invalid age entered.")
# # Output
# # Enter your age: 18

# # You are eligible to vote.

# Hello




# Prompting the user to enter their age
age = int(input("Enter your age: "))

# Checking the age and printing the eligibility status
if age >= 18:
    print("You are eligible to vote.")
else:
    if age >= 0:
        print("You are not eligible to vote. You must be 18 or older.")
    else:
        print("Invalid age entered.")
# OUTPUT
# Enter your age: 12
# You are not eligible to vote. You must be 18 or older.
# Enter your age: 19
# You are eligible to vote