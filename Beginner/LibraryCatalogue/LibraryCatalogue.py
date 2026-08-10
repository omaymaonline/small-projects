import os
import time

def clear_screen():
    wait()
    os.system("cls") if os.name == "nt" else os.system("clear")

def wait():
    time.sleep(2)

library_catalogue = {}

print("**** Welcome to the Library Catalogue! ****")

while True:
    print("\nMenu:\n1. Add Book\n2. Checkout Book\n3. Checkin Book\n4. List Books\n5. Exit")

    choice = input("\nEnter a number between 1-5: ")
    while not choice.isdigit():
        choice = input("Please enter a digit! ")
    choice = int(choice)

    if choice == 1:  # Add book
        isbn = input("Enter the Book ISBN: ")
        while not isbn.isdigit():
            isbn = input("Please enter a digit: ")
        while isbn in library_catalogue:
            isbn = input("ISBN already exists in the Catalogue.\nPlease enter a different one: ")
            while not isbn.isdigit():
                isbn = input("Please enter a digit: ")

        title = input("Enter the Book Title: ").strip()
        if not title:
            confirm = input("I'll mark this book as 'Untitled'. Would you like to proceed with that? (y/n): ").lower()
            while confirm in ["n", "no"]:
                title = input("Please enter the Book Title: ").strip()
                if title:
                    break
                confirm = input("I'll mark this book as 'Untitled'. Would you like to proceed with that? (y/n): ").lower()
            if not title:
                title = "Untitled"

        author = input("Enter the Author's Name: ").strip()
        if not author:
            confirm = input("I'll mark the author as 'Unknown'. Would you like to proceed with that? (y/n): ").lower()
            while confirm in ["n", "no"]:
                author = input("Please enter the Author's Name: ").strip()
                if author:
                    break
                confirm = input("I'll mark the author as 'Unknown'. Would you like to proceed with that? (y/n): ").lower()
            if not author:
                author = "Unknown"

        library_catalogue[isbn] = {"ISBN": isbn, "Title": title, "Author": author, "Available": True}
        print(f"\nBook '{title}' by {author} added successfully to the Catalogue!")
        clear_screen()

    elif choice == 2:  # Checkout
        if library_catalogue:
            isbn = input("Enter the Book ISBN to checkout: ")
            while not isbn.isdigit():
                isbn = input("Please enter a digit! ")
            while isbn not in library_catalogue:
                isbn = input("ISBN not found.\nPlease enter a valid one: ")
                while not isbn.isdigit():
                    isbn = input("Please enter a digit! ")

            if not library_catalogue[isbn]["Available"]:
                print("This book is already checked out.")
            else:
                library_catalogue[isbn]["Available"] = False
                print(f"Book '{library_catalogue[isbn]['Title']}' checked out successfully.")
        else:
            print("Empty Catalogue.\nNo books available.")
        clear_screen()

    elif choice == 3:  # Checkin
        if library_catalogue:
            isbn = input("Enter the Book ISBN to check in: ")
            while not isbn.isdigit():
                isbn = input("Please enter a digit! ")
            while isbn not in library_catalogue:
                isbn = input("ISBN not found.\nPlease enter a valid one: ")
                while not isbn.isdigit():
                    isbn = input("Please enter a digit! ")

            if library_catalogue[isbn]["Available"]:
                print("This book is already marked as available.")
            else:
                library_catalogue[isbn]["Available"] = True
                print(f"Book '{library_catalogue[isbn]['Title']}' checked in successfully.")
        else:
            print("Empty Catalogue.\nNo books available.")
        clear_screen()

    elif choice == 4:  # List books
        if library_catalogue:
            for i in library_catalogue:
                book = library_catalogue[i]
                status = "Available" if book["Available"] else "Checked out"
                print(f"ISBN: {book['ISBN']}\nTitle: {book['Title']}\nAuthor: {book['Author']}\nStatus: {status}\n----------------------")
            input("Press Enter when done.")
        else:
            print("Empty Catalogue.\nNo books to list.")
        clear_screen()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("INVALID OPTION!")
        clear_screen()