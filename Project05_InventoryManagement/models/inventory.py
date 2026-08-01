from models.product import Product

class Inventory(Product):

    def display(self):

        print("------------------------------")
        print("Product ID :", self.get_id())
        print("Name       :", self.get_name())
        print("Price      :", self.get_price())
        print("Quantity   :", self.get_quantity())
        print("------------------------------")