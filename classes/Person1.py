import random

class Person:
    
    def __init__(self):
        self.name = self.generate_name()
        self.id = self.generate_id()
        self.age = self.generate_age()


    def get_name(self):
        return self.name
      
    def set_name(self, value):
        self.name = value
        
    def get_id(self):
        return self.id
      
    def set_id(self, value):
        self.id = value

    def get_age(self):
        return self.age
      
    def set_age(self, value):
        self.age = value

    
    def Print(self):
        print(f"The name is: {self.name}, the id is: {self.id}, the age is: {self.age}")


    def generate_name(self):
        names_list = ["Patrick", "Sandy", "Bobsponge", "Puff"]
        return names_list[random.randint(0, len(names_list) - 1)]
    
    def generate_id(self):
        id_list = [123456789, 987654321, 234567891, 876543219]
        return id_list[random.randint(0, len(id_list) - 1)]
    
    def generate_age(self):
        age_list = [0, 46, 10, 60]
        return age_list[random.randint(0, len(age_list) - 1)]
    