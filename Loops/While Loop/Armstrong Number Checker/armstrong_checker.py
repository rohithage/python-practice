# Challenge: Check if a number is an armstrong number

# input from user 
num = int(input("Enter a number: "))

# Save the original number to compare later
original = num

# Find the number of digits
order = len(str(num))

# Initialize sum
sum_of_powers = 0

# Process each digit
while n > 0:
    digit = num % 10 # Get the last digit
    sum_of_powers += digit ** order # Add the digit raised to the power of order
    num = num // 10

# Check if the sum matches the original number
if sum_of_powers == original:
    print(f"{original} is an Armstrong Number")
else:
    print(f"{original} is not an Armstrong number")