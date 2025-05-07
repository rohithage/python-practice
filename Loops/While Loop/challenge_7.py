# Challenge 7: Calculate the sum of numbers from 1 to 10

# Initialize sum accumulator and counter
total_sum = 0  
current_number = 1  # Starting number

# Loop while current number is less than or equal to 10
while current_number <= 10:
    total_sum += current_number  # Add current number to the running total
    current_number += 1  # Move to the next number
    
# Print the final result using f-string formatting
print(f"The sum of numbers from 1 to 10 is: {total_sum}")