import numpy as np
grades_boys = [56,89,51,90]
grades_girls = [90,89,76,45]

grades_boys_array = np.array(grades_boys)
grades_girls_array = np.array(grades_girls)

print(f"The diff between individual grade is {abs(grades_boys_array - grades_girls_array)}")