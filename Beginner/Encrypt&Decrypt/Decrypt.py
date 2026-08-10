import string

# Character groups
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

print("****** Message Decrypting ******")

encrypted_message = input("\nEnter your encrypted message: ")

# Ensure valid shift number
shift_number = input("Enter the shift number used to encrypt: ")
while not shift_number.isdigit():
    shift_number = input("Please enter a number: ")
shift_number = int(shift_number)

decrypted_message = ""

for char in encrypted_message:
    if char in lowercase:
        new_char = lowercase[(lowercase.index(char) - shift_number) % len(lowercase)]
    elif char in uppercase:
        new_char = uppercase[(uppercase.index(char) - shift_number) % len(uppercase)]
    elif char in digits:
        new_char = digits[(digits.index(char) - shift_number) % len(digits)]
    else:
        new_char = char  # includes symbols and spaces
    decrypted_message += new_char

print(f"\nHere's your decrypted message:\n-----------------\n{decrypted_message}\n-----------------")