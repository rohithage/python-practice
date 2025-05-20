# Rope Cutting Optimizer ✂️

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Algorithm](https://img.shields.io/badge/category-algorithm-orange)
![Optimization](https://img.shields.io/badge/category-optimization-yellow)

## Description
A Python program that calculates the maximum number of pieces a rope can be divided into when cut into segments of lengths 3, 5, and 7 units. The program uses a brute-force approach to find the optimal combination of segment lengths that maximizes the number of pieces.

## Features
- ✂️ Finds optimal rope cutting configuration
- 🔢 Handles any positive integer rope length
- ⚡ Efficient nested loop implementation
- 📊 Maximizes total number of pieces
- 🧮 Checks all possible combinations of lengths 3, 5, and 7

## Usage

python rope_cutting.py

Enter the rope length when prompted.

## How It Works
1. Takes rope length as input
2. Uses nested loops to try all combinations of:
   - 3-unit pieces (i)
   - 5-unit pieces (j)
3. Calculates remaining length for 7-unit pieces (k)
4. Validates if remaining length can be divided by 7
5. Tracks the combination with maximum total pieces

## Algorithm

while i * 3 <= n:
    while i * 3 + j * 5 <= n:
        rem = n - (i * 3 + j * 5)
        if rem % 7 == 0:
            k = rem // 7
            max_pieces = max(max_pieces, i + j + k)
        j += 1
    i += 1


## Sample Outputs

Enter the rope length: 23
Maximum number of pieces: 5

(Explanation: 5 pieces = 2×3 + 1×5 + 2×7)


Enter the rope length: 15
Maximum number of pieces: 3

(Explanation: 3 pieces = 5×3 or 3×5)

## Mathematical Approach
The program solves the equation:

3i + 5j + 7k = n

Where:
- i, j, k are non-negative integers
- Goal is to maximize (i + j + k)

## Applications
- Resource allocation optimization
- Manufacturing material cutting
- Inventory management
- Mathematical problem solving
- Algorithm design practice

## Requirements
- Python 3.6+

## Customization
Modify the segment lengths by changing:
python
3, 5, 7  # Current segment lengths

## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com