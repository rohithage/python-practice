# Challenge: Rope Cutting Optimizer

# Take input for the total length of the rope
n = int(input("Enter the rope length: "))

# Initialize variable to keep track of the maximum number of pieces
# Start with -1 to indicate that no valid combination has been found yet
max_pieces = -1

# Start looping with i: number of pieces of length 3
i = 0
while i * 3 <= n:  # Ensure total length of 3-length pieces doesn't exceed rope length
    j = 0
    # Start looping with j: number of pieces of length 5
    while i * 3 + j * 5 <= n:  # Ensure combined length of 3s and 5s doesn't exceed rope length
        # Calculate remaining length after using 3-length and 5-length pieces
        rem = n - (i * 3 + j * 5)
        
        # Check if the remaining length can be divided into 7-length pieces
        if rem % 7 == 0:
            k = rem // 7  # Calculate number of 7-length pieces that fit
            
            # Calculate total number of pieces used in this combination
            total_pieces = i + j + k
            
            # Update max_pieces if this combination gives more pieces
            max_pieces = max(max_pieces, total_pieces)
        
        j += 1  # Try next value of j (more 5-length pieces)
    
    i += 1  # Try next value of i (more 3-length pieces)

# After checking all combinations, print the maximum number of pieces found
print(f"Maximum number of pieces: {max_pieces}")
