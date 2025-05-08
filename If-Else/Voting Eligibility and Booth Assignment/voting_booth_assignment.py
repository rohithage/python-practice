# Voting Eligibility and Booth Assignment Program

# Get user input for age (converted to integer)
age = int(input("Enter Your Age: "))

# Get user input for citizenship status (converted to lowercase for case-insensitive comparison)
citizen = input("Your citizen yes or no: ").lower()

# Check voting eligibility based on age
if age < 18:
    # If under 18, print not eligible message
    print("You're not eligible for vote")
else:
    # For ages 18+, check citizenship status
    if citizen == "yes":
        # Citizen voters: assign booth based on age ranges
        if 18 <= age <= 25:
            # Young voters (18-25) go to Booth A
            print("Assigned to Booth A")
        elif 26 <= age <= 40:
            # Middle-aged voters (26-40) go to Booth B
            print("Assigned to Booth B")
        else:
            # Senior voters (40+) go to Booth C
            print("Assigned to Booth C")
    else:
        # Non-citizens cannot vote
        print("Only citizens can vote")