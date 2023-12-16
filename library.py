def display_menu():
    print("1. Add book")
    print("2. Display available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

def add_book(books, book_title):
    books.append({"title": book_title, "available": True})
    print("Book '{}' added successfully.".format(book_title))

def display_books(books):
    print("Available Books:")
    if not books:
        print("No books available.")
    else:
        for book in books:
            status = "Available" if book["available"] else "Not Available"
            print("{} - {}".format(book['title'], status))

def borrow_book(books, book_title):
    for book in books:
        if book["title"] == book_title and book["available"]:
            book["available"] = False
            print("You have successfully borrowed '{}'.".format(book_title))
            return
    print("Sorry, '{}' is not available for borrowing.".format(book_title))

def return_book(books, book_title):
    for book in books:
        if book["title"] == book_title and not book["available"]:
            book["available"] = True
            print("You have successfully returned '{}'.".format(book_title))
            return
    print("Invalid book title or '{}' is not borrowed.".format(book_title))

def main():
    books = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            book_title = input("Enter the title of the book: ")
            add_book(books, book_title)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            book_title = input("Enter the title of the book you want to borrow: ")
            borrow_book(books, book_title)
        elif choice == "4":
            book_title = input("Enter the title of the book you want to return: ")
            return_book(books, book_title)
        elif choice == "5":
            print("Exiting the library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()