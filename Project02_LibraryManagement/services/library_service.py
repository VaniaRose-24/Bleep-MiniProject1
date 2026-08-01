from models.book import Book

books = []

def add_book(book_id, title, author):

    books.append(Book(book_id, title, author))

    print("Book Added Successfully")


def display_books():

    if not books:
        print("No Books Available")
        return

    for book in books:
        book.display()


def search_book(book_id):

    for book in books:

        if book.get_id() == book_id:
            return book

    return None


def update_book(book_id):

    book = search_book(book_id)

    if book:

        title = input("New Title : ")
        author = input("New Author : ")

        book.set_title(title)
        book.set_author(author)

        print("Updated Successfully")

    else:

        print("Book Not Found")


def delete_book(book_id):

    global books

    for book in books:

        if book.get_id() == book_id:

            books.remove(book)

            print("Deleted Successfully")

            return

    print("Book Not Found")


def issue_book(book_id):

    book = search_book(book_id)

    if book:

        if book.is_issued():

            print("Already Issued")

        else:

            book.issue()

            print("Book Issued")

    else:

        print("Book Not Found")


def return_book(book_id):

    book = search_book(book_id)

    if book:

        book.return_book()

        print("Book Returned")

    else:

        print("Book Not Found")