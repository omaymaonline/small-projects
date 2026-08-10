import os
import time

def clear_screen():
    wait()
    os.system("cls") if os.name == "nt" else os.system("clear")

def wait():
    time.sleep(2)

data_base = {}

print("**** Welcome to the 'Students Database'! ****")

while True:
    print("\nMenu:\n1. Add student\n2. View students\n3. Edit student profile\n4. Delete one profile\n5. Exit")
    
    choice = input("\nEnter a number between 1-5: ")
    while not choice.isdigit():
        choice = input("Please enter a digit! ")
    choice = int(choice)

    if choice == 1:
        id = input("Enter the Student's ID: ")
        while not id.isdigit():
            id = input("Please enter a digit: ")
        while id in data_base:
            id = input("ID already exists in the Database.\nPlease enter a different one: ")
            while not id.isdigit():
                id = input("Please enter a digit: ")
        name = input("Enter the Student's Name: ")
        email = input("Enter the student's Email: ")
        while "@" not in email or "." not in email:
            email = input("Please enter a valid email address: ")
        data_base[id] = {"ID": id, "Name": name, "Email": email}
        print(f"\nStudent: {data_base[id]['Name']} is added successfully to the Database!")
        clear_screen()

    elif choice == 2:
        if data_base:
            for i in data_base:
                print(f"Student: ID: {data_base[i]['ID']}, Name: {data_base[i]['Name']}, Email: {data_base[i]['Email']}\n---------------------\n")
            temporary = input("Please press enter if you're done.")
            clear_screen()
        else:
            print("Empty Database.\nNo DATA is stored yet.")
            clear_screen()

    elif choice == 3:
        id = input("Enter Student ID: ")
        while not id.isdigit():
            id = input("Please enter a digit! ")
        while id not in data_base:
            id = input("ID not available.\nPlease enter a valid ID number: ")
            while not id.isdigit():
                id = input("Please enter a digit! ")

        name_change = input("Enter your new name: ")
        data_base[id]["Name"] = name_change
        email_change = input("Enter your new email: ")
        while "@" not in email_change or "." not in email_change:
            email_change = input("Please enter a valid email: ")
        data_base[id]["Email"] = email_change

        print(f"Profile updated successfully!\nStudent ID: {data_base[id]['ID']}, Name: {data_base[id]['Name']}, Email: {data_base[id]['Email']}")
        clear_screen()
        
    elif choice == 4:
        if data_base:
            id = input("Enter the Student ID to delete: ")
            while not id.isdigit():
                id = input("Please enter a digit! ")
            while id not in data_base:
                id = input("ID not found.\nPlease enter a valid one: ")
                while not id.isdigit():
                    id = input("Please enter a digit! ")
            
            confirm = input(f"Are you sure you want to delete the student '{data_base[id]['Name']}'? (y/n) ").lower()
            if confirm == "y" or confirm == "yes":
                del data_base[id]
                print("Profile deleted successfully!")
            else:
                print("Deletion canceled.")
        else:
            print("Empty Database.\nNo DATA to delete.")
        clear_screen()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("INVALID OPTION!")
        clear_screen()

# Potential Future Updates:
# option 6: Save database to file (text or JSON) either creating it or modifying one which already exists.