# Challenge 15: Calculate Product of All Digits in a Number

# Get input number from user
number = int(input("Enter a number: "))
original_number = number  # Store original for output
product = 1  # Initialize product (multiplicative identity)

# Handle special case of 0 input
if number == 0:
    product = 0  # Product of digits for 0 is 0
else:
    # Process each digit
    while number > 0:
        last_digit = number % 10  # Extract last digit
        product *= last_digit     # Multiply with product
        number = number // 10    # Remove last digit

# Print the result with original number
print(f"Product of digits in {original_number}: {product}")