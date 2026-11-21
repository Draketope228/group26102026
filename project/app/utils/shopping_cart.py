class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        for item in self.items:
            if item["name"] == name:
                item["quantity"] += quantity
                item["price"] = price
                return

        new_item = {
            "name": name,
            "price": price,
            "quantity": quantity,
        }
        self.items.append(new_item)

    def remove_item(self, name):
        updated_items = []
        for item in self.items:
            if item["name"] != name:
                updated_items.append(item)
        self.items = updated_items
