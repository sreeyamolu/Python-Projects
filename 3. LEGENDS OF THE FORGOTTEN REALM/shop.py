
from weapons import WEAPONS, ARMORS
from potions import POTIONS


def show_shop(player):

    while True:
        print("\n===== GAME SHOP =====")
        print("Your Gold:", player.gold)

        print("1. Buy Weapons")
        print("2. Buy Armor")
        print("3. Buy Potions")
        print("4. Equip Armor")
        print("5. Exit Shop")

        choice = input("Choose an option: ").strip()

        # BUY WEAPONS
        if choice == "1":

            print("\n===== WEAPONS =====")

            for i, weapon in enumerate(WEAPONS, start=1):
                print(i, weapon["name"], "- Damage:", weapon["damage"])

            print("0. Back")

            try:
                item = int(input("Choose weapon: "))

                if item == 0:
                    continue

                if item < 1 or item > len(WEAPONS):
                    print("Invalid choice!")
                    continue

                weapon = WEAPONS[item - 1]
                price = weapon["damage"] * 10

                if player.gold >= price:

                    player.gold -= price

                    if weapon["name"] not in player.inventory:
                        player.inventory.append(weapon["name"])

                    player.equipped_weapon = weapon["name"]

                    print("\nWeapon purchased and equipped successfully!")
                    print("Equipped Weapon:", weapon["name"])
                    print("Weapon Damage:", weapon["damage"])
                    print("Base Attack:", player.attack)
                    print("Gold remaining:", player.gold)

                else:
                    print("Not enough Gold!")

            except ValueError:
                print("Invalid choice!")

        # BUY ARMOR
        elif choice == "2":

            print("\n===== ARMORS =====")

            for i, armor in enumerate(ARMORS, start=1):
                print(i, armor["name"], "- Defense:", armor["defense"])

            print("0. Back")

            try:
                item = int(input("Choose armor: "))

                if item == 0:
                    continue

                if item < 1 or item > len(ARMORS):
                    print("Invalid choice!")
                    continue

                armor = ARMORS[item - 1]
                price = armor["defense"] * 10

                if player.gold >= price:

                    player.gold -= price

                    if armor["name"] not in player.inventory:
                        player.inventory.append(armor["name"])

                    player.equipped_armor = armor["name"]

                    print("\nArmor purchased and equipped successfully!")
                    print("Equipped Armor:", armor["name"])
                    print("Armor Defense:", armor["defense"])
                    print("Base Defense:", player.defense)
                    print("Gold remaining:", player.gold)

                else:
                    print("Not enough Gold!")

            except ValueError:
                print("Invalid choice!")

        # BUY POTIONS
        elif choice == "3":

            print("\n===== POTIONS =====")

            for i, potion in enumerate(POTIONS, start=1):
                price = potion["value"] * 2

                print(
                    i,
                    potion["name"],
                    "- Value:", potion["value"],
                    "- Price:", price
                )

            print("0. Back")

            try:
                item = int(input("Choose potion: "))

                if item == 0:
                    continue

                if item < 1 or item > len(POTIONS):
                    print("Invalid choice!")
                    continue

                potion = POTIONS[item - 1]
                price = potion["value"] * 2

                if player.gold >= price:

                    player.gold -= price

                    if potion["type"] == "Health":
                        player.potions += 1

                    elif potion["type"] == "Mana":
                        player.mana_potions += 1

                    # Store every potion purchase separately
                    player.inventory.append(potion["name"])

                    print("\nPotion purchased successfully!")
                    print("Potion:", potion["name"])
                    print("Gold remaining:", player.gold)

                else:
                    print("Not enough Gold!")

            except ValueError:
                print("Invalid choice!")

        # EQUIP ARMOR
        elif choice == "4":

            print("\n===== EQUIP ARMOR =====")

            available_armors = [
                armor for armor in ARMORS
                if armor["name"] in player.inventory
            ]

            if not available_armors:

                print("No armor available in inventory!")

            else:

                for i, armor in enumerate(available_armors, start=1):
                    print(
                        i,
                        armor["name"],
                        "- Defense:", armor["defense"]
                    )

                print("0. Back")

                try:
                    item = int(input("Choose armor: "))

                    if item == 0:
                        continue

                    if item < 1 or item > len(available_armors):
                        print("Invalid choice!")
                        continue

                    armor = available_armors[item - 1]

                    player.equipped_armor = armor["name"]

                    print("\nArmor equipped successfully!")
                    print("Equipped Armor:", armor["name"])
                    print("Armor Defense:", armor["defense"])
                    print("Base Defense:", player.defense)

                except ValueError:
                    print("Invalid choice!")

        # EXIT SHOP
        elif choice == "5":

            print("Leaving Shop...")
            break

        else:
            print("Invalid choice!")
