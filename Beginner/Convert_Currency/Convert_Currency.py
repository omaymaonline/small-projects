import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def wait(seconds=2):
    time.sleep(seconds)

currencies = {
    "USD": 1.00,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.36,
    "DZD": 134.27,
    "CAD": 1.37
}

print("**** Welcome to the Currency Converter ****")

while True:
    print("\nMenu:\n1. View available currencies\n2. Convert currency\n3. Add or update currency rate\n4. Delete a currency\n5. Exit")

    choice = input("\nEnter a number between 1–5: ")
    while not choice.isdigit():
        choice = input("Please enter a digit! ")
    choice = int(choice)

    if choice == 1:
        print("\nAvailable currencies (USD-based):")
        for code, rate in currencies.items():
            print(f"{code}: {rate}")
        input("\nPress Enter to continue...")
        clear_screen()

    elif choice == 2:
        print("\nConvert between currencies")
        from_curr = input("Enter source currency (e.g. USD): ").upper()
        while from_curr not in currencies:
            from_curr = input("Currency not available. Enter valid code: ").upper()

        to_curr = input("Enter target currency (e.g. EUR): ").upper()
        while to_curr not in currencies:
            to_curr = input("Currency not available. Enter valid code: ").upper()

        while True:
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Invalid input. Try again.")

        if currencies[from_curr] == 0:
            print("Error: base currency rate cannot be 0.")
        else:
            converted = (amount / currencies[from_curr]) * currencies[to_curr]
            print(f"\n{amount:.2f} {from_curr} = {converted:.2f} {to_curr}")
        input("\nPress Enter to continue...")
        clear_screen()

    elif choice == 3:
        print("\nAdd or update currency rate")
        code = input("Enter currency code (e.g. USD): ").upper()
        while True:
            rate = input("Enter rate compared to USD: ")
            try:
                rate = float(rate)
                break
            except ValueError:
                print("Invalid input. Try again.")
        currencies[code] = rate
        print(f"Currency '{code}' updated successfully!")
        input("\nPress Enter to continue...")
        clear_screen()

    elif choice == 4:
        if currencies:
            code = input("Enter currency code to delete: ").upper()
            while code not in currencies:
                code = input("Currency not found. Enter a valid one: ").upper()
            confirm = input(f"Delete '{code}'? (y/n): ").lower()
            if confirm in ["y", "yes"]:
                del currencies[code]
                print("Currency deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("No currencies stored.")
        input("\nPress Enter to continue...")
        clear_screen()

    elif choice == 5:
        print("Exiting program...")
        wait()
        break

    else:
        print("INVALID OPTION!")
        wait()
        clear_screen()