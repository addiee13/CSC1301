# This loop converts temperature to and from celsius and fahreneheit
# Loop indefinitely:
#     Output "Temperature Converter"
#     Output "1. Convert Celsius to Fahrenheit"
#     Output "2. Convert Fahrenheit to Celsius"
#     Output "3. Quit"
#     Prompt user for choice and store it in variable choice

#     If choice is '1':
#         Prompt user for temperature in Celsius and store it in variable celsius
#         Calculate temperature in Fahrenheit using the formula (celsius * 9/5) + 32
#         Output "Temperature in Fahrenheit:" followed by the calculated temperature
#     Else if choice is '2':
#         Prompt user for temperature in Fahrenheit and store it in variable fahrenheit
#         Calculate temperature in Celsius using the formula (fahrenheit - 32) * 5/9
#         Output "Temperature in Celsius:" followed by the calculated temperature
#     Else if choice is '3':
#         Output "Exiting program..."
#         Exit the loop
#     Else:
#         Output "Invalid choice. Please enter 1, 2, or 3."
#-------------------------------------------------------------------------------------------------
while True:
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

#----------------------------------------------------------------------------------        
# For each iteration in range(1):
#     Output "Temperature Converter"
#     Output "1. Convert Celsius to Fahrenheit"
#     Output "2. Convert Fahrenheit to Celsius"
#     Output "3. Quit"

#     Prompt user for choice and store it in variable choice

#     If choice is '1':
#         Prompt user for temperature in Celsius and store it in variable celsius
#         Calculate temperature in Fahrenheit using the formula (celsius * 9/5) + 32
#         Output "Temperature in Fahrenheit:" followed by the calculated temperature
#     Else if choice is '2':
#         Prompt user for temperature in Fahrenheit and store it in variable fahrenheit
#         Calculate temperature in Celsius using the formula (fahrenheit - 32) * 5/9
#         Output "Temperature in Celsius:" followed by the calculated temperature
#     Else if choice is '3':
#         Output "Exiting program..."
#         Exit the loop
#     Else:
#         Output "Invalid choice. Please enter 1, 2, or 3."
#------------------------------------------------------------------------------------------------------

for _ in range(1):
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
#------------------------------------------------------------------------------------
# OUTPUT
# 1. Convert Celsius to Fahrenheit
# 2. Convert Fahrenheit to Celsius
# 3. Quit
# Enter your choice (1/2/3): 1
# Enter temperature in Celsius: 23
# Temperature in Fahrenheit: 73.4
# Temperature Converter
# 1. Convert Celsius to Fahrenheit
# 2. Convert Fahrenheit to Celsius
# 3. Quit
# Enter your choice (1/2/3): 2
# Enter temperature in Fahrenheit: 45
# Temperature in Celsius: 7.222222222222222
# Temperature Converter
# 1. Convert Celsius to Fahrenheit
# 2. Convert Fahrenheit to Celsius
# 3. Quit
# Enter your choice (1/2/3): 3
# Exiting program...
# Temperature Converter
# 1. Convert Celsius to Fahrenheit
# 2. Convert Fahrenheit to Celsius
# 3. Quit
# Enter your choice (1/2/3): 3
# Exiting program...