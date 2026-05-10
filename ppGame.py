import random
from Level_two import *

# ==============================
# POWERPUFF GIRLS ADVENTURE
# ==============================

print("=" * 50)
print(" WELCOME TO POWERPUFF GIRLS: DEFEND TOWNSVILLE")
print("=" * 50)

# inadd ko lang 'to para formality ng laro haha
print("""
GAME INSTRUCTIONS:
1. Choose your Powerpuff Hero
2. Fight random villains
3. Use Attack, Heal, or Special Skills
4. Defeat enemies to survive
5. Run Away if danger is too high

Good luck saving Townsville!
""")

#Input ng Player
name = input("Enter your name? ").capitalize()



# Main Menu - another option lang din before magstart ang game.
def main_menu():
    while True:

        print("\n====== MAIN MENU ======")
        print("1. Start Game")
        print("2. Shop")
        print("3. Exit")

        main_menu = input("\nChoose option: ").lower()

        # START GAME
        if main_menu == "1" or main_menu == "start game":
            print("\nStarting Game...\n")
            break

        # SHOP
        elif main_menu == "2" or main_menu == "shop":

            print("\n====== SHOP ======")
            print("1. Healing Potion - Restore HP")
            print("2. Special Skill - Increase ATK")
            print("3. Exit Shop")

            shop_choice = input("\nChoose item: ")

            if shop_choice == "1":
                print("You bought a Heal Potion!")

            elif shop_choice == "2":
                print("You bought Special Skill!")

            elif shop_choice == "3":
                print("Leaving Shop...")

            else:
                print("Invalid shop choice!")

        # EXIT
        elif main_menu == "3" or main_menu == "exit" :

            print("\nThanks for playing Powerpuff Girls Adventure!")
            exit()
            break
        else:
            print("\nInvalid menu choice!")
main_menu()

# Dictionary (Name, HP, Attack, Special Attack)
print("\n====== Choose your Hero ======\n")
heroes = {
    "Blossom": {
        "atk": 20,
        "hp": 100,
        "def": 15,
        "ss": 40
    },

    "Bubbles": {
        "atk": 15,
        "hp": 100,
        "def": 10,
        "ss": 40
    },

    "Buttercup": {
        "atk": 25,
        "hp": 100,
        "def": 20,
        "ss": 40
    }
}

#Villain Dictionary
villains = {
    "Princess Morbucks" : {
        "villain_atk" : 10,
        "villain_def" : 5, 
        "villain_hp" : 100
    } ,
    "HIM" : { 
        "villain_atk" : 15,
        "villain_def" : 10, 
        "villain_hp" : 100
    },
    "Fuzzy Lumpkins" : {
        "villain_atk" : 25,
        "villain_def" : 15,
        "villain_hp" : 100
    },
    "Mojo Jojo" : { 
        "villain_atk" : 30,
        "villain_def" : 20, 
        "villain_hp" : 100
    }
}


# Display hero choices
#Characters = ["Blossom", "Bubbles", "Buttercup"]
for num,hero in enumerate(heroes, 1):
    print(num,hero)

while True:

    Characters_choice = input("Select Hero: ").lower()
    if Characters_choice == "blossom" or Characters_choice == "1":
        Cname = "Blossom"
        selected_hero = heroes["Blossom"]
        print("\nHere are the Stats of Blossom:") 
        print("HP: 100")
        print("Attack: 15")
        print("Defense: 10")

    elif Characters_choice == "bubbles" or Characters_choice == "2":
        Cname = "Bubbles"
        selected_hero = heroes ["Bubbles"]
        print("\nHere are the Stats of Bubbles:") 
        print("HP: 100")
        print("Attack: 12")
        print("Defense: 8")

    elif Characters_choice == "buttercup" or Characters_choice == "3":
        Cname = "Buttercup"
        selected_hero = heroes["Buttercup"]
        print("\nHere are the Stats of Buttercup:") 
        print("HP: 100")
        print("Attack: 20")
        print("Defense: 17")

    else: 
        print("Error")
        continue

    confirm = input(f"\nDo you want you use this Character {Cname}? (yes/no): ")

    if confirm == "yes":
        print(f"\n{name} selected {Cname}!")
        break
    else:
        print("choose again...")


# player dictionary para mag store ng stats etc.
print(selected_hero["heroes"])
print(selected_hero["hp"])

print(f"\nWelcome: {selected_hero['hero']}!")
print(f"You chose {selected_hero['heroes']}!")

print(f"HP: {selected_hero['hp']}")
print(f"ATK: {selected_hero['atk']}")
print(f"SP ATK: {selected_hero['splatk']}")



# Loop ng Games 

# while True:

#     # gumamit ng import para auto pick yun kalaban
#     enemy = random.choice(villains)

#     # Tuple unpacking same lang para ma call nman sa enemy parts
#     enemy_name, enemy_hp, enemy_atk, enemy_splatk = enemy

#     print(f"\n Villain Alert! {enemy_name} appeared!")

#     # Battle loop
#     while enemy_hp > 0:

#         print(f"\n{player['heroes']} HP: {player['hp']}")
#         print(f"{enemy_name} HP: {enemy_hp}")

#         display_menu()

#         action = input("\nChoose action: ")

#         # NORMAL ATTACK

#         if action == "1":

#             damage = random.randint(1, player["atk"])
#             enemy_hp -= damage

#             print(f"\n{player['heroes']} attacked {enemy_name}!")
#             print(f"It dealt {damage} damage!")

#         # HEAL the world
#         elif action == "2":

#             heal = random.randint(3, 7)
#             player["hp"] += heal

#             print(f"\n Holy Father healed {player['heroes']} for {heal} HP!")

#         # SPECIAL SKILLS
#         elif action == "3":

#             special_damage = random.randint(10, player["splatk"])
#             enemy_hp -= special_damage

#             print(f"\nSPECIAL ATTACK ACTIVATED!")
#             print(f"{player['heroes']}: used RASENGAN!")
#             print(f"It dealt {special_damage} damage!")

#         # RUN AWAY
#         elif action == "4":

#             print("\nYou flew away safely!")
#             break

#         else:
#             print("\nInvalid action!")
#             continue

#         # Enemy defeated
#         if enemy_hp <= 0:
#             print(f"\n{enemy_name} was defeated!")
#             break

#         # Enemy attacks back
#         enemy_damage = random.randint(1, enemy_atk)
#         player["hp"] -= enemy_damage

#         print(f"\n{enemy_name} attacked back!")
#         print(f"{player['heroes']} lost {enemy_damage} HP!")

#         # Player defeated
#         if player["hp"] <= 0:
#             print(f"\n{player['heroes']} fainted!")
#             print("Townsville is doomed... GAME OVER!")
#             exit()

#     # Continue game
#     again = input("\nDo you want to continue saving Townsville? (y/n): ").lower()

#     if again != "y":
#         print("\nThanks for playing Powerpuff Girls Adventure!")
#         break