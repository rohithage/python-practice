# Challenge 1: Find the Sum of Digits Until Single Digit

# Take user input and convert it to an integer
number = int(input("Enter a number: "))

# Continue looping until the number is reduced to a single digit
while number >= 10:
    sum = 0          # Initialize sum to store the sum of digits
    n = number       # Make a copy of 'number' to process digits
    
    # Loop to extract and sum each digit of 'n'
    while n > 0:
        digit = n % 10   # Get the last digit using modulo 10
        sum += digit     # Add the digit to the sum
        n = n // 10      # Remove the last digit using integer division
    
    # Update 'number' with the sum of its digits for the next iteration
    number = sum

# Print the final single-digit result
print(f"Final Single Digit: {number}")