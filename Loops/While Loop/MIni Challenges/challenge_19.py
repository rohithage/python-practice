# Calculate sum of squares of each digit in a number
number = int(input("Enter a number: "))  
sum_of_squares = 0  

while number > 0:
    digit = number % 10  # Extract the last digit
    sum_of_squares += digit ** 2  # Add square of the digit
    number = number // 10  # Remove the last digit

print(f"Sum of squares of digits: {sum_of_squares}")