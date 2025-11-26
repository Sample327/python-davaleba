import random
import time

def travel_time(distance_km, speed_kmh=5):
    time_hours = distance_km / speed_kmh
    return round(time_hours, 1)


def format_supplies(water_liters, snacks):
    return f"you need {water_liters}L water and {snacks}"


def create_hero():
    name = input("Enter your Heros name: ").strip().title()
    return {
        "name": name,
        "class": "Knight of an order",
        "rank": "Grand Master",
        "gold": 0,
        "hp": 100,
        "xp": 0,
        "inventory": []
}

def create_chest():
    return [
        
            {"name": "sword",
            "damage": 45,
            "description": "Used by King Pharnavazi",
            "rarity": "Legendary"
            },
            {
                "name": "bow",
                "damage": 25,
                "description": "Jin Sakai's bow",
                "rarity": "Epic"
            },
            {
                "name": "axe",
                "damage": 35, 
                "description": "Viking axe of King Ragnar", 
                "rarity": "Rare"
            }
        
    ]


def create_goblin():
    return [
            {
                "name": "Goblin",
                "hp": 50,
                "damage": 5,
                "reward": {
                "xp": 10,
                "gold": 50,
                "item": {"name": "Health Potion", "heal": 100, "rarity": "Common"}
                }
            },
            {
                "name": "Orc",
                "hp": 70,
                "damage": 8,
                "reward": {
                "xp": 20,
                "gold": 80,
                "item": {"name": "Iron Shield", "defense": 5, "rarity": "Uncommon"}
                }
            },
            {
                "name": "Devil",
                "hp": 160,
                "damage": 14,
                "reward": {
                "xp": 150,
                "gold": 200,
                "item": {"name": "Holy Blade", "damage": 30, "rarity": "Epic"}
                }
            }
        ]



def choose_weapon(chest):
    print("\nItems in the chest:")
    for item in chest:
        print(f"- {item['name'].title()}")

    while True:
        choice = input("please choose weapons from the chest: ").strip().lower()

        for item in chest:
            if item["name"].lower() == choice:
                chest.remove(item)
                print(f"You chose the {item['name'].title()}!\n")
                return item

        print("please take existed things from chest")
    
def deal_damage(attacker, defender):
    dmg = attacker.get("damage", 0)
    defender["hp"] -= dmg

    if defender["hp"] < 0:
        defender["hp"] = 0
    print(f"{attacker["name"]} hits {defender["name"]} for {dmg} damage.({defender['hp']} HP left) ")

    return defender

def is_defeated(character):
    return character["hp"] <= 0



def run_battle(hero, goblin, weapon):
    print(f"\nA {goblin['name']} appears prepare for battle ")

    hero_attack = {
        "name": hero["name"],
        "damage": weapon["damage"]
    }

    while hero["hp"] > 0 and goblin["hp"] > 0:
        print("your turn")
        action = input("attack or defend?: ").strip().lower()

        if action == "attack":
            deal_damage(hero_attack,goblin)
            if is_defeated(goblin):
                print("victory, you win")
                return "victory"

        elif action == "defend":
            goblin_attack = {
                "name": goblin["name"],
                "damage": goblin["damage"] // 2
            }
            deal_damage(goblin_attack,hero)
            if is_defeated(hero):
                print("you are defeated.")
                return "defeat"
            continue
        else:
            print("please choose attack or defend")

    return "victory" if goblin["hp"] == 0 else "defeat"


def apply_reward(hero, reward):
    hero["xp"] += reward["xp"]
    hero["gold"] += reward["gold"]
    hero["inventory"].append(reward["item"])
    print(f"\nReward received:")
    print(f"+{reward['xp']} XP")
    print(f"+{reward['gold']} gold")
    print(f"Item found: {reward['item']['name']}\n")

def show_defeat_summary(hero, chest):
    print("\n=== DEFEAT SUMMARY ===")
    print("Your hero has fallen. The kingdom is doomed.")
    print("\nRemaining chest items:")
    for item in chest:
        print(f"- {item["name"]}")


hero = create_hero()
chest = create_chest()
monsters = create_goblin()

print(f"\nWelcome, {hero['name']} the {hero['class']}!\n")

weapon = choose_weapon(chest)
hero["inventory"].append(weapon)


enemy = random.choice(monsters)

result = run_battle(hero, enemy, weapon)

if result == "victory":
    apply_reward(hero, enemy["reward"])
else:
    show_defeat_summary(hero, chest)
