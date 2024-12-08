import random
import string

def generate_password(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Build the character set based on the input flags
    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        # Check if all criteria are met
        meets_criteria = True
        if number:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# Get user input
try:
    min_length = int(input("Enter the minimum length of the password: "))
    if min_length < 1:
        raise ValueError("Password length must be at least 1.")
except ValueError as e:
    print(f"Invalid input for minimum length: {e}")
    exit()

has_number = input("Do you want to include numbers? (y/n): ").strip().lower() == "y"
has_special = input("Do you want to include special characters? (y/n): ").strip().lower() == "y"

# Generate and display the password
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is: {pwd}")
