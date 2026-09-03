# 📚 Library Catalogue

A small Python project that simulates a simple library catalogue. Users can add books, check books out, check them back in, and view all books in the catalogue through a menu-driven program.

## ✨ Features

* Add books using their ISBN, title, and author
* Prevent duplicate ISBNs
* Checkout available books
* Check in borrowed books
* List all books with their current availability
* Validate user input
* Handle empty titles and authors with default values
* Clear the screen between actions
* Exit the programme through the menu

## 🧠 Concepts

`import` · `os` · `time` · `functions` · `while loops` · `for loops` · `dictionaries` · `nested dictionaries` · `input()` · `isidigit()` · `if/elif/else` · `dictionary keys` · `dictionary values` · `boolean values` · `functions with no parameters` · `f-strings`

## ▶️ How It Works

The programme starts with an empty library catalogue and continuously displays a menu:

```text
1. Add Book
2. Checkout Book
3. Checkin Book
4. List Books
5. Exit
```

### Add Book

The user enters an ISBN, title, and author. The ISBN must be unique, while empty titles and authors are given default values of `"Untitled"` and `"Unknown"`.

Each book is stored in the catalogue using its ISBN as the key.

### Checkout Book

The user enters the ISBN of a book. If the book is available, its status is changed to unavailable.

### Checkin Book

The user enters the ISBN of a book. If it is checked out, its status is changed back to available.

### List Books

The programme loops through the catalogue and displays each book's ISBN, title, author, and current status.

## 🛠️ Modules Used

* `os` — used to clear the terminal screen.
* `time` — used to pause the programme before clearing the screen.

## 🎯 What I Practised

This project brings together loops, functions, dictionaries, input validation, conditionals, and Boolean values to build a complete menu-driven programme.
