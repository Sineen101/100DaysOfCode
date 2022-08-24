logo = """           
  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |  _________   | || |    _______   | || |      __      | || |  _______     | |
| |   .' ___  |  | || |     /  \     | || | |_   ___  |  | || |   /  ___  |  | || |     /  \     | || | |_   __ \    | |
| |  / .'   \_|  | || |    / /\ \    | || |   | |_  \_|  | || |  |  (__ \_|  | || |    / /\ \    | || |   | |__) |   | |
| |  | |         | || |   / ____ \   | || |   |  _|  _   | || |   '.___`-.   | || |   / ____ \   | || |   |  __ /    | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |  _| |___/ |  | || |  |`\____) |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
| |   `._____.'  | || ||____|  |____|| || | |_________|  | || |  |_______.'  | || ||____|  |____|| || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     _____    | || |   ______     | || |  ____  ____  | || |  _________   | || |  _______     | |
| |   .' ___  |  | || |    |_   _|   | || |  |_   __ \   | || | |_   ||   _| | || | |_   ___  |  | || | |_   __ \    | |
| |  / .'   \_|  | || |      | |     | || |    | |__) |  | || |   | |__| |   | || |   | |_  \_|  | || |   | |__) |   | |
| |  | |         | || |      | |     | || |    |  ___/   | || |   |  __  |   | || |   |  _|  _   | || |   |  __ /    | |
| |  \ `.___.'\  | || |     _| |_    | || |   _| |_      | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |   `._____.'  | || |    |_____|   | || |  |_____|     | || | |____||____| | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def cipher():  # The main function
    # Ask the user to input the direction of the cipher
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # The message is converted to lowercase
    text = input("Type your message:\n").lower()
    # The shift number is converted to an integer
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)  # The caeser function is called


def caeser(plain_text, shift_key, command):  # Encrypt or decrypt the message
    if shift_key > 25:  # If the shift key is greater than 25, it will loop back to the beginning of the alphabet
        shift_key = shift_key % 25
    cipher_text = ""
    new_position = 0
    for letter in plain_text:   # For each letter in the plain text
        if letter not in alphabet:  # If the letter is not in the alphabet
            cipher_text += letter  # Add the letter to the cipher text
        else:
            # Find the position of the letter in the alphabet
            position = alphabet.index(letter)
        if command == "encode":  # If the command is encode, the letter is shifted by the shift key
            # The new position is the old position plus the shift key
            new_position = position + shift_key
        elif command == "decode":   # If the command is decode, the letter is shifted by the negative of the shift key
            # The negative of the shift key is subtracted from the position of the letter
            new_position = position - shift_key
        # The new letter is added to the cipher text
        else:
            print("Invalid command")
            cipher()
        cipher_text += alphabet[new_position]
        # The cipher text is printed
    print(f"Your {command}d message is {cipher_text}")
    restart = input("Would you like to restart? (y/n)\n ")
    if restart == "y":
        cipher()
    else:
        print("Thank you for using the Caesar Cipher!")


print(logo)
cipher()  # The main function is called to start the program
