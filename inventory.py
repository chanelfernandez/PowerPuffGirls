from loot import *
import random

def show_inventory():
    print("\n===== INVENTORY =====")
    print(f"Coins: {loot['coins']}")
    print(f"Small Potion: {loot['heal_potion']}")
    print(f"Big Potion: {loot['ss_potion']}")

def use_heal_potion(player):
    if loot["heal_potion"] > 0:
        loot["heal_potion"] -= 1
        player["hp"] += 20
        print("Used Heal Potion (+20 HP)")
    else:
        print("No Heal Potions!")

def use_ss_potion(player):
    if loot["ss_potion"] > 0:
        loot["ss_potion"] -= 1
        #player["hp"] += 50
        print("Used Special Skill Potion")
    else:
        print("No Special Skill Potions!")

def use_coins(player):
    if loot["coins"] > 0:
        loot["coins"] -= 1
        print(f"\nYou have {coins} Happy Paper!")
    else:
        print("No Happy Paper")