
import random
from player import Player
from enemy import ENEMIES, BOSS_ENEMIES, create_enemy
from battle import start_battle
from shop import show_shop
from save_load import save_game, load_game
from potions import show_potions, POTIONS
from weapons import WEAPONS, ARMORS
from world_map import choose_location


# TESTING MODE
# True = Skip boss level restrictions for testing.
# False = Normal game progression.
TESTING_MODE = False


# Region and Boss connection
REGION_BOSSES = {
    "Village": ("Goblin King", 10),
    "Forest": ("Forest Guardian", 20),
    "Cave": ("Ancient Golem", 30),
    "Desert": ("Vampire Lord", 40),
    "Ruins": ("Dragon Rider", 50),
    "Castle": ("Demon General", 60),
    "Volcano": ("Ice Titan", 70),
    "Frozen Mountain": ("Shadow Emperor", 80),
    "Sky Temple": ("Celestial Dragon", 90),
    "Demon Realm": ("Ancient Demon King", 100)
}


def create_character():

    print("\n===== CHARACTER CREATION =====")

    name = input("Enter your character name: ").strip()

    while not name:
        print("Name cannot be empty!")
        name = input("Enter your character name: ").strip()

    print("\nChoose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    classes = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Archer",
        "4": "Assassin"
    }

    choice = input("Choose your class: ").strip()

    while choice not in classes:
        print("Invalid choice! Try again.")
        choice = input("Choose your class: ").strip()

    player_class = classes[choice]

    player = Player(name, player_class)

    print("\nCharacter created successfully!")
    player.show_stats()

    return player


def game_menu(player):

    selected_location = None

    while player.hp > 0:

        print("\n===== GAME MENU =====")
        print("1. Start Battle")
        print("2. Visit Shop")
        print("3. View Potions")
        print("4. View Inventory")
        print("5. View Player Stats")
        print("6. World Map")
        print("7. Save Game")
        print("8. Exit Game")

        if TESTING_MODE:
            print("TESTING MODE: Boss level restrictions disabled!")

        if selected_location:
            print("Selected Location:", selected_location["name"])

        choice = input("Choose an option: ").strip()

        # START BATTLE
        if choice == "1":

            if selected_location is None:
                print("\nPlease select a location from World Map first!")
                continue

            location_name = selected_location["name"]
            boss_info = REGION_BOSSES.get(location_name)

            if boss_info:

                boss_name, boss_level = boss_info

                can_fight_boss = (
                    TESTING_MODE or player.level >= boss_level
                )

                if (
                    can_fight_boss
                    and boss_name not in player.bosses_defeated
                ):

                    boss_enemies = [
                        enemy for enemy in BOSS_ENEMIES
                        if enemy["name"] == boss_name
                    ]

                    if boss_enemies:

                        enemy_data = boss_enemies[0]

                        print("\n===== BOSS BATTLE =====")
                        print("You are facing:", boss_name)

                        if TESTING_MODE and player.level < boss_level:
                            print("TESTING MODE: Level restriction bypassed!")

                    else:

                        print("Boss data not found!")
                        continue

                else:

                    # NORMAL ENEMY BATTLE
                    available_enemies = [
                        enemy for enemy in ENEMIES
                        if enemy["name"] in selected_location["enemies"]
                        and not enemy.get("is_boss", False)
                    ]

                    if not available_enemies:
                        print("No enemies available in this location!")
                        continue

                    enemy_data = random.choice(available_enemies)

                    if not TESTING_MODE and player.level < boss_level:
                        print("\nYou need to reach Level", boss_level)
                        print("to challenge this region's boss.")

            else:

                print("No boss information found for this location!")
                continue

            enemy = create_enemy(enemy_data)

            if enemy.is_boss:
                print("\nBoss Name:", enemy.name)
                print("Boss Level:", enemy.level)
                print("Boss HP:", enemy.hp)

            # START BATTLE
            start_battle(player, enemy)

            # AUTOMATICALLY SAVE AFTER BATTLE
            save_game(player)

            if player.hp <= 0:
                break

        # VISIT SHOP
        elif choice == "2":

            show_shop(player)

        # VIEW POTIONS
        elif choice == "3":

            show_potions(player)

        # VIEW INVENTORY
        elif choice == "4":

            print("\n===== YOUR INVENTORY =====")

            potion_names = [
                potion["name"] for potion in POTIONS
            ]

            print("\n--- Weapons & Armor ---")

            weapons_armor = [
                item for item in player.inventory
                if item not in potion_names
            ]

            if weapons_armor:
                for item in weapons_armor:
                    print("-", item)
            else:
                print("No weapons or armor!")

            print("\n--- Potions ---")

            inventory_potions = [
                item for item in player.inventory
                if item in potion_names
            ]

            if inventory_potions:
                for item in inventory_potions:
                    print("-", item)
            else:
                print("No purchased potions!")

            print("\nHealth Potions:", player.potions)
            print("Mana Potions:", player.mana_potions)

            print("\n--- Equipped Items ---")
            print("Equipped Weapon:", player.equipped_weapon)
            print("Equipped Armor:", player.equipped_armor)

            # EQUIP WEAPON
            available_weapons = [
                weapon for weapon in WEAPONS
                if weapon["name"] in player.inventory
            ]

            if available_weapons:

                print("\n--- EQUIP WEAPON ---")

                for i, weapon in enumerate(available_weapons, start=1):
                    print(
                        i, ".", weapon["name"],
                        "- Damage:", weapon["damage"]
                    )

                print("0. Back")

                try:

                    weapon_choice = int(
                        input("Choose a weapon to equip: ")
                    )

                    if weapon_choice == 0:
                        pass

                    elif 1 <= weapon_choice <= len(available_weapons):

                        selected_weapon = available_weapons[
                            weapon_choice - 1
                        ]

                        player.equipped_weapon = selected_weapon["name"]

                        print("\nWeapon equipped successfully!")
                        print("Equipped Weapon:", player.equipped_weapon)

                        save_game(player)

                    else:
                        print("Invalid weapon choice!")

                except ValueError:
                    print("Please enter a valid number!")

            else:
                print("\nNo weapons available to equip!")
                
                
                
            # EQUIP ARMOR
            available_armors = [
                armor for armor in ARMORS
                if armor["name"] in player.inventory
            ]

            if available_armors:

                print("\n--- EQUIP ARMOR ---")

                for i, armor in enumerate(available_armors, start=1):
                    print(
                        i, ".", armor["name"],
                        "- Defense:", armor["defense"]
                    )

                print("0. Back")

                try:
                    armor_choice = int(
                        input("Choose an armor to equip: ")
                    )

                    if armor_choice == 0:
                        pass

                    elif 1 <= armor_choice <= len(available_armors):

                        selected_armor = available_armors[
                            armor_choice - 1
                        ]

                        player.equipped_armor = selected_armor["name"]

                        print("\nArmor equipped successfully!")
                        print("Equipped Armor:", player.equipped_armor)

                        save_game(player)

                    else:
                        print("Invalid armor choice!")

                except ValueError:
                    print("Please enter a valid number!")

            else:
                print("\nNo armor available to equip!")
            
                

        # VIEW PLAYER STATS
        elif choice == "5":

            player.show_stats()

        # WORLD MAP
        elif choice == "6":

            location = choose_location(player)

            if location is not None:
                selected_location = location

        # SAVE GAME
        elif choice == "7":

            save_game(player)

        # EXIT GAME
        elif choice == "8":

            save_game(player)
            print("Exiting Game...")
            break

        else:

            print("Invalid choice!")


def main():

    while True:

        print("\n===== LEGENDS OF THE FORGOTTEN REALM =====")
        print("1. New Game")
        print("2. Continue Game")
        print("3. Instructions")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        # NEW GAME
        if choice == "1":

            player = create_character()
            game_menu(player)

        # CONTINUE GAME
        elif choice == "2":

            data = load_game()

            if data is not None:

                player = Player(
                    data["name"],
                    data["player_class"]
                )

                player.level = data["level"]
                player.exp = data["exp"]
                player.hp = data["hp"]
                player.max_hp = data["max_hp"]
                player.mana = data["mana"]
                player.max_mana = data["max_mana"]
                player.attack = data["attack"]
                player.defense = data["defense"]
                player.gold = data["gold"]
                player.potions = data["potions"]
                player.mana_potions = data.get("mana_potions", 2)
                player.inventory = data.get("inventory", [])
                player.loot_items = data.get("loot_items", [])
                player.equipped_weapon = data.get("equipped_weapon")
                player.equipped_armor = data.get("equipped_armor")

                # RESTORE BOSS AND ENEMY TRACKING
                player.bosses_defeated = data.get(
                    "bosses_defeated", []
                )
                player.enemies_defeated = data.get(
                    "enemies_defeated", 0
                )

                print("\nGame loaded successfully!")
                game_menu(player)

            else:

                print("No saved game found!")

        # INSTRUCTIONS
        elif choice == "3":

            print("\n===== GAME INSTRUCTIONS =====")
            print("1. Create a character and choose your class.")
            print("2. Fight enemies to earn EXP and Gold.")
            print("3. Level up to unlock new locations.")
            print("4. Defeat region bosses to unlock the next region.")
            print("5. Buy weapons, armor and potions from the shop.")
            print("6. Use skills and potions during battles.")
            print("7. Defend yourself to reduce enemy damage.")
            print("8. Explore different locations using the World Map.")
            print("9. Defeat the Ancient Demon King to complete the game.")
            print("10. Save your game before exiting.")
            print("11. Use Continue Game to load your saved progress.")
            print("\nBecome the strongest hero in the realm!")

        # EXIT
        elif choice == "4":

            print("Thank you for playing!")
            break

        else:

            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
