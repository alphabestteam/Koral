class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, product):
        for observer in self.observers:
            observer.update(product)


class Observer:
    def update(self, product):
        pass


class Buyer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, product):
        print(f"{self.name} received notification about {product} availability.")


class Store(Subject):
    def add_product(self, product):
        print(f"New product added: {product}")
        self.notify(product)


def main():

    store = Store()

    buyer1 = Buyer("Alice")
    buyer2 = Buyer("Bob")

    store.subscribe(buyer1)
    store.subscribe(buyer2)

    store.add_product("Smartphone")  # This will notify both buyers about the new product
    store.unsubscribe(buyer2)
    print("")

    store.add_product("Laptop")  # Only buyer1 will be notified about the new product

if __name__ == '__main__':
    main()
