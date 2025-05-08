# Challenge 11: Generate Multiplication Table for Any Number

# Get input number from user
n = int(input("Enter a Number: "))

# Initialize counter starting at 1
i = 1

# Generate multiplication table from 1 to 10
while i <= 10:
    # Print formatted multiplication expression (n x i = result)
    print(f"{n} × {i} = {n * i}")  
    
    # Increment counter for next iteration
    i += 1