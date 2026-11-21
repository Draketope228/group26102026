from app.utils.shopping_cart import ShoppingCart


class TestShoppingCart:
    def test_init_creates_empty_items(self):
        cart = ShoppingCart()
        assert cart.items == []

    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item("Milk", 35, 1)

        assert cart.items == [{"name": "Milk", "price": 35, "quantity": 1}]

    def test_add_existing_item_updates_price_and_sums_quantity(self):
        cart = ShoppingCart()
        cart.add_item("Milk", 35, 1)
        cart.add_item("Milk", 40, 2)

        assert cart.items == [{"name": "Milk", "price": 40, "quantity": 3}]

    def test_remove_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("Milk", 35, 1)
        cart.add_item("Bread", 25, 2)

        cart.remove_item("Milk")

        assert cart.items == [{"name": "Bread", "price": 25, "quantity": 2}]

    def test_remove_missing_item_does_nothing(self):
        cart = ShoppingCart()
        cart.add_item("Bread", 25, 2)

        cart.remove_item("Butter")

        assert cart.items == [{"name": "Bread", "price": 25, "quantity": 2}]
