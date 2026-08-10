# Create library
library = []

# First book the user owns
owned_book1 = input("Enter a title of a book you have: ")
if not owned_book1:
    owned_book1=input("Please enter something: ")
    if owned_book1:
        library.append(owned_book1)
else:
    library.append(owned_book1)

# Maybe another book?
owned_book2 = input("Do you own another one? (or press enter) ")
if owned_book2:
    library.append(owned_book2)

# Show them their library
print("\nYour library:", library)

# Create wishlist
wishlist = []

# 1st wishlist
wishlist_1 = input("What book do you wish to have? ")
if wishlist_1 in library:
    wishlist_1 = input("You've already got this book in your library.\nEnter another one (or press enter to skip): ")
if wishlist_1:
    wishlist.append(wishlist_1)

# 2nd wishlist maybe?
wishlist_2 = input("Maybe another book you wish you had? (or press enter to skip) ")
if wishlist_2:
    if wishlist_2 in library:
        wishlist_2 = input("You've already had this book in your library!\nEnter another one (or press enter to skip): ")
    elif wishlist_2 in wishlist:
        wishlist_2 = input("You've already had this book in your wishlist!\nEnter another one (or press enter to skip): ")
    if wishlist_2:
        wishlist.append(wishlist_2)

# Show them their wishlist
print("Your wishlist:", wishlist)

# update wishlist => library?
acquired = input("Enter the name of your book you've acquired from your wishlist (or press enter to skip): ")
if acquired:
    if acquired in library:
        acquired = input("You've already had this book in your library!\nEnter another one (or press enter to skip): ")
    elif acquired not in wishlist:
        confirm = input("This book doesn't exist in your wishlist!\nDo you want me to add it to the library anyway? (y/n): ")
        if confirm.lower() == "y":
            library.append(acquired)
    else:
        library.append(acquired)
        print("Book added successfully!")

# Update library and wishlist
print(f"\nUpdated library: {library}\nUpdated wishlist: {wishlist}")