import random
from loot import *

def stage2(player):
    print("\n===== LABORATORY RUINS =====")
    print("A destroyed lab filled with unstable experiments.")
    print("Stronger enemies are lurking in the shadows.\n")
    
    enemy_name = "HIM"
    enemy_hp = 100
    enemy_atk = 15
    
    # pang loop ng battle
    while enemy_hp > 0:
        print(f"\nEnemy: {enemy_name}")
        print(f"HP: {enemy_hp}")
        print(f"\nYour HP: {player['hp']}")
        
        print("\n1. Attack")
        print("2. Heal")
        print("3. Special Skill")
    
        
        action = input("Choose action: ")
        
        if action == "1":
            # NORMAL ATTACK
            damage = random.randint(3, player["atk"])
            enemy_hp -= damage
            print(f"You dealt {damage} damage!")
        
        elif action == "2":
            # HEAL ACTION
            if loot["heal_potion"] > 0:
                loot["heal_potion"] -= 1

                heal = random.randint(5, 50)
                player["hp"] = min(player["hp"] + heal, 100)
                print(f"You healed {heal} HP!")
            else:
                print("\n=========================")
                print("Insufficient Heal Potions!")
                print("=========================\n")

        elif action == "3":
            if loot["ss_potion"] > 0:
                loot["ss_potion"] -= 1

            # SPECIAL SKILL ACTION
                special_damage = random.randint(10, player.get("splatk", 50))
                enemy_hp -= special_damage
                print(f"\n SPECIAL SKILL ACTIVATED! ")
                print(f"You used a powerful attack!")
                print(f"It dealt {special_damage} damage!")
            else:
                print("Insufficient Special Skill Potions!")
        

        
        else:
            print("Invalid action! Try again.")
            continue
        
        # Enemy attacks back (if buhay pa)
        if enemy_hp > 0:
            enemy_damage = random.randint(1, enemy_atk)
            player["hp"] -= enemy_damage
            print(f"\n{enemy_name} attacked you for {enemy_damage} damage!")
        
        # Check if player is defeated
        if player["hp"] <= 0:
            print("\n" + "="*30)
            print("GAME OVER")
            print("="*30)
            exit()
    
    print("\n" + "="*30)
    print("Stage 2 Cleared! Victory!")
    print("="*30)
    
    # # Reward for clearing stage (ONLY ON VICTORY)
    # reward = random.randint(50, 100)
    # player["hp"] += 20  # Heal player after victory
    # player["coins"] = player.get("coins", 0) + reward
    
    # print(f"\nYou gained {reward} coins!")
    # print(f"Your HP was restored to {player['hp']}")
    
    return "\nYou defeated the HIM!"