import random

P = 0.5 # Proportion constant 

class Monster:
    def __init__(self, monster_name: str, current_hero_level: int) -> None:
        self.monster_name = monster_name
        self.current_hero_level = current_hero_level
        self.level = self.generate_level()
        self.hp = self.generate_hp_damage()
        self.damage = self.generate_hp_damage()


    def get_monster_name(self):
        return self.monster_name
      
    def set_monster_name(self, value):
        self.monster_name = value   

    def get_hp(self):
        return self.hp
      
    def set_hp(self, value):
        self.hp = value   

    def get_damage(self):
        return self.damage
      
    def set_damage(self, value):
        self.damage = value

    def get_level(self):
        return self.level
      
    def set_level(self, value):
        self.level = value

    def get_current_hero_level(self):
        return self.current_hero_level
      
    def set_current_hero_level(self, value):
        self.current_hero_level = value



    def generate_level(self) -> int:
        # The function will generate a level for the monster
        # The monsters level supposed to be the same or one less / more then the heros level
        # The function will return the generated level of the monster
        if self.current_hero_level == 1:
            return random.randint(self.current_hero_level, self.current_hero_level + 1)
        return random.randint(self.current_hero_level - 1 , self.current_hero_level + 1)


    def generate_hp_damage(self) -> int:
        # The function will generate the hp and level of the monster
        # The function will generate hp and damage proportion to the level of the monster
        # The function will return the generated hp / damage
        return self.get_level() / P 


    def attack(self, hero) -> None:
        # The function gets a hero
        # The function will reduce our heros hp using the ReduceHealth of that monster. 

        hero.reduce_health(Monster(self.get_monster_name(), hero.get_level()))
        print("\nThe Monster Attacked!")
        print(f"\n The Heros hp is: {round(hero.get_hp(), 2)}")


    def reduce_health(self, hero) -> int:
        # The function will get a hero
        # The function will reduce to the monster hp according to the heros damage
        # The function will return the left hp of the monster

        if (self.hp - hero.get_damage() <= 0):
            self.set_hp(0)
            return self.get_hp()
        print(hero.get_damage())
        self.set_hp(self.get_hp() - hero.get_damage())
        return self.get_hp()
    
        

