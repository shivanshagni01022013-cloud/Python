import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Ask user if they want to include special characters
use_specials = input("Include special characters? (yes/no): ").lower()

# Define characters to use
letters = string.ascii_letters
digits = string.digits
specials = string.punctuation if use_specials == "yes" else ""

# Combine all possible characters
all_chars = letters + digits + specials

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
