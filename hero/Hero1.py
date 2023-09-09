N = 50
M = 25
K = 3

class Hero:
    def __init__(self, hero_name: str) -> None:
        self.hero_name = hero_name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        self.defended = False # a flag to check if the hero made a defend action for next round


    def get_hero_name(self):
        return self.hero_name
      
    def set_hero_name(self, value):
        self.hero_name = value

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

    def get_coins(self):
        return self.coins
      
    def set_coins(self, value):
        self.coins = value

    def get_defend(self):
        return self.defend
      
    def set_defend(self, value):
        self.defend = value


    def heal(self) -> None:
        # The function will return to our hero N percent of his hp
        self.hp += self.hp * N / 100
        print(f" Healed successfully! The heros hp is: {self.get_hp()}")
        
    
    def level_up(self) -> bool:
        # The function will raise out hero a level. with every level raised, the heros damage and life will raise by M percent and with reset her hp.
        # A level raised is optional only if the hero has K coins from the raised level 
        # The function will return True if the level-up was sucssesful, otherwish, False
        if(self.coins / K >= self.level + 1):
            self.level +=1
            self.hp = 10 + self.level - 1 # restarting the heros hp
            self.hp += self.hp * M / 100 # upgrading the hp
            self.damage += self.damage * M / 100 # upgrading the damage

            print(f"\n The Hero Got Upgraded To Level {self.level}!")
            self.coins -= self.level + 1
            return True

        else:
            print("\nNot Enough Coins For Level Up!")
            return False

    
    def attack(self, monster) -> None:
        # The function gets a monster
        # The function will reduce the monsters hp using the ReduceHealth of that monster. 
        # If the monster is dead, the hero will get a coins by her level
        
        monster.set_hp(monster.reduce_health(monster))
        if monster.get_hp() <= 0:
            self.increase_coins(monster.get_level())
        print("\nThe Hero Attacked!")



    def defend(self) -> None:
        # The function will reduce the damage that the hero will get in 80% in the next attack
        self.hp = self.hp * 1.8
        self.defended = True


    def reduce_health(self, monster) -> int:
        # The function will get a monster.
        # The function will reduce the heros hp by the damage of that monster and if the hero is defending herself.
        # The function will return the life that's left after the fight with the monster 

        if self.defended == True:
            self.hp -= monster.get_damage()
            self.hp = self.hp / 1.8
            self.defend = False

        if (self.hp - monster.get_damage() <= 0):
            self.hp = 0
            return self.hp 

        self.hp -= monster.get_damage()
        return self.hp
    

    def increase_coins(self, coins_amount: int) -> None:
        # The function will get the desired mount to add to the heros coins
        # The function will update the heros coins with the amount of coins to add

        self.coins += coins_amount
        

