from costumer1 import Costumer
from product1 import Product
from register1 import Register

def main():
    juice = Product("Juice", 3, 4)
    chocolate = Product("chocolate", 7, 5)
    milk = Product("milk", 6, 3)
    eggs = Product("eggs", 5, 3)
    water = Product("water", 3, 10)

    overall_price_for_janice = (
        juice.get_overall_price()
        + chocolate.get_overall_price()
        + milk.get_overall_price()
        + eggs.get_overall_price()
    )

    Janice = Costumer(
        "Janice", overall_price_for_janice,  [[juice, juice.get_amount_of_product()], [chocolate, chocolate.get_amount_of_product()], [milk, milk.get_amount_of_product()], [eggs, eggs.get_amount_of_product()]] , [juice , chocolate, milk, eggs], "0", 200
    )
    print(f"\n*Before adding a product:* \n Janices shopping list: \n {Janice.get_shopping_list()}\n Janices overall price {Janice.get_overall_price()}")
    
    Janice.add_product(water)

    print(f"\n*After adding a product:* \n Janices shopping list: \n {Janice.get_shopping_list()}\n Janices overall price {Janice.get_overall_price()}")

    Janice.remove_product("milk", 3)

    print(f"\n*After removing a product:* \n Janices shopping list: \n {Janice.get_shopping_list()}\n Janices overall price {Janice.get_overall_price()}")

    Janice.remove_product("milk", 3)

    print(f"\n*After removing a product:* \n Janices shopping list: \n {Janice.get_shopping_list()}\n")


    register1 = Register(Janice.get_shopping_list(),"bank name", "0", Janice.get_overall_price())
    register1.checkout_costumer(Janice)
    register1.print_summery()
    

if __name__ == "__main__":
    main()
