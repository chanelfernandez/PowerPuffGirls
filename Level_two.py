def HIM(hp: int, atk: int, defense:int):
    
    first_damage = defense - atk
    damage = first_damage - atk
    print(f"You attacked the monster for {atk} damage")
    return damage
    
def selected_hero(hp, atk, defense):
    
    damage = hp - atk
    print(f"The monster counter attacked for {atk} damage!")
    return damage

# if __name__ == "__main__":
    
#     print("I will always appear")
#     print("I will just appear when ran directly")
#     # monster_attack()

