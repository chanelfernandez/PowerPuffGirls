import random

def stage1(player):

    print("\n===== TOWNSVILLE STREETS =====")
    print("You are now in the streets of Townsville. Something feels wrong...")
    print("A cute little girl, but she seems grumpy. Be Prepared!")

    enemy_name = "Princess Morbucks"
    enemy_hp = 80
    enemy_atk = 10


    # pang loob ng battle
    while enemy_hp > 0:

        print(f"\nEnemy: {enemy_name}")
        print(f"Enemy HP: {enemy_hp}")
        print(f"\nYour Hp: {player['hp']}")

        print("\n1. Attack")
        print("2. Heal")

        action = input("Choose action: ")

        # launch attack ko
        if action == "1":

            damage = random.randint(1, player["atk"])
            enemy_hp -= damage

            print(f"You dealt {damage} damage!")

        # healing for everyone
        elif action == "2":

            heal = random.randint(5, 10)
            player["hp"] += heal

            print(f"You healed {heal} HP!")

        # launch attack ng enemy
        enemy_damage = random.randint(1, enemy_atk)
        player["hp"] -= enemy_damage

        print(f"Enemy hit you for {enemy_damage}")

        # pag namatay
        if player["hp"] <= 0:
            print("GAME OVER")
            exit()

    print("\nYou defeated the grumpy princess!")