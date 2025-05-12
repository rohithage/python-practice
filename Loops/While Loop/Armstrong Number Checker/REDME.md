# Armstrong Number Checker 🔢

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Math](https://img.shields.io/badge/category-math-orange)

## Description
A Python program that checks whether a given number is an Armstrong number (also known as narcissistic number). An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## Features
- ✅ Checks for Armstrong numbers of any length
- 🔢 Handles positive integers only
- ⚡ Instant verification
- 📊 Example: 153 (1³ + 5³ + 3³ = 153) is an Armstrong number

## Usage
python armstrong_checker.py

Then enter any positive integer when prompted.

## How It Works
1. Takes integer input from user
2. Calculates the number of digits (order)
3. Processes each digit:
   - Extracts digits one by one
   - Raises each digit to the power of total digits
   - Sums these values
4. Compares the sum to the original number

## Sample Outputs

Enter a number: 153
153 is an Armstrong Number


Enter a number: 370
370 is an Armstrong Number


Enter a number: 123
123 is not an Armstrong number


Enter a number: 9474
9474 is an Armstrong Number


## Requirements
- Python 3.6+

## Mathematical Background
An n-digit number is an Armstrong number if:

abcd... = aⁿ + bⁿ + cⁿ + dⁿ + ...

Where:
- a, b, c, d... are the digits
- n is the number of digits

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com