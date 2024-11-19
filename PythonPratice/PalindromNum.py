a = int(input("Enter your number: "))
original = a
result = 0
while a > 0:
    last = a % 10
    result = result * 10 + last
    a = a // 10

print("Reversed number:", result)
if result == original:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")