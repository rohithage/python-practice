# GCD Calculator 🧮

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Math](https://img.shields.io/badge/category-mathematics-orange)

## Description
A Python program that calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm. The GCD is the largest positive integer that divides both numbers without leaving a remainder.

## Features
- 🚀 Efficient implementation of Euclidean algorithm
- 🔢 Handles all positive integers
- 💡 Preserves original input values for clear output
- ⚡ Instant results

## Usage

python gcd_calculator.py

Then enter two positive integers when prompted.

## How It Works
1. Takes two integer inputs from the user
2. Implements the Euclidean algorithm:
   python
   while b != 0:
       temp = b
       b = a % b
       a = temp
   
3. Outputs the GCD of the original numbers

## Sample Outputs

Enter the first number: 56
Enter the second number: 98
The GCD of 56 and 98 is 14


Enter the first number: 81
Enter the second number: 153
The GCD of 81 and 153 is 9


Enter the first number: 17
Enter the second number: 23
The GCD of 17 and 23 is 1


## Mathematical Background
The Euclidean algorithm works on the principle that:

GCD(a, b) = GCD(b, a mod b)

This process continues until b becomes 0, at which point 'a' contains the GCD.

## Requirements
- Python 3.6+

## Applications
GCD is fundamental in:
- Simplifying fractions
- Cryptography algorithms
- Number theory problems
- Computer science algorithms

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com