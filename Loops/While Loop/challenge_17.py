# Check if a number is palindrome (reads same forwards and backwards)
num = int(input("Enter a number: "))
original = num  # Store original number for comparison
reverse = 0     # Initialize reversed number

# Reverse the digits
while num > 0:
    digit = num % 10       # Get last digit
    reverse = reverse * 10 + digit  # Build reversed number
    num = num // 10        # Remove last digit

# Compare original with reversed
print(f"{original}: {'Palindrome' if original == reverse else 'Not Palindrome'}")