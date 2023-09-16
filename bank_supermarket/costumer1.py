from api import Api

class Costumer:
    def __init__(self, costumer_name: str, overall_price: float, objects_list: list, shopping_list = None, bank_account_number = "0", balance = "0"):
        self.costumer_name = costumer_name
        self.shopping_list = shopping_list
        self.overall_price = overall_price
        self.objects_list = objects_list
        self.bank_account_number = bank_account_number
        self.balance = balance

        if bank_account_number == "0":
            Api.create_account(self, self.costumer_name, self.balance)

    def get_costumer_name(self):
        return self.costumer_name
      
    def set_costumer_name(self, value):
        self.costumer_name = value

    def get_shopping_list(self):
        return self.shopping_list
      
    def set_shopping_list(self, value):
        self.shopping_list = value

    def get_overall_price(self):
        return self.overall_price
      
    def set_overall_price(self, value):
        self.overall_price = value

    def get_objects_list(self):
        return self.objects_list
      
    def set_objects_list(self, value):
        self.objects_list = value

    def add_product(self, product) -> None:
        # The function will get a product object, and would add a product to the costumer shopping list. if the product already exists , the function will sum the amount of units of that product. 
        # Also, the function will update the overall price of that costumer according to the product price and amount.
        
        if self.shopping_list == None:
            self.shopping_list = {}

        is_in_shopping_list = False
        for i in range(len(self.get_shopping_list())):
            for j in range(i):
                if self.shopping_list[i - 1] == self.objects_list[i - 1][0]: # If already exists in the shopping list
                    self.shopping_list[i - 1] += self.objects_list[i - 1][2]
                    is_in_shopping_list = True
                    break

        if not is_in_shopping_list: # If doesn't exists, make a new product object in the shopping list
            self.shopping_list.append([self.objects_list[i - 1][0], self.objects_list[i - 1][2]])
                    

        self.overall_price += self.objects_list[i - 1][2] * self.objects_list[i - 1][1]


    def remove_product(self, product_name: str, amount_to_delete: int) -> None:
        # The function will get the name and amount of units to remove from that product.
        is_wrong_name = True

        if self.shopping_list == None:
            self.shopping_list = {}

        for i in range(len(self.get_shopping_list())):
            for j in range(i):

                if self.shopping_list[i - 1][0] == product_name:
                    print(f"here: {self.shopping_list[i - 1][0]}")
                    print(self.shopping_list[i - 1][1])
                    if self.shopping_list[i - 1][1] - amount_to_delete == 0:
                        self.shopping_list.remove(self.shopping_list[i - 1])
                        self.overall_price -= self.objects_list[i - 1][1] * amount_to_delete
                        return
                    
                    elif self.shopping_list[i][1] - amount_to_delete < 0:
                        print("Wrong Amount! More Then The Current Amount! Try Again! ")
                        return
                    
                    self.shopping_list[i - 1][1] -= amount_to_delete
                    self.overall_price -= self.objects_list[i - 1][1] * amount_to_delete
                    print(f"\n{amount_to_delete} Units Got Deleted From The Product {product_name} ")
                    is_wrong_name = False
                    return

        if is_wrong_name:
            print("Wrong Product Name! Try Again!")
            return

"""
how to reduce the overall price if we send the name and the amount and not the object itself? ??
"""


