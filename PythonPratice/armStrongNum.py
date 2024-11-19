# Input: Enter a number
number = int(input("Enter a number: "))

# Calculate the number of digits
num_digits = len(str(number))

# Calculate the sum of the digits raised to the power of num_digits
armstrong_sum = sum(int(digit) ** num_digits for digit in str(number))

# Check if the number is an Armstrong number
if number == armstrong_sum:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")