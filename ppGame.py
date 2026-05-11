import random

# ==============================
# POWERPUFF GIRLS ADVENTURE
# ==============================

print("=" * 40)
print("   POWERPUFF GIRLS ADVENTURE")
print("=" * 40)

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

# Main Menu - another option lang din before magstart ang game.
while True:

    print("\n====== MAIN MENU ======")
    print("1. Start Game")
    print("2. Shop")
    print("3. Exit")

    main_menu = input("\nChoose option: ")

    # START GAME
    if main_menu == "1":
        print("\nStarting Game...")
        break

    # SHOP
    elif main_menu == "2":

        print("\n====== SHOP ======")
        print("1. Healing Potion - Restore HP")
        print("2. Power Gloves - Increase ATK")
        print("3. Exit Shop")

        shop_choice = input("\nChoose item: ")

        if shop_choice == "1":
            print("You bought a Potion!")

        elif shop_choice == "2":
            print("You bought Power Gloves!")

        elif shop_choice == "3":
            print("Leaving Shop...")

        else:
            print("Invalid shop choice!")

    # EXIT
    elif main_menu == "3":

        print("\nThanks for playing Powerpuff Girls Adventure!")
        exit()

    else:
        print("\nInvalid menu choice!")

# List of Tuples (Name, HP, Attack, Special Attack)

heroes = [
    ("Blossom - Channel Fernandez", 50, 10, 25),
    ("Bubbles - Kimberly David", 45, 7, 30),
    ("Buttercup - Febbie Escoto", 55, 8, 35)
]

villains = [
    ("Russell Nunag", 35, 5, 20),
    ("Lovendin Montero", 40, 6, 25),
    ("Kain Agustin", 32, 5, 30),
    ("Arthur Javier", 38, 4, 35),
]


#Input ng Player
name = input("What is your hero name? ").capitalize()

print("\n====== Choose your Hero ======\n")

# Display hero choices
for i, hero in enumerate(heroes, start=1):
    print(f"{i}. {hero[0]}")

choice = int(input("\nSelect Hero: "))

# tupples to parang nag ccall din ng functions
hero_name, hero_hp, hero_atk, hero_splatk = heroes[choice - 1]

# player dictionary para mag store ng stas etc.
player = {
    "hero": name,
    "heroes": hero_name,
    "hp": hero_hp,
    "atk": hero_atk,
    "splatk": hero_splatk,
}

print(f"\nWelcome: {player['hero']}!")
print(f"You chose {player['heroes']}!")

print(f"HP: {player['hp']}")
print(f"ATK: {player['atk']}")
print(f"SP ATK: {player['splatk']}")

# Battle Menu

menu = [
    "1. Attack",
    "2. Heal",
    "3. Special Skills",
    "4. Run Away"
]

def display_menu():
    print("\n=== ACTIONS ===")
    for item in menu:
        print(item)


# Loop ng Games 

while True:

    # gumamit ng import para auto pick yun kalaban
    enemy = random.choice(villains)

    # Tuple unpacking same lang para ma call nman sa enemy parts
    enemy_name, enemy_hp, enemy_atk, enemy_splatk = enemy

    print(f"\n Villain Alert! {enemy_name} appeared!")

    # Battle loop
    while enemy_hp > 0:

        print(f"\n{player['heroes']} HP: {player['hp']}")
        print(f"{enemy_name} HP: {enemy_hp}")

        display_menu()

        action = input("\nChoose action: ")

        # NORMAL ATTACK

        if action == "1":

            damage = random.randint(1, player["atk"])
            enemy_hp -= damage

            print(f"\n{player['heroes']} attacked {enemy_name}!")
            print(f"It dealt {damage} damage!")

        # HEAL the world
       

        elif action == "2":

            heal = random.randint(3, 7)
            player["hp"] += heal

            print(f"\n Holy Father healed {player['heroes']} for {heal} HP!")

        # SPECIAL SKILLS
     
        elif action == "3":

            special_damage = random.randint(10, player["splatk"])
            enemy_hp -= special_damage

            print(f"\nSPECIAL ATTACK ACTIVATED!")
            print(f"{player['heroes']}: used RASENGAN!")
            print(f"It dealt {special_damage} damage!")

        # RUN AWAY
        elif action == "4":

            print("\nYou flew away safely!")
            break

        else:
            print("\nInvalid action!")
            continue

        # Enemy defeated
        if enemy_hp <= 0:
            print(f"\n{enemy_name} was defeated!")
            break

        # Enemy attacks back
        enemy_damage = random.randint(1, enemy_atk)
        player["hp"] -= enemy_damage

        print(f"\n{enemy_name} attacked back!")
        print(f"{player['heroes']} lost {enemy_damage} HP!")

        # Player defeated
        if player["hp"] <= 0:
            print(f"\n{player['heroes']} fainted!")
            print("Townsville is doomed... GAME OVER!")
            exit()

    # Continue game
    again = input("\nDo you want to continue saving Townsville? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing Powerpuff Girls Adventure!")
        break