import csv
from models.inventory import Inventory


def save_products(products):

    with open("data/products.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Price", "Quantity"]
        )

        for product in products:

            writer.writerow([
                product.get_id(),
                product.get_name(),
                product.get_price(),
                product.get_quantity()
            ])

    print("Products Saved Successfully")


def load_products():

    products = []

    try:

        with open("data/products.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return products

            for row in rows[1:]:

                products.append(
                    Inventory(
                        int(row[0]),
                        row[1],
                        float(row[2]),
                        int(row[3])
                    )
                )

    except FileNotFoundError:

        pass

    return products