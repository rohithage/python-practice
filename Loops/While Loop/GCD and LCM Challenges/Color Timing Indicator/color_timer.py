# Challenge: Color Timing Indicator

# Initialize the second counter
second = 1

# Loop runs while 'second' is less than or equal to 1
while second <= 1:
    output = ""  # Reset output for each second
    
    # If 'second' is divisible by 2, append "Red" to output
    if second % 2 == 0:
        output += "Red"
    
    # If 'second' is divisible by 3, append "Green"
    if second % 3 == 0:
        if output != "":
            output += ", "  # Add comma if another color already exists
        output += "Green"  # Append "Green" to output

    # If output is still empty, set it to "-"
    if output == "":
        output = "-"
    
    # Print result for current second
    print(f"Second {second}: {output}")
    
    # Move to the next second
    second += 1
