from models.inventory import Inventory

products = []


def add_product(product_id, name, price, quantity):
    products.append(Inventory(product_id, name, price, quantity))
    print("Product Added Successfully")


def display_products():

    if not products:
        print("No Products Found")
        return

    for product in products:
        product.display()


def search_product(product_id):

    for product in products:
        if product.get_id() == product_id:
            return product

    return None


def update_product(product_id):

    product = search_product(product_id)

    if product:

        name = input("New Name : ")
        price = float(input("New Price : "))
        quantity = int(input("New Quantity : "))

        product.set_name(name)
        product.set_price(price)
        product.set_quantity(quantity)

        print("Product Updated Successfully")

    else:

        print("Product Not Found")


def delete_product(product_id):

    global products

    for product in products:

        if product.get_id() == product_id:

            products.remove(product)

            print("Product Deleted Successfully")

            return

    print("Product Not Found")


def inventory_report():

    if not products:
        print("Inventory Empty")
        return

    total_value = 0

    for product in products:

        total = product.get_price() * product.get_quantity()

        total_value += total

        print(
            f"{product.get_name()} : "
            f"{product.get_quantity()} units "
            f"₹{total}"
        )

    print(f"\nTotal Inventory Value : ₹{total_value}")