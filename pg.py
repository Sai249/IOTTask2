import random
import string

def generate_password(num_letters, num_numbers, num_symbols):
    password = []

    # Add letters
    for _ in range(num_letters):
        password.append(random.choice(string.ascii_letters))

    # Add numbers
    for _ in range(num_numbers):
        password.append(random.choice(string.digits))

    # Add symbols
    for _ in range(num_symbols):
        password.append(random.choice(string.punctuation))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Get user input
num_letters = int(input("Enter the number of letters: "))
num_numbers = int(input("Enter the number of numbers: "))
num_symbols = int(input("Enter the number of symbols: "))

# Generate the password
password = generate_password(num_letters, num_numbers, num_symbols)

print(f"Generated Password: {password}")
