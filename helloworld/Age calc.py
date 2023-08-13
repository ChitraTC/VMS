def sum_of_digits(number,length):
    remainder = result = 0
    while number != 0:
        remainder = number % 10
        result = result + (remainder ** length)
        number = number // 10
        length = length - 1
    return result

print("Disarium numbers between 1 and 100 are \n")
for number in range(1, 101):
    number=str(number)
    length=len(number)
    number=int(number)
    result = sum_of_digits(number,length)
    if result == number:
        print(number)