import json

FILE_NAME = "library_data.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)


def add_book(library):
    book_id = input("Enter Book ID: ")
    if book_id in library:
        print("Book ID already exists!")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library[book_id] = {
        "title": title,
        "author": author,
        "status": "Available"
    }
    save_data(library)
    print("Book added successfully!")


def view_books(library):
    if not library:
        print("No books available.")
        return
    for book_id, details in library.items():
        print(f"\nBook ID: {book_id}")
        print(f"Title: {details['title']}")
        print(f"Author: {details['author']}")
        print(f"Status: {details['status']}")


def issue_book(library):
    book_id = input("Enter Book ID to issue: ")
    if book_id in library and library[book_id]["status"] == "Available":
        library[book_id]["status"] = "Issued"
        save_data(library)
        print("Book issued successfully!")
    else:
        print("Book not available or invalid ID.")


def return_book(library):
    book_id = input("Enter Book ID to return: ")
    if book_id in library and library[book_id]["status"] == "Issued":
        library[book_id]["status"] = "Available"
        save_data(library)
        print("Book returned successfully!")
    else:
        print("Invalid return request.")


def main():
    library = load_data()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_books(library)
        elif choice == "3":
            issue_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


main()
