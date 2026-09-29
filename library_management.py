books = {}
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books[book_id] = [title, author, "Available"]
    print("Book added successfully.")
def display_books():
    if len(books) == 0:
        print("No books found.")
    else:
        for book_id in books:
            data = books[book_id]
            print("Book ID:", book_id)
            print("Title:", data[0])
            print("Author:", data[1])
            print("Status:", data[2])
def search_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        data = books[book_id]
        print("Book Found")
        print("Book ID:", book_id)
        print("Title:", data[0])
        print("Author:", data[1])
        print("Status:", data[2])
    else:
        print("Book not found.")
def issue_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        if books[book_id][2] == "Available":
            books[book_id][2] = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")
def return_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        if books[book_id][2] == "Issued":
            books[book_id][2] = "Available"
            print("Book returned successfully.")
        else:
            print("Book is already available.")
    else:
        print("Book not found.")
def delete_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        del books[book_id]
        print("Book deleted successfully.")
    else:
        print("Book not found.")
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        delete_book()
    elif choice == 7:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
