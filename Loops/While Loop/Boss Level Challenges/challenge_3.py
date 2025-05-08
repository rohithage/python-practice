# Challenge 3: Check if a Number is a Armstrong Number

# Take user input for the number
n = int(input("Enter a number: "))

# Store the original number for comparison later
original = n

# Initialize sum to accumulate the sum of powered digits
sum = 0

# Loop until all digits are processed
while n > 0:
    last_digit = n % 10       # Extract the last digit
    sum += last_digit ** 3    # Add the cube of the digit to sum
    n = n // 10               # Remove the last digit

# Check if the sum of cubes equals the original number
if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")