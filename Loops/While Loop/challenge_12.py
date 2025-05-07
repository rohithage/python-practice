# Challenge 12: Reverse the Digits of a Number
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10       # Get last digit
    reverse = (reverse * 10) + digit  # Shift previous digits and add new one
    n = n // 10           # Remove last digit

print(f"Reversed Number: {reverse}")
