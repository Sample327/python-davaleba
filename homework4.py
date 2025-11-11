import random
import time


story = """
Really long time ago there was one crazy scientist who accidentally opened a portal
to another dimension. After that, from that portal came three deadly monsters.
Goblin,Orc and the Devil.
They destroyed entire regions, and only the knights were brave enough to fight them back.
Unfortunately, every knight was killed by the monsters.
They headed toward the kingdom, and only one knight remained alive — 
a hero. People believed in him, and his last mission is to kill all the monsters.

You have to be that hero... so let's begin.
"""

for char in story:
    print(char, end="", flush=True)
    time.sleep(0.04)

name = input("\nEnter your hero's name: ").strip().title()

hero = {
    "name": name,
    "class": "Knight of an order",
    "rank": "Grand Master",
    "gold": 0,
    "hp": 100,
    "xp": 0,
    "inventory": []
}

print("\nYour character sheet:")
for key, value in hero.items():
    print(f"{key}: {value}")


chest = [
    {"name": "sword",
     "damage": 45,
     "description": "Used by King Pharnavazi",
     "rarity": "Legendary"
    },
    {"name": "bow",
     "damage": 25,
     "description": "Jin Sakai's bow",
     "rarity": "Epic"
      },
    {"name": "axe",
     "damage": 35, 
     "description": "Viking axe of King Ragnar", 
     "rarity": "Rare"
     }
]

print("\nYou open a wooden chest. Inside you see:")
for item in chest:
    print(f"- {item['name'].title()} ({item['description']})")


while True:
    choice = input("\nChoose one of the weapons: ").strip().lower()
    chosen_item = None 

    for item in chest:
        if item["name"].lower() == choice:
            chosen_item = item
            break  

    if chosen_item:
        hero["inventory"].append(chosen_item)
        chest.remove(chosen_item)
        print(f"Congrats! You equipped the {chosen_item['name']}.\n")
        break
    else:
        print("That item is not in the chest. Try again!")

weapon_damage = hero["inventory"][0]["damage"]
weapon_name = hero["inventory"][0]["name"]

# titqos gasagebia magram bolomde ver vxvdebi nul indexs rato vwert

monsters = [
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


for devil in monsters:
    print(f"\nA {devil['name']} appears! Prepare for battle!")
    while hero["hp"] > 0 and devil["hp"] > 0:
        action = input("Do you want to attack, defend, or hide?: ").strip().lower()

        if action == "attack":
            random_reduce = random.randint(0, weapon_damage)
            damage_done = weapon_damage - random_reduce

            if damage_done == 0:
                print("You swing wildly and miss!")
            elif random_reduce == 0:
                print("A perfect strike!")
            else:
                print(f"You hit the {devil['name']} for {damage_done} damage!")

            devil["hp"] -= damage_done
            if devil["hp"] < 0:
                devil["hp"] = 0
            print(f"{devil['name']} HP: {devil['hp']}")

            if devil["hp"] == 0:
                print(f"\nYou have slain the {devil['name']}!")
                hero["xp"] = hero.get("xp", 0) + devil["reward"]["xp"]
                hero["gold"] = hero.get("gold", 0) + devil["reward"]["gold"]
                hero["inventory"].append(devil["reward"]["item"])
                print(f"You earn {devil['reward']['xp']} XP, {devil['reward']['gold']} gold, and found a {devil['reward']['item']['name']}!")
                break


            random_enemy_reduce = random.randint(0, devil["damage"])
            enemy_damage = devil["damage"] - random_enemy_reduce
            if enemy_damage == 0:
                print("The enemy missed you completely!")
            elif random_enemy_reduce == 0:
                print("A perfect hit from the enemy!")
            hero["hp"] -= enemy_damage
            if hero["hp"] < 0:
                hero["hp"] = 0
            print(f"Your HP: {hero['hp']}")

        elif action == "defend":
            reduced_damage = devil["damage"] // 2
            hero["hp"] -= reduced_damage
            if hero["hp"] < 0:
                hero["hp"] = 0
            print(f"You block bravely! The {devil['name']} only deals {reduced_damage} damage. Your HP: {hero['hp']}")

        elif action == "hide":
            print("You fled the battle like a coward...")
            break

        else:
            print("Please choose 'attack', 'defend', or 'hide'.")



    if hero["hp"] == 0:
        print("\nYou have fallen in battle. the kingdom is destroyed.")
        print("\nWhat's left in the chest:")
        for item in chest:
            print(f"- {item['name']}")
        break

    potion = None
    for item in hero["inventory"]:
        if item["name"].lower() == "health potion":
            potion = item
            break 

    if potion:
        use_potion = input("Do you want to drink your health potion? (y/n): ").strip().lower()
        if use_potion == "y":
            hero["hp"] = min(hero["hp"] + potion["heal"], 100)
            print(f"You drink the potion and restore your health! HP: {hero['hp']}")
            hero["inventory"].remove(potion)
        else:
            print("You decided not to use the potion.")
    else:
            print("You don't have a health potion in your inventory.")

    print("\nHero inventory now contains:")
    for item in hero["inventory"]:
        print(f"- {item['name']}")


if chest:
    sorted_chest = sorted(chest, key=lambda x: x["name"])
    print(f"\nYou notice something shiny left in the chest for the next adventure: {sorted_chest[0]['name'].title()}...")

# lambdam cota damabnia da sheveshvi :D sorted cota gaugebaria.


print("\n=== FINAL HERO STATS ===")
for key, value in hero.items():
    if key != "inventory":
        print(f"{key}: {value}")

print("\nInventory:")
for item in hero["inventory"]:
    print(f"- {item['name']}")
