# Challenge 13: Sum of Digits
n = int(input("Enter a number: "))
sum_of_digits = 0

while n > 0:
    digit = n % 10       # Get last digit
    sum_of_digits += digit
    n = n // 10          # Remove last digit

print(f"Sum of digits: {sum_of_digits}")
