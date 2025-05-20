# Number Pyramid Builder 🔢

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Pattern](https://img.shields.io/badge/category-pattern-orange)

## Description
A Python program that generates a number pyramid pattern based on user input. The current implementation creates a simple left-aligned number sequence, serving as a foundation for more complex pyramid patterns.

## Features
- 🏗️ Builds customizable number patterns
- 🔢 Handles any positive integer row count
- 📐 Simple nested loop structure
- 🧱 Foundation for more complex pyramid patterns
- 🖨️ Clean output formatting

## Usage

python number_pyramid.py

Enter the desired number of rows when prompted.

## Current Implementation
python
while i <= n:
    j = i
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


## Sample Output (3 rows)

1 
2 
3 


## Potential Enhancements
Try modifying the program to create:
python
1 
1 2 
1 2 3 

Or:
python
    1
   2 2
  3 3 3


## How to Extend
1. For a right-aligned pyramid:
   python
   print(" " * (n-i), end="")
   
2. For a centered pyramid:
   python
   print(" " * (n-i), end="")
   
3. For repeating numbers:
   python
   print(str(i) * i, end=" ")
   

## Applications
- Programming education
- Pattern recognition exercises
- Algorithm visualization
- Console art generation
- Looping practice

## Requirements
- Python 3.6+

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com