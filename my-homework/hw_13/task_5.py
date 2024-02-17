class Storage:
    def save(self, order: 'Order') -> None:
        pass

class Database(Storage):
    def connect(self) -> None:
        print("Connecting to the database")

    def save(self, order: 'Order') -> None:
        print(f"Saving order {order.items} with total {order.total} to the database")

class File(Storage):
    def save(self, order: 'Order') -> None:
        print(f"Saving order {order.items} with total {order.total} to a file")

class Order:
    def __init__(self, items: list, total: float):
        self.items = items
        self.total = total

    def process(self, storage: Storage) -> None:
        storage.save(self)

if __name__ == "__main__":
    order = Order(["Coffee Latte", "Croissant with jam"], 4.98)

    db_storage = Database()
    order.process(db_storage)

    file_storage = File()
    order.process(file_storage)