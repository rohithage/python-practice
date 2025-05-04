age = int(input("Enter Your Age: "))

category = "Invalid Age"  # Default value if nothing matches

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "Teenager"
elif age >=20 and age <=59:
    category = "Adult"
elif age >= 60:
    category = "Senior Citizen"

print(category)
