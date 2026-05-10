import random
from stage1 import stage1
from stage2 import stage2
from stage3 import stage3
from confirm import confirm_choice
from loot import loot, stage_reward

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

# Main Menu - another option lang din before magstart ng game.
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
for num, hero in enumerate(heroes, 1):
    print(num, hero)

selected_hero = None
Cname = None

while True:

    Characters_choice = input("Select Hero: ").lower()

    if Characters_choice == "blossom" or Characters_choice == "1":
        Cname = "Blossom"
        selected_hero = heroes["Blossom"]

        print("\nHere are the Stats of Blossom:") 
        print("HP: 100")
        print("Attack: 20")
        print("Defense: 15")

    elif Characters_choice == "bubbles" or Characters_choice == "2":
        Cname = "Bubbles"
        selected_hero = heroes["Bubbles"]

        print("\nHere are the Stats of Bubbles:") 
        print("HP: 100")
        print("Attack: 15")
        print("Defense: 10")

    elif Characters_choice == "buttercup" or Characters_choice == "3":
        Cname = "Buttercup"
        selected_hero = heroes["Buttercup"]

        print("\nHere are the Stats of Buttercup:") 
        print("HP: 100")
        print("Attack: 25")
        print("Defense: 20")

    else: 
        print("Error")
        continue

    if confirm_choice(f"\nDo you want to use this Character {Cname}?"):
        print(f"\n{name} selected {Cname}!")
        break
    else:
        print("choose again...")

# player dictionary para mag store ng stats etc.
player = {
    "name": name,
    "hero": Cname,
    "hp": selected_hero["hp"],
    "atk": selected_hero["atk"],
    "def": selected_hero["def"],
    "ss": selected_hero["ss"]
}

print("\n===== PLAYER INFO =====")
print(f"Hero: {player['hero']}")
print(f"HP: {player['hp']}")
print(f"ATK: {player['atk']}")
print(f"DEF: {player['def']}")
print(f"SS: {player['ss']}")

# checkpoint system
def continue_game(stage_name):
    if confirm_choice(f"Do you want to continue to {stage_name}?"):
        print(f"\nEntering {stage_name}...\n")
        return True
    else:
        print("\nGame stopped. Thanks for playing!")
        return False

# dito yung flow pwede edit dito for example may edit kayo after ng isang stage
print("\nEntering Stage 1")

stage1(player)
stage_reward(1)

if not continue_game("Stage 2"):
    main_menu()
    exit()

stage2(player)
stage_reward(2)

if not continue_game("Final Boss"):
    main_menu()
    exit()

print("\nEntering Stage 3 (FINAL BOSS)")
stage3(player)
stage_reward(3)