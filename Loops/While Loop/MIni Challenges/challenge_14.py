# Challenge 14: Count the Number of Digits in a Number

# Get input number from user
num = int(input("Enter a Number: ")) 
count = 0  # Initialize digit counter

# Special case: handle 0 input
if num == 0:
    count = 1  # 0 has exactly 1 digit
else:
    # Process each digit by removing last digit until none left
    while num > 0:
        num = num // 10  # Remove last digit
        count += 1       # Increment digit counter

# Print the result
print(f"Number of digits: {count}")