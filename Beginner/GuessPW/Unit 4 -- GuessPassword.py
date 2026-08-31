import random
computer_pw=f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"

print("Welcome!\nYou're to guess the password created by the computer!\n\n")
guess=input("Enter a 4-digit PIN code: ")
if guess==computer_pw:
    print("Yayy!\nYou got it right!")
else:
    print(f"Oops!\nYou failed, the computer went with '{computer_pw}'.")
