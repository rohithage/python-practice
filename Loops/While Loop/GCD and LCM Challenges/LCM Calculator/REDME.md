# LCM Calculator 🔢

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Math](https://img.shields.io/badge/category-mathematics-orange)

## Description
A Python program that calculates the Least Common Multiple (LCM) of two numbers using their Greatest Common Divisor (GCD). The program implements Euclid's Algorithm for GCD calculation and then uses the mathematical relationship between GCD and LCM.

## Features
- 🧮 Calculates both GCD and LCM
- ⚡ Uses efficient Euclid's Algorithm
- 📊 Preserves original input values
- 💡 Clear output formatting
- 🔢 Handles all positive integers

## Usage

python lcm_calculator.py

Then enter two positive integers when prompted.

## How It Works
1. Takes two integer inputs from user
2. Calculates GCD using Euclid's Algorithm:
   python
   while b != 0:
       temp = b
       b = a % b
       a = temp
   
3. Calculates LCM using the formula:
   python
   LCM = (a × b) // GCD
   
4. Outputs the calculated LCM

## Sample Outputs

Enter the first number: 12
Enter the second number: 18
The LCM of the given numbers is: 36


Enter the first number: 21
Enter the second number: 14
The LCM of the given numbers is: 42


Enter the first number: 15
Enter the second number: 28
The LCM of the given numbers is: 420


## Mathematical Background
The program uses these mathematical principles:
- **Euclid's Algorithm** for GCD:
  
  GCD(a, b) = GCD(b, a mod b)
  
- **LCM-GCD Relationship**:
  
  LCM(a, b) = (a × b) / GCD(a, b)
  

## Requirements
- Python 3.6+

## Applications
- Solving fraction problems
- Finding common denominators
- Scheduling problems
- Cryptography algorithms
- Number theory applications

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com