print("Welcome to 'Shop Calc'!")
items_number = input("How many items are there in your basket? (Enter a digit) ")

while not items_number.isdigit():
    items_number = input("Please enter a digit! ")
items_number = int(items_number)

print("Let's start calculating: ")

items = []
prices = []
for i in range(1, items_number + 1):
    name = input(f"What's the name of the item number '{i}'? ")
    price = input(f"How much did the '{name}' cost you? (Please enter a digit) $ ")

# Keep asking until the user enters a valid numeric value (int or float)
    while True:
        try:
            price = float(price)
            break
        except ValueError:
            price = input("Please enter a valid number! $ ")

    items.append(name)
    prices.append(price)

see_items = input("Do you want to see your items? (y/n) ").lower()
if see_items == 'y' or see_items == 'yes':
    print(", ".join(items))
else:
    print("Okay.")

see_cost = input("Do you want to see how much it'll cost you? (y/n) ").lower()
if see_cost == 'y' or see_cost == 'yes':
    print(sum(prices), "$")
else:
    print("Okay.")
