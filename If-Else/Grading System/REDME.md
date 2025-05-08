# Grade Calculator 📊

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

## Description
A simple Python program that calculates grades based on marks input (0-100 scale). The program provides instant grade evaluation with input validation.

## Features
- ✅ Instant grade calculation
- 🔢 Input validation (0-100 range)
- 📝 Clear grade categories:
  - 90+ → Grade A
  - 80-89 → Grade B
  - 70-79 → Grade C
  - Below 70 → Fail

## Usage
1. Run the program:

python grade_calculator.py

2. Enter your marks when prompted (0-100)

## Sample Outputs

Enter your marks (0-100): 95
Grade A


Enter your marks (0-100): 82
Grade B


Enter your marks (0-100): 68
Fail


Enter your marks (0-100): 105
Invalid marks! Please enter a value between 0 and 100.


## Requirements
- Python 3.6+

## How It Works
1. Takes integer input (0-100)
2. Validates input range
3. Uses conditional statements to determine grade:

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
# ... etc


## Author
Rohit Hage
rohithage(https://github.com/rohithage)  
📧 rohithage8@gmail.com
