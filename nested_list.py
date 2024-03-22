STUDENTS = 4
TESTS = 3
students = ["Adam", "Harini", "Ayushman", "Riyan"]
scores = [
        [60, 70, 80],
        [80,90,100], 
        [50, 40, 60], 
        [30,80,60]
          ]

def max_score(scores):
    max = scores[0][0]
    for score in scores:
        for i in score:
            if i >= max:
                max = i
    return(max)

def test_avg(scores):
    total_1 = 0
    total_2 = 0
    total_3 = 0
    for score in scores: 
        total_1 += score[0]
        total_2 += score[1]
        total_3 += score[2]
    return (total_1/STUDENTS, total_2/STUDENTS, total_3/STUDENTS)
def highest_scorer(scores, students):
    max = max_score(scores)
    i = 0
    while i < len(scores[i]):
        j = 0
        while j < len(scores[i]):
            if max == scores[i][j]:
                return students[i]
            j += 1
        i += 1
avg_1 , avg_2, avg_3 = test_avg(scores)
# print(f"The average of first test is {avg_1:.2f}, second test is {avg_2:.2f} and third test is {avg_3:.2f}")
print(f"The highest scorer is {highest_scorer(scores, students)}")

