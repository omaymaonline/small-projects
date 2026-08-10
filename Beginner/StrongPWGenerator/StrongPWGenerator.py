import random

import string
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

print("Welcome to 'Strong Password Generator'!")

characters=input("How many characters do you want in your password? (Please enter a digit) ")
while not characters.isdigit():
    characters=input("Please enter a digit! ")
characters=int(characters)

number_of_letters=input("How many letters do I include? (Please enter a digit) ")
while not number_of_letters.isdigit():
    number_of_letters=input("Please enter a digit! ")
number_of_letters=int(number_of_letters)

number_of_numbers=input("How many numbers? ")
while not number_of_numbers.isdigit():
    number_of_numbers=input("Please a digit! ")
number_of_numbers=int(number_of_numbers)

number_of_symbols=input("How many symbols? ")
while not number_of_symbols.isdigit():
    number_of_symbols=input("A digit! ")
number_of_symbols=int(number_of_symbols)

if characters!=(number_of_letters+number_of_numbers+number_of_symbols):
    print("Invalid input! The sum of letters, numbers, and symbols doesn't match the password length!")

else:
    password=(
        random.choices(letters,k=number_of_letters) +
        random.choices(numbers,k=number_of_numbers) +
        random.choices(symbols,k=number_of_symbols)
    )

    random.shuffle(password)

    print(f"Your password: {"".join(password)}")