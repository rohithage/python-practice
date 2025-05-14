# Chocolate Distribution 🍫

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Logic](https://img.shields.io/badge/category-logic-orange)

## Description
A Python program that fairly distributes chocolates between two people based on turn order. Person B gets odd-numbered chocolates (1st, 3rd, 5th...) while Person A gets even-numbered chocolates (2nd, 4th, 6th...).

## Features
- 🍫 Fair turn-based distribution
- 🔢 Handles any positive number of chocolates
- 📊 Clear output showing distribution
- ⚡ Efficient while-loop implementation
- 🎯 Simple conditional logic

## Usage

python chocolate_distribution.py

Enter the total number of chocolates when prompted.

## How It Works
1. Takes total chocolates as input
2. Uses a counter to track each chocolate
3. Distributes using modulo operation:
   python
   if i % 2 == 0:
       a_chocolates += 1  # Even to Person A
   else:
       b_chocolates += 1  # Odd to Person B
   
4. Outputs the final distribution count

## Sample Outputs

Enter total chocolates: 10
Person A gets 5 Chocolates
Person B gets 5 Chocolates



Enter total chocolates: 7
Person A gets 3 Chocolates
Person B gets 4 Chocolates


## Logic Explanation
- **Person B**: Gets chocolates 1, 3, 5... (odd positions)
- **Person A**: Gets chocolates 2, 4, 6... (even positions)
- For even totals, both get equal shares
- For odd totals, Person B gets one extra

## Applications
- Fair resource distribution
- Turn-based game mechanics
- Alternating task assignments
- Educational tool for modulo operations

## Requirements
- Python 3.6+

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com

