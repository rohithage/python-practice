# Challenge 2: Product of Digits Until Single Digit

# Take user input for the number
n = int(input("Enter a number: "))

# Loop until 'n' becomes a single-digit number (n < 10)
while n >= 10:
    product = 1  # Initialize product for the current iteration
    
    # Multiply all digits of 'n'
    while n > 0:
        last_digit = n % 10  # Extract the last digit
        product *= last_digit  # Multiply it into the product
        n = n // 10  # Remove the last digit
    
    n = product  # Update 'n' to be the product of its digits
    # The loop repeats if 'n' is still >= 10

# Print the final single-digit result
print(f"Final Single digit: {n}")