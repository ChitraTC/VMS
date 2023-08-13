# Code to generate Disarium number starts
def calculate_length(number):
    length = 0
    while number != 0:
        length = length + 1
        number = number // 10
    return length
# sum_of_digits() will calculates the sum of digits powered with their respective position
def sum_of_digits(number):
    remainder = result = 0
    length = calculate_length(number)
    while number > 0:
        remainder = number % 10
        result = result + (remainder ** length)
        number = number // 10
        length = length - 1
    return result
def print_disarium():
    result = 0
# Displays all Disarium numbers between 1 and 100
print("Disarium numbers between 1 and 1000 are \n")
for each_number in range(1, 1001):
    result = sum_of_digits(each_number)
    if result == each_number:
        print(each_number)
# Code to generate Disarium number ends
