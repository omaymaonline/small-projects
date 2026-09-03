import os
import time

def clear_screen():
    wait()
    os.system("cls") if os.name == "nt" else os.system("clear")

def wait():
    time.sleep(2)

contacts = {}

print("**** Welcome to the 'Phone Contact Manager'! ****")

while True:
    print("\nMenu:\n1. Add a new contact\n2. View contacts\n3. Edit an existing contact\n4. Delete a contact\n5. Exit")
    
    choice = input("\nEnter a number between 1-5: ")
    while not choice.isdigit():
        choice = input("Please enter a digit! ")
    choice = int(choice)

    if choice == 1:
        contact_id = input("Enter the Contact ID: ")
        while not contact_id.isdigit():
            contact_id = input("Please enter a digit: ")
        while contact_id in contacts:
            contact_id = input("ID already exists in Contacts.\nPlease enter a different one: ")
            while not contact_id.isdigit():
                contact_id = input("Please enter a digit: ")

        name = input("Enter the Contact Name: ")

        phone = input("Enter the Contact Phone Number: ")
        while not phone.isdigit():
            phone = input("Please enter digits only for phone number: ")

        email = input("Enter the Contact Email (optional, press Enter to skip): ")
        if email:
            while "@" not in email or "." not in email:
                email = input("Please enter a valid email address or press Enter to skip: ")
                if email == "":
                    break
        else:
            email = "Not Provided"

        contacts[contact_id] = {"ID": contact_id, "Name": name, "Phone": phone, "Email": email}
        print(f"\nContact: {contacts[contact_id]['Name']} added successfully!")
        clear_screen()

    elif choice == 2:
        if contacts:
            print("\nYour Contacts:\n")
            for i in contacts:
                print(f"ID: {contacts[i]['ID']}, Name: {contacts[i]['Name']}, Phone: {contacts[i]['Phone']}, Email: {contacts[i]['Email']}\n---------------------\n")
            temp = input("Press Enter when done.")
            clear_screen()
        else:
            print("Empty Contacts list.\nNo data stored yet.")
            clear_screen()

    elif choice == 3:
        contact_id = input("Enter the Contact ID you want to edit: ")
        while not contact_id.isdigit():
            contact_id = input("Please enter a digit! ")
        while contact_id not in contacts:
            contact_id = input("ID not found.\nPlease enter a valid one: ")
            while not contact_id.isdigit():
                contact_id = input("Please enter a digit! ")

        new_name = input("Enter new name: ")
        contacts[contact_id]["Name"] = new_name

        new_phone = input("Enter new phone number: ")
        while not new_phone.isdigit():
            new_phone = input("Please enter digits only for phone number: ")
        contacts[contact_id]["Phone"] = new_phone

        new_email = input("Enter new email (press Enter to skip): ")
        if new_email:
            while "@" not in new_email or "." not in new_email:
                new_email = input("Please enter a valid email or press Enter to skip: ")
                if new_email == "":
                    break
            contacts[contact_id]["Email"] = new_email
        print("Contact updated successfully!")
        clear_screen()

    elif choice == 4:
        if contacts:
            contact_id = input("Enter the Contact ID to delete: ")
            while not contact_id.isdigit():
                contact_id = input("Please enter a digit! ")
            while contact_id not in contacts:
                contact_id = input("ID not found.\nPlease enter a valid one: ")
                while not contact_id.isdigit():
                    contact_id = input("Please enter a digit! ")

            confirm = input(f"Are you sure you want to delete '{contacts[contact_id]['Name']}'? (y/n) ").lower()
            if confirm == "y" or confirm == "yes":
                del contacts[contact_id]
                print("Contact deleted successfully!")
            else:
                print("Deletion canceled.")
        else:
            print("Empty Contacts list.\nNo data to delete.")
        clear_screen()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("INVALID OPTION!")
        clear_screen()
