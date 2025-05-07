# Challenge 10: Calculate Factorial of a Number

# Get input number from user
n = int(input("Enter a Number: "))

# Initialize factorial result (0! = 1, 1! = 1)
factorial = 1  

# Initialize loop counter
i = 1  

# Calculate factorial using while loop
while i <= n:
    factorial *= i  # Multiply current factorial by counter
    i += 1         # Increment counter

# Print formatted result (e.g., "5! = 120")
print(f"{n}! = {factorial}")