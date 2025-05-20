# Challenge: Number Pyramid Builder

# Take input from user: number of rows in the pyramid
n = int(input("Enter numbers of row: "))

# Initialize the row counter
i = 1

# Outer loop to control the number of rows
while i <= n:
    # Initialize the column counter for each row
    j = i
    
    # Inner loop to print the number(s) in the current row
    while j <= i:
        print(j, end=" ")  # Print the number and stay on the same line
        j += 1  # Move to the next number (though this always runs only once here)
    
    print()  # Move to the next line after printing a row
    i += 1  # Move to the next row
