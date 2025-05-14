# Challenge: Timing Machines

# Function to calculate GCD using Euclid's Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Simultaneously update a and b
    return a  # When b becomes 0, a contains the GCD

# Function to calculate LCM using the GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)  # LCM formula: (a * b) / GCD

# Machine A and B beep every 'a' and 'b' seconds respectively
a = 12
b = 18

# Find when both machines beep together (i.e., LCM of a and b)
result = lcm(a, b)

# Display the result
print(f"Both machines will beep together after {result} seconds.")
