# Challenge: Split Chocolates

# Take input for total chocolates
chocolates = int(input("Enter total chocolates: "))

# Initialize count for Person A and Person B
a_chocolates = 0  # Person A's chocolates (even turns)
b_chocolates = 0  # Person B's chocolates (odd turns)

# Initialize the counter
i = 1  # Start counting from chocolate #1

# Use a while loop to distribute chocolates one by one
while i <= chocolates:
    if i % 2 == 0:
        a_chocolates += 1  # Even-numbered chocolate goes to Person A
    else:
        b_chocolates += 1  # Odd-numbered chocolate goes to Person B
    i += 1  # Move to the next chocolate

# Print the result
print(f"Person A gets {a_chocolates} Chocolates")
print(f"Person B gets {b_chocolates} Chocolates")



'''# Ask the user how many chocolates they have
n = int(input("How many chocolates do you have? "))

# Initialize empty lists to store chocolates for Person A and B
a_list = []  # Will store even-valued chocolates (Person A)
b_list = []  # Will store odd-valued chocolates (Person B)

# Start counter from 1
i = 1

# Loop through each chocolate
while i <= n:
    # Ask user for the value of the i-th chocolate
    value = int(input(f"Enter value of chocolate {i}: "))
    
    # If the chocolate value is even, give to Person A
    if value % 2 == 0:
        a_list.append(value)
    # Otherwise (odd), give to Person B
    else:
        b_list.append(value)

    # Move to the next chocolate
    i += 1

# Print final result
print("\n--- Result ---")
print("Person A gets", len(a_list), "chocolates:", a_list)
print("Person B gets", len(b_list), "chocolates:", b_list)
'''