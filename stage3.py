import random

def stage3(player):

    print("\n===== MOJO JOJO'S LAIR =====")
    print("The final battlefield. Everything ends here.")
    print("Defeat the boss to save Townsville.\n")

    enemy_name = "Mojo Jojo"
    enemy_hp = 150
    enemy_atk = 20


    #pang loop ng battle
    while enemy_hp > 0:

        print(f"\nBOSS: {enemy_name}")
        print(f"HP: {enemy_hp}")
        print(f"\nYour Hp: {player['hp']}")

        print("\n1. Attack")
        print("2. Heal")
        print("3. Special")

        action = input("Choose action: ")

        if action == "1":
            enemy_hp -= random.randint(5, player["atk"])

        elif action == "2":
            player["hp"] += 10

        elif action == "3":
            enemy_hp -= player["ss"]

        player["hp"] -= random.randint(5, enemy_atk)

        if player["hp"] <= 0:
            print("GAME OVER")
            exit()

    print("\nYOU SAVED TOWNSVILLE! GAME COMPLETED!")