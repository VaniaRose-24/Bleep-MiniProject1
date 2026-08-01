from services.inventory_service import *
from services.file_service import *

from services.inventory_service import products

products.extend(load_products())

while True:

    print("""
========== INVENTORY MANAGEMENT ==========

1. Add Product
2. Display Products
3. Search Product
4. Update Product
5. Delete Product
6. Inventory Report
7. Save Products
8. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        product_id = int(input("Product ID : "))
        name = input("Product Name : ")
        price = float(input("Price : "))
        quantity = int(input("Quantity : "))

        add_product(product_id, name, price, quantity)

    elif choice == "2":

        display_products()

    elif choice == "3":

        product_id = int(input("Product ID : "))

        product = search_product(product_id)

        if product:
            product.display()
        else:
            print("Product Not Found")

    elif choice == "4":

        update_product(int(input("Product ID : ")))

    elif choice == "5":

        delete_product(int(input("Product ID : ")))

    elif choice == "6":

        inventory_report()

    elif choice == "7":

        save_products(products)

    elif choice == "8":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")