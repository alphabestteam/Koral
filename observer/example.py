class Subject:
    # This function maintains a list of observers, 
    # and manage the methods for each observer.

    def __init__(self):
        # This function initializes an empty store to store observers.

        self.observers = []


    def subscribe(self, observer):
        # This function adds an observer to the list of observers
        # who are intrusted in reciving notifications when a new product gets added.

        self.observers.append(observer)


    def unsubscribe(self, observer):
        # This function removes an observer from the observers list.
        # If an observer is no longer interested in receiving notifications, it can unsubscribe using this method.

        self.observers.remove(observer)


    def notify(self, product):
        # This function iterates through the list of observers and calls the update method on each observer,
        # passing along information about the product.
        # This is how the subject informs its observers about changes or events.

        for observer in self.observers:
            observer.update(product)



class Observer:
    # This class serves as a base template for all observers, 
    # and we define a function name which we would like to override later and implement it

    def update(self, product):
        pass



class Buyer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, product):
        # We override the written update function in the observer class
        # do that we can define our specific behavior when the costumers are notified about some changes
        # in our case , if a new product is get added

        print(f"{self.name} received notification about {product} availability.")



class Store(Subject):
    def add_product(self, product):
        # This function manage observers
        #  When a new product is added, the notify method is called, 
        # which iterates over the list of observers and calls their update method, 
        # passing the product as an argument.

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
