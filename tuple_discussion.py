def get_avg():
    name = input("Enter the name of the student: ")
    score_1 = int(input("Enter the score for test 1: "))
    score_2 = int(input("Enter the score for test 2: "))
    score_3 = int(input("Enter the score for test 3: "))
    avg = (score_1 + score_2 + score_3)/3
    return name, avg
name , avg = get_avg()
print(f"The average test score of {name.title()} is {avg:.2f}!")