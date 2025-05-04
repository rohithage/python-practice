n = int(input("Enter a Number: "))

if n == 0:
    print("Zero")
elif n > 0 and n % 2 == 0:
    print("Positive Even")
elif n > 0 and n % 2 != 0:
    print("Positive Odd") 
else:
    print("Negative Number")
