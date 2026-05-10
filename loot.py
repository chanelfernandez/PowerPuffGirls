import random

# six seventory
loot = {
    "coins": 0,
    "small_potion": 0,
    "big_potion": 0
}

# pag acquire ng coins
def add_coins(level):
    coins = 100 * level
    loot["coins"] += coins
    print(f"\nYou got {coins} coins!")

# eto chance ng potion sa size din
def get_loot():
    chance = random.randint(1, 100)

    if chance <= 50:
        loot["small_potion"] += 1
        print("You found a small potion!")

    elif chance <= 70:
        loot["big_potion"] += 1
        print("You found a big potion!")

# eto pang buy
def buy_small():
    if loot["coins"] >= 50:
        loot["coins"] -= 50
        loot["small_potion"] += 1
        print("Bought small potion!")
    else:
        print("Not enough coins!")

def buy_big():
    if loot["coins"] >= 100:
        loot["coins"] -= 100
        loot["big_potion"] += 1
        print("Bought big potion!")
    else:
        print("Not enough coins!")

# rewardsssss
def stage_reward(level):
    add_coins(level)
    get_loot()