# Loop through numbers from 1 to 50 (inclusive)
for i in range(1, 51):

    # If the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # If only divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    
    # If only divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    
    # If none of the above, just print the number itself
    else:
        print(i)

    