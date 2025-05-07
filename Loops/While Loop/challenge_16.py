# Challenge 16: Calculate Sum of Even Digits in a Number

# Get input number from user
number = int(input("Enter a number: "))
original_number = number  # Store original for output
even_sum = 0  # Initialize sum (better variable name than 'sum')

# Process each digit
while number > 0:
    digit = number % 10  # Extract last digit
    
    # Check if digit is even
    if digit % 2 == 0:
        even_sum += digit  # Add to sum if even
    
    number = number // 10  # Remove last digit

# Print the result with original number
print(f"Sum of even digits in {original_number}: {even_sum}")