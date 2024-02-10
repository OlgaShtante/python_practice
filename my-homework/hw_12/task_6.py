from typing import List

class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

class Cart:
    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product) -> None:
        self.items.append(product)

    def remove_item(self, product: Product) -> None:
        if product in self.items:
            self.items.remove(product)

    def get_total(self) -> float:
        total_cost = sum(product.price for product in self.items)
        return total_cost

if __name__ == "__main__":
    product1 = Product("Headphones", 199.99, "Wireless set")
    product2 = Product("Mouse", 89.99, "Wireless mouse with a charger")

    cart = Cart()
    cart.add_item(product1)
    cart.add_item(product2)

    total_cost = cart.get_total()
    print(f"Total cost in the cart: ${total_cost}")

    cart.remove_item(product1)
    updated_total_cost = cart.get_total()
    print(f"Total cost after removing a product from the cart: ${updated_total_cost}")

