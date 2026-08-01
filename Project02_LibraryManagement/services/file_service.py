import csv

def save_books(books):

    with open("data/books.csv","w",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["ID","Title","Author","Issued"])

        for book in books:

            writer.writerow([
                book.get_id(),
                book.get_title(),
                book.get_author(),
                book.is_issued()
            ])

    print("Books Saved")