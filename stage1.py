import random
from loot import*

def stage1(player):

    print("\n===== TOWNSVILLE STREETS =====")
    print("You are now in the streets of Townsville. Something feels wrong...")
    print("A cute little girl, but she seems grumpy. Be Prepared!")

    enemy_name = "Princess Morbucks"
    enemy_hp = 100
    enemy_atk = 10


    # pang loob ng battle
    while enemy_hp > 0:

        print(f"\nEnemy: {enemy_name}")
        print(f"Enemy HP: {enemy_hp}")
        print(f"\nYour Hp: {player['hp']}")

        print("\n1. Attack")
        print("2. Heal")
        print("3. Special Skill")

        action = input("Choose action: ")

        # launch attack ko
        if action == "1":

            damage = random.randint(1, player["atk"])
            enemy_hp -= damage

            print(f"You dealt {damage} damage!")

        # healing for everyone
        elif action == "2":

            if loot["heal_potion"] > 0:
                loot["heal_potion"] -= 1

                heal = random.randint(10, 25)
                player["hp"] += heal

                print(f"You used Heal Potion (+{heal} HP)")
            else:
                print("No Heal Potions!")

        # SPECIAL SKILL 
        elif action == "3":

            if loot["ss_potion"] > 0:
                loot["ss_potion"] -= 1

                damage = random.randint(15, 40)
                enemy_hp -= damage

                print(f"You used Special Skill Potion! (-{damage} HP enemy)")
            else:
                print("No Special Skill Potions!")

        # launch attack ng enemy
        enemy_damage = random.randint(1, enemy_atk)
        player["hp"] -= enemy_damage

        print(f"Enemy hit you for {enemy_damage}")

        # pag namatay
        if player["hp"] <= 0:
            print("GAME OVER")
            exit()

    print("\nYou defeated the grumpy princess!")