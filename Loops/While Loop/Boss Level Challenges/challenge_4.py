# Challenge: Find the GCD (Greatest Common Divisor) of Two Numbers

# Step 1: Take two inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Step 2: Find the smaller number
if num1 < num2:
    smaller = num1
else:
    smaller = num2

# Step 3: Loop from smaller down to 1
while smaller > 0:
    if num1 % smaller == 0 and num2 % smaller == 0:
        # If 'smaller' divides both numbers, it is the GCD
        gcd = smaller
        break
    smaller -= 1  # Decrease and check again

# Step 4: Print the GCD
print(f"The GCD of {num1} and {num2} is: {gcd}")
