import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', '<', '>', '?', '.', '/', '~', '`', ' ']

print("```````````````Welcome to Python Password Generator``````````````````")
n_letters = int(input("How many letters do you want in your password?\n "))
n_symbols = int(input("How many symbols do you want in your password?\n "))
n_numbers = int(input("How many numbers do you want in your password?\n "))

password = []

# Generates the password with the number of letters specified by the user
for char in range(1, n_letters + 1):
    password += random.choice(letters)

# Generates the password with the number of symbols specified by the user
for char in range(1, n_symbols + 1):
    password += random.choice(symbols)

# Generates the password with the number of numbers specified by the user
for char in range(1, n_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)             # Shuffles the password

passwd = ""
for char in password:            # Converts the password to a string
    passwd += char

print(f"Your password is: {passwd}")
