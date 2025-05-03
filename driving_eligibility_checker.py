age = int(input("Enter Your Age: "))

has_license = input("Do you have a License yes or no").lower()
if age < 18:
    print("Not Eligible to Drive")
    
else:
    if has_license == "yes":
        print("Eligible to Drive")
    else:
        print("Get License First")

