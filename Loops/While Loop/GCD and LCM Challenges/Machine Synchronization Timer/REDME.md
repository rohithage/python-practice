# Machine Synchronization Timer ⏱️

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Math](https://img.shields.io/badge/category-mathematics-orange)
![Physics](https://img.shields.io/badge/category-physics-yellow)

## Description
A Python program that calculates when two machines with different beeping intervals will synchronize (beep together) using Least Common Multiple (LCM) calculation. Implements Euclid's Algorithm for efficient GCD calculation.

## Features
- 🚀 Efficient GCD calculation using Euclid's Algorithm
- ⏱️ Accurate synchronization timing prediction
- 🔢 Handles any positive integer intervals
- 📊 Clear output showing synchronization time
- 🧮 Modular design with separate GCD and LCM functions

## Usage

# Customize machine intervals by changing these values:
a = 12  # Machine A's beep interval (seconds)
b = 18  # Machine B's beep interval (seconds)

# Run the program to see synchronization time
python machine_sync.py


## How It Works
1. Calculates GCD using Euclid's Algorithm:
   python
   def gcd(a, b):
       while b != 0:
           a, b = b, a % b
       return a
   
2. Calculates LCM using the GCD:
   python
   def lcm(a, b):
       return (a * b) // gcd(a, b)
   
3. Determines synchronization time as the LCM of both intervals

## Sample Output

Both machines will beep together after 36 seconds.


## Mathematical Background
The synchronization time is found using:

Synchronization Time = LCM(interval_A, interval_B)

Where LCM is calculated using:

LCM(a, b) = (a × b) / GCD(a, b)


## Applications
- Industrial machine synchronization
- Traffic light timing systems
- Musical metronome alignment
- Astronomical event prediction
- Process scheduling in operating systems

## Requirements
- Python 3.6+

## Customization
Edit the interval values in the code:
python
a = 15  # Change to Machine A's actual interval
b = 25  # Change to Machine B's actual interval


## Author
Rohit Hage 

rohithage(https://github.com/rohithage)  
📧 rohithage@gmail.com
