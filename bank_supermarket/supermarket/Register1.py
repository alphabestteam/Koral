from bank.api import Api

class Register:
    def __init__(self, overall_shopping_list: list, account_name: str, bank_account_number = "0", profit_amount = 0.0 ):
        self.overall_shopping_list = overall_shopping_list
        self.profit_amount = profit_amount
        self.bank_account_number = bank_account_number
        self.bank_name = account_name

        if bank_account_number == "0":
            Api.create_account(self.bank_name, self.profit_amount)

    def __repr__(self) -> str:
        return self.overall_shopping_list
    

    def get_profit_amount(self):
        return self.profit_amount
      
    def set_profit_amount(self, value):
        self.profit_amount = value

    def get_overall_shopping_list(self):
        return self.overall_shopping_list
      
    def set_overall_shopping_list(self, value):
        self.overall_shopping_list = value


    def checkout_costumer(self, costumer) -> None:
        # The function will get a Costumer object and adds to the profit amount the price that costumer had to pat and his buying to the overall shopping list
        self.profit_amount += costumer.get_overall_price()
        """
        check if its possible to add 2 lists like that:
        """
        self.overall_shopping_list += costumer.get_shopping_list() 
        Api.transfer_money(costumer.get_costumer_name(), self.bank_account_number, costumer.get_overall_price(), self.bank_name, self.bank_account_number)
        

    def print_summery(self) -> None:
        # The function will print the profit amount of the register and the shopping list that register made that day.

        print(f"\n The Profit Amount Is : \n {self.profit_amount} \n The Overall Shopping List Is : \n {self.overall_shopping_list}")