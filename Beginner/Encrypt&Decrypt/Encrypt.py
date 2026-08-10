import string

# Character groups
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

print("****** Message Encrypting ******")

message = input("\nEnter your message: ")

# Ensure valid shift number
shift_number = input("Enter the shift number: ")
while not shift_number.isdigit():
    shift_number = input("Please enter a number: ")
shift_number = int(shift_number)

encrypted_message = ""

for i in message:
    if i in lowercase:
        new_char = lowercase[(lowercase.index(i) + shift_number) % len(lowercase)]
    elif i in uppercase:
        new_char = uppercase[(uppercase.index(i) + shift_number) % len(uppercase)]
    elif i in digits:
        new_char = digits[(digits.index(i) + shift_number) % len(digits)]
    else:
        new_char = i  # includes symbols and spaces
    encrypted_message += new_char

print(f"\nHere's your encrypted message:\n-----------------\n{encrypted_message}\n-----------------")