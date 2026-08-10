# User: first name, family name, email, password, status "Not verified!" (default).
# Options: 1. Add new user. 2. Display all users. 3. Search and Edit user. 4. Exit.

import os
import time
def clear_screen():
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')

class User:
    def __init__(self, first_name, family_name, email, password):
        self.first_name = first_name
        self.family_name = family_name
        self.email = email
        self.password = password
        self.status = "Not verified!"

    def display(self):
        print(f"\n{self.first_name} {self.family_name}:")
        print("Email:", self.email)
        print("Password:", self.password)
        print("Status:", self.status)

users = []

while True:
    clear_screen()
    print("\n--- MENU ---")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Search and edit user")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nEnter user details:")
        first_name = input("First name: ")
        family_name = input("Family name: ")
        email = input("Email: ")
        password = input("Password: ")

        new_user = User(first_name, family_name, email, password)
        users.append(new_user)
        print("User added successfully!")

    elif choice == "2":
        if not users:
            print("No users found.")
        else:
            print("\n--- Users List ---")
            for user in users:
                user.display()

    elif choice == "3":
        email = input("Enter the email of the user to search: ")
        found = None   # found is empty until we find the user.
        for user in users:
            if user.email == email:
                found = user
                break
        if found:
            print("User found:")
            found.display()
            edit = input("Do you want to edit this user? (y/n): ").lower()
            if edit == "y":
                found.first_name = input("New first name (leave blank to keep current): ") or found.first_name
                found.family_name = input("New family name (leave blank to keep current): ") or found.family_name
                found.email = input("New email (leave blank to keep current): ") or found.email
                found.password = input("New password (leave blank to keep current): ") or found.password
                found.status = "Not verified!"
                print("User updated successfully!")
        else:
            print("No user found with that email.")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")