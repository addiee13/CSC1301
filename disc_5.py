##Calculates the area of the rectangle
#   @param length the length of the rectangle
#   @param width the width if the rectangle
#   @return area area of the rectangle
def calculate_rectangle_area(length, width):
    area = length * width  # Calculate area using the formula length * width
    return area
print(calculate_rectangle_area(50, 9))
# OUTPUT
# 450

##Prints the multiples of a number upto 10
#   number the number whose multiples are displayed
def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number * i}")
print_multiplication_table(9)

#OUTPUT
# Multiplication table for 9:
# 9
# 18
# 27
# 36
# 45
# 54
# 63
# 72
# 81
# 90