# Count even and odd digits in a number
n = int(input("Enter a number: "))
even_count = 0  # Tracks even digits
odd_count = 0   # Tracks odd digits

while n > 0:
    digit = n % 10       # Extract last digit
    if digit % 2 == 0:   # Check if even
        even_count += 1
    else:                # Otherwise odd
        odd_count += 1
    n = n // 10          # Remove last digit

print("Even digits:", even_count)
print("Odd digits:", odd_count)