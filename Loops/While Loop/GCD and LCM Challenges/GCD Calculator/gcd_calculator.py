# Challenge: Find the GCD (Greatest Common Divisor) of Two Numbers

# GCD of two numbers using while loop

# Input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Store original values for display later
x = a 
y = b

# Using while loop to find the GCD
while b != 0:
    temp = b # Save the value of b in temp
    b = a % b # Update b to be the remainder of divide by b
    a = temp # Update a to be the old value of b

# 'a' now contains the GCD after the loop ends.
print(f"The GCD of {x} and {y} is {a}")