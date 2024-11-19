a = int(input("Enter your number: "))
original = a
result = 0
while a > 0:
    last = a % 10
    result = result * 10 + last
    a = a // 10
sum_original = sum(int(digit) for digit in str(original))
print("Reversed number:", result)
print("Sum of digits of the original number:", sum_original)
