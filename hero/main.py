from Hero1 import Hero
from Monster1 import Monster

def choose_action(action_input: str, hero: Hero, monster: Monster) -> bool:
    # The function will get an input that the hero want to make ( attack , level up , heal, defend ) 
    # The function will return True if the action got done successfully , and False otherwise
    if action_input == "attack":
        hero.attack(monster)

    elif action_input == "level-up":
        if not hero.level_up():
            return False
        
    
    elif action_input == "heal":
        hero.heal()
    
    elif action_input == "defend":
        hero.defend()
    
    else:
        print("\nWrong Input! Try Again!")
        return False
    
    hero.increase_coins(1)
    return True



def main():

    name_hero = input("Please Enter The Heros Name: ")
    hero_generated = Hero(name_hero)

    name_monster = input("Please Enter The Monsters name: ")
    monster_generated = Monster(name_monster, hero_generated.get_level())

    while not hero_generated.get_hp() <= 0:
        print(f"\nThe Hero {name_hero} has {round(hero_generated.get_hp(), 2)} hp!")
        print(f"The Monster {name_monster} has {round(monster_generated.get_hp(), 2)} hp!\n")
        print(f"You Have {hero_generated.get_coins()} coins!\n")

        if(monster_generated.get_hp() <= 0):
            print("You Defeated The Monster! Time To Generate Another One!")
            name_monster = input("Please Enter The Monsters name: ")
            monster_generated = Monster(name_monster, hero_generated.get_level())
            print(f"\nThe Hero {name_hero} has {round(hero_generated.get_hp(), 2)} hp!")
            print(f"The Monster {name_monster} has {round(monster_generated.get_hp(), 2)} hp!\n")

        action = input("\nPlease choose the desired action: \n 'attack' \n 'level-up' \n 'heal' \n 'defend' \nEnter Your Choosing:")
        is_gone_thru = choose_action(action, hero_generated, monster_generated)

        if is_gone_thru and monster_generated.get_hp() > 0: # If the action was made successfully
            monster_generated.attack(hero_generated)


    print("You Have 0 hp :( You Lost!")
        