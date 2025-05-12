# Input from the user
a = int(input("Enter the first number: "))  # Input first number from the user
b = int(input("Enter the second number: ")) # Input second number from the user

# Store original numbers
original_a = a  # Save the original value of a for later use
original_b = b  # Save the original value of b for later use

# Find GCD using Euclid's Algorithm
while b != 0:
    temp = b              # Store current value of b in temp
    b = a % b             # Set b as the remainder of a divided by b
    a = temp              # Set a as previous b

gcd = a   # After the loop, 'a' will hold the GCD

# Calculate LCM
lcm = (original_a * original_b) // gcd   # LCM formula: (a * b) / GCD

# Print LCM
print(f"The LCM of the given numbers is: {lcm}")
