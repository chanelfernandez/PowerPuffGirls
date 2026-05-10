import random

def stage2(player):

    print("\n===== LABORATORY RUINS =====")
    print("A destroyed lab filled with unstable experiments.")
    print("Stronger enemies are lurking in the shadows.\n")

    enemy_name = "HIM"
    enemy_hp = 100
    enemy_atk = 15


    #pang loop ng battle
    while enemy_hp > 0:

        print(f"\nEnemy: {enemy_name}")
        print(f"HP: {enemy_hp}")
        print(f"\nYour Hp: {player['hp']}")

        print("\n1. Attack")
        print("2. Heal")

        action = input("Choose action: ")

        if action == "1":
            damage = random.randint(3, player["atk"])
            enemy_hp -= damage

        elif action == "2":
            player["hp"] += 5

        player["hp"] -= random.randint(1, enemy_atk)

        if player["hp"] <= 0:
            print("GAME OVER")
            exit()

    print("\nStage 2 Cleared!")