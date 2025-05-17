# Color Timing Indicator 🚦

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Logic](https://img.shields.io/badge/category-logic-orange)

## Description
A Python program that demonstrates conditional timing logic by indicating color outputs based on second intervals. The program shows how to combine multiple conditions to generate different outputs at specific time intervals.

## Features
- ⏱️ Simple timing simulation
- 🎨 Conditional color output
- 📊 Clear formatted output
- 🔢 Modular condition checking
- ➕ String concatenation handling

## Usage

python color_timer.py

## How It Works
1. Initializes a second counter
2. For each second:
   - Checks divisibility by 2 (Red)
   - Checks divisibility by 3 (Green)
   - Handles multiple conditions with proper formatting
   - Provides default "-" when no conditions match
3. Outputs the result for each second

## Code Logic
python
while second <= 1:
    output = ""
    if second % 2 == 0:
        output += "Red"
    if second % 3 == 0:
        if output != "":
            output += ", "
        output += "Green"
    if output == "":
        output = "-"
    print(f"Second {second}: {output}")
    second += 1


## Sample Output

Second 1: -

## Expected Outputs for Extended Runtime
(If modifying the loop condition to run longer)

Second 1: -
Second 2: Red
Second 3: Green
Second 4: Red
Second 5: -
Second 6: Red, Green


## Applications
- Traffic light simulation
- Event scheduling
- Pattern generation
- Educational tool for:
  - Modulo operations
  - Conditional logic
  - String concatenation

## Requirements
- Python 3.6+

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com