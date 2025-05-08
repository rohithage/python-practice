# Grade Calculator Program

# Get user input and convert to integer
marks = int(input("Enter your marks (0-100): "))

# Validate input range
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
else:
    # Determine grade based on marks
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    else:
        print("Fail")