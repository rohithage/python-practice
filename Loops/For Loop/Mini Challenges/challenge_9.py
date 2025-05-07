# Loop from 1 to 30
for i in range(1, 31):

    # Check if number divisible by both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print(f"Divisible by 3 and 5: {i}")

    # Check if divisible only by 3
    elif i % 3 == 0:
        print(f"Divisible by 3: {i}")

    # Check if divisible only by 5
    elif i % 5 == 0:
        print(f"Divisible by 5: {i}")

    # If not divisible by 3 or 5
    else:
        print(f"Number: {i}")
