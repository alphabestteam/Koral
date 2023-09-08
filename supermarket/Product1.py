class Product:
    def __init__(self, product_name: str, price_per_unit: int, amount_of_product: int):
        self.product_name = product_name
        self.price_per_unit = price_per_unit
        self.amount_of_product = amount_of_product
        self.overall_price = self.price_per_unit * self.amount_of_product


    def __repr__(self) -> str:
        return self.product_name


    def get_product_name(self):
        return self.product_name
      
    def set_product_name(self, value):
        self.product_name = value

    def get_price_per_unit(self):
        return self.price_per_unit
      
    def set_price_per_unit(self, value):
        self.price_per_unit = value

    def get_amount_of_product(self):
        return self.amount_of_product
      
    def set_amount_of_product(self, value):
        self.amount_of_product = value

    def get_overall_price(self):
        return self.overall_price
      
    def set_overall_price(self, value):
        self.overall_price = value