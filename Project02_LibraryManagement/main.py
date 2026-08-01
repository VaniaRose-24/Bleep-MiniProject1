from services.library_service import *
from services.file_service import save_books
from utils.validator import *

while True:

    print("""
========== LIBRARY MANAGEMENT ==========

1 Add Book
2 Display Books
3 Search Book
4 Update Book
5 Delete Book
6 Issue Book
7 Return Book
8 Save Books
9 Exit
""")

    choice = input("Choice : ")

    if choice == "1":

        book_id = get_int("Book ID : ")
        title = input("Title : ")
        author = input("Author : ")

        add_book(book_id, title, author)

    elif choice == "2":

        display_books()

    elif choice == "3":

        book = search_book(get_int("Book ID : "))

        if book:
            book.display()
        else:
            print("Book Not Found")

    elif choice == "4":

        update_book(get_int("Book ID : "))

    elif choice == "5":

        delete_book(get_int("Book ID : "))

    elif choice == "6":

        issue_book(get_int("Book ID : "))

    elif choice == "7":

        return_book(get_int("Book ID : "))

    elif choice == "8":

        save_books(books)

    elif choice == "9":

        break

    else:

        print("Invalid Choice")