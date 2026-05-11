import random

# six seventory
loot = {
    "coins": 0,
    "heal_potion": 0,
    "ss_potion": 0
}

# pag acquire ng coins
def add_coins(level):
    coins = 100 * level
    loot["coins"] += coins
    print(f"\nYou got {coins} coins!")
    return coins

# eto chance ng potion sa size din
def get_loot():
    chance = random.randint(0, 100)

    if chance <= 50:
        loot["heal_potion"] += 1
        print("You found a heal potion!")
        return "heal_potion"

    elif chance <= 70:
        loot["ss_potion"] += 1
        print("You found a Special Skill potion!")
        return "ss_potion" 

# eto pang buy
def heal_potion():
    print("Heal potion cost 50 happy paper")
    if loot["coins"] >= 50:
        loot["coins"] -= 50
        loot["heal_potion"] += 1
        
        print("Bought heal potion!")
        return True
    else:
        print("Not enough Happy Paper!")
    return False

def ss_potion():
    print("Special Skill potion cost 50 happy paper")
    if loot["coins"] >= 100:
        loot["coins"] -= 100
        loot["ss_potion"] += 1
        print("Bought Special Skill potion!")
        return True
    else:
        print("Not enough coins!")
        False
# rewardsssss
def stage_reward(level):
    add_coins(level)
    get_loot()