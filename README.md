Importing Libraries
Python

import random
import string
AI-generated code. Review and use carefully. More info on FAQ.
random: Used to generate random choices.
string: Provides constants for letters, digits, and punctuation.
Password Generation Function
Python

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
AI-generated code. Review and use carefully. More info on FAQ.
generate_password(num_letters, num_numbers, num_symbols): Defines a function to generate a password based on the number of letters, numbers, and symbols specified by the user.
password = []: Initializes an empty list to store the password characters.
for _ in range(num_letters): Loops to add the specified number of letters to the password.
for _ in range(num_numbers): Loops to add the specified number of numbers to the password.
for _ in range(num_symbols): Loops to add the specified number of symbols to the password.
random.shuffle(password): Shuffles the list to ensure the characters are in a random order.
return ‘’.join(password): Converts the list to a string and returns the generated password.
User Input and Password Generation
Python

num_letters = int(input("Enter the number of letters: "))
num_numbers = int(input("Enter the number of numbers: "))
num_symbols = int(input("Enter the number of symbols: "))

password = generate_password(num_letters, num_numbers, num_symbols)

print(f"Generated Password: {password}")
AI-generated code. Review and use carefully. More info on FAQ.
Prompts the user to enter the number of letters, numbers, and symbols.
Calls the generate_password function with the user inputs.
Prints the generated password.
This script allows you to customize the composition of your password by specifying the number of letters, numbers, and symbols. Give it a try and let me know if you have any questions or need further assistance!
