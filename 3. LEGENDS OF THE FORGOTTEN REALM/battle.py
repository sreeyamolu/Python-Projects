
import random
from weapons import WEAPONS, ARMORS
from potions import POTIONS


def start_battle(player, enemy):

    print("\n===== BATTLE START =====")
    print("An enemy appeared:", enemy.name)
    print("Enemy HP:", enemy.hp)

    turn_count = 0

    while player.hp > 0 and enemy.hp > 0:

        print("\n===== YOUR TURN =====")
        print("1. Attack")
        print("2. Skills")
        print("3. Heal")
        print("4. Use Potion")
        print("5. Defend")
        print("6. Inventory")
        print("7. View Stats")
        print("8. Run")

        choice = input("Choose your action: ").strip()

        defending = False
        action_completed = True

        # ATTACK
        if choice == "1":

            weapon_damage = 0

            if player.equipped_weapon:
                for weapon in WEAPONS:
                    if weapon["name"] == player.equipped_weapon:
                        weapon_damage = weapon["damage"]
                        break

            damage = max(
                1,
                player.attack + weapon_damage - enemy.defense
            )

            if random.randint(1, 100) <= player.critical_chance:
                damage *= player.critical_damage
                print("\n===== CRITICAL HIT! =====")

            enemy.hp = max(0, enemy.hp - damage)

            print("\nYou attacked", enemy.name)
            print("Damage:", damage)
            print("Enemy HP:", enemy.hp)

        # SKILLS
        elif choice == "2":

            skill_cost = 20

            if player.mana >= skill_cost:

                player.mana -= skill_cost

                damage = max(
                    1,
                    player.skill_damage - enemy.defense
                )

                enemy.hp = max(0, enemy.hp - damage)

                print("\nYou used", player.skill_name)
                print("Skill Damage:", damage)
                print("Mana remaining:", player.mana)
                print("Enemy HP:", enemy.hp)

            else:
                print("Not enough Mana!")
                action_completed = False

        # HEAL
        elif choice == "3":

            if player.hp >= player.max_hp:
                print("Your HP is already full!")
                action_completed = False

            else:

                old_hp = player.hp
                player.hp = min(player.hp + 30, player.max_hp)

                print("\nYou healed yourself!")
                print("HP restored:", player.hp - old_hp)
                print("Your HP:", player.hp)

        # USE POTIONS
        elif choice == "4":

            print("\n===== USE POTION =====")

            available_potions = []

            # Count Health and Mana potions in inventory
            owned_health = [
                item for item in player.inventory
                if any(
                    p["name"] == item and p["type"] == "Health"
                    for p in POTIONS
                )
            ]

            owned_mana = [
                item for item in player.inventory
                if any(
                    p["name"] == item and p["type"] == "Mana"
                    for p in POTIONS
                )
            ]

            # Add every purchased Health potion separately
            for item in owned_health:
                for potion in POTIONS:
                    if potion["name"] == item:
                        available_potions.append(potion)
                        break

            # Add every purchased Mana potion separately
            for item in owned_mana:
                for potion in POTIONS:
                    if potion["name"] == item:
                        available_potions.append(potion)
                        break

            # Add starting Small Health potions
            starting_health = max(
                0,
                player.potions - len(owned_health)
            )

            small_health = next(
                p for p in POTIONS
                if p["name"] == "Small Health Potion"
            )

            for _ in range(starting_health):
                available_potions.append(small_health)

            # Add starting Small Mana potions
            starting_mana = max(
                0,
                player.mana_potions - len(owned_mana)
            )

            small_mana = next(
                p for p in POTIONS
                if p["name"] == "Small Mana Potion"
            )

            for _ in range(starting_mana):
                available_potions.append(small_mana)

            # Add other purchased potions
            for item in player.inventory:

                for potion in POTIONS:

                    if (
                        potion["name"] == item
                        and potion["type"] not in ("Health", "Mana")
                    ):
                        available_potions.append(potion)
                        break

            if not available_potions:

                print("No potions available!")
                action_completed = False

            else:

                for i, potion in enumerate(available_potions, start=1):
                    print(
                        i, ".", potion["name"],
                        "- Value:", potion["value"]
                    )

                print("0. Back")

                try:

                    potion_choice = int(input("Choose a potion: "))

                    if potion_choice == 0:
                        action_completed = False

                    elif not 1 <= potion_choice <= len(available_potions):
                        print("Invalid potion choice!")
                        action_completed = False

                    else:

                        potion = available_potions[potion_choice - 1]
                        potion_type = potion["type"]
                        value = potion["value"]
                        used = True

                        # HEALTH POTION
                        if potion_type == "Health":

                            if player.hp >= player.max_hp:
                                print("Your HP is already full!")
                                used = False

                            elif player.potions <= 0:
                                print("No Health Potions available!")
                                used = False

                            else:

                                old_hp = player.hp

                                player.hp = min(
                                    player.hp + value,
                                    player.max_hp
                                )

                                player.potions -= 1

                                print("\nHealth Potion used!")
                                print("HP restored:", player.hp - old_hp)
                                print("Health Potions remaining:", player.potions)

                                # Remove one purchased potion, if applicable
                                if potion["name"] in player.inventory:
                                    player.inventory.remove(potion["name"])

                        # MANA POTION
                        elif potion_type == "Mana":

                            if player.mana >= player.max_mana:
                                print("Your Mana is already full!")
                                used = False

                            elif player.mana_potions <= 0:
                                print("No Mana Potions available!")
                                used = False

                            else:

                                old_mana = player.mana

                                player.mana = min(
                                    player.mana + value,
                                    player.max_mana
                                )

                                player.mana_potions -= 1

                                print("\nMana Potion used!")
                                print("Mana restored:", player.mana - old_mana)
                                print("Mana Potions remaining:", player.mana_potions)

                                if potion["name"] in player.inventory:
                                    player.inventory.remove(potion["name"])

                        # STRENGTH POTION
                        elif potion_type == "Strength":

                            player.strength_bonus += value
                            player.attack += value

                            print("Strength increased by:", value)

                        # DEFENSE POTION
                        elif potion_type == "Defense":

                            player.defense_bonus += value
                            player.defense += value

                            print("Defense increased by:", value)

                        # CRITICAL POTION
                        elif potion_type == "Critical":

                            player.critical_bonus += value

                            player.critical_chance = min(
                                100,
                                player.critical_chance + value
                            )

                            print(
                                "Critical Chance increased by:",
                                value
                            )

                        # SPEED POTION
                        elif potion_type == "Speed":

                            player.speed_active = True
                            print("Speed activated!")

                        # FIRE RESISTANCE POTION
                        elif potion["name"] == "Fire Resistance Potion":

                            player.fire_resistance = value
                            print("Fire Resistance activated!")

                        # ICE RESISTANCE POTION
                        elif potion["name"] == "Ice Resistance Potion":

                            player.ice_resistance = value
                            print("Ice Resistance activated!")

                        # FULL RECOVERY POTION
                        elif potion_type == "Recovery":

                            old_hp = player.hp
                            old_mana = player.mana

                            player.hp = player.max_hp
                            player.mana = player.max_mana

                            print("\nFull Recovery!")
                            print("HP restored:", player.hp - old_hp)
                            print("Mana restored:", player.mana - old_mana)

                        else:

                            print("This potion effect is not configured!")
                            used = False

                        # Remove used special potions
                        if used and potion_type not in ("Health", "Mana"):

                            if potion["name"] in player.inventory:
                                player.inventory.remove(potion["name"])

                        if not used:
                            action_completed = False

                except ValueError:

                    print("Invalid potion choice!")
                    action_completed = False

        # DEFEND
        elif choice == "5":

            print("\nYou are defending!")
            defending = True

        # INVENTORY AND EQUIP WEAPON
        elif choice == "6":

            print("\n===== INVENTORY =====")

            if player.inventory:
                for item in player.inventory:
                    print("-", item)
            else:
                print("Your inventory is empty!")

            available_weapons = [
                weapon for weapon in WEAPONS
                if weapon["name"] in player.inventory
            ]

            if available_weapons:

                print("\n===== EQUIP WEAPON =====")

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

                        selected_weapon = available_weapons[weapon_choice - 1]

                        player.equipped_weapon = selected_weapon["name"]

                        print("\nWeapon equipped successfully!")
                        print("Equipped Weapon:", player.equipped_weapon)
                        print("Weapon Damage:", selected_weapon["damage"])

                    else:
                        print("Invalid weapon choice!")

                except ValueError:
                    print("Please enter a valid number!")

            else:
                print("\nNo weapons available to equip!")

            action_completed = False

        # VIEW STATS
        elif choice == "7":

            player.show_stats()
            action_completed = False

        # RUN
        elif choice == "8":

            print("\nYou ran away!")
            return False

        else:

            print("Invalid choice!")
            action_completed = False

        if not action_completed:
            continue

        if enemy.hp <= 0:
            break

        turn_count += 1

        # ARMOR DEFENSE
        armor_defense = 0

        if player.equipped_armor:

            for armor in ARMORS:
                if armor["name"] == player.equipped_armor:
                    armor_defense = armor["defense"]
                    break

        total_defense = player.defense + armor_defense

        # BOSS ABILITIES
        if enemy.is_boss:

            # Boss heals 2% every 8 turns
            if turn_count % 8 == 0:

                heal_amount = max(
                    1,
                    int(enemy.max_hp * 0.02)
                )

                old_enemy_hp = enemy.hp

                enemy.hp = min(
                    enemy.hp + heal_amount,
                    enemy.max_hp
                )

                print("\n===== BOSS HEALING =====")
                print(
                    enemy.name,
                    "restored",
                    enemy.hp - old_enemy_hp,
                    "HP!"
                )

                print("Boss HP:", enemy.hp)

            # Boss special attack every 3 turns
            if turn_count % 3 == 0:

                print("\n===== BOSS SPECIAL ATTACK =====")
                print(enemy.name, "uses a powerful special attack!")

                enemy_damage = max(
                    1,
                    int(max(0, enemy.attack - total_defense) * 1.5)
                )

            else:

                enemy_damage = max(
                    0,
                    enemy.attack - total_defense
                )

        else:

            enemy_damage = max(
                0,
                enemy.attack - total_defense
            )

        # DEFEND REDUCES DAMAGE
        if defending:
            enemy_damage = int(enemy_damage * 0.5)

        # SPEED DODGE
        if getattr(player, "speed_active", False):

            print("\nSpeed activated!")
            print("You dodged the enemy attack!")
            player.speed_active = False

        else:

            print("\n", enemy.name, "attacked you!")

            if enemy_damage > 0:

                player.hp = max(
                    0,
                    player.hp - enemy_damage
                )

                print("Damage received:", enemy_damage)

            else:

                print("No damage! Your defense blocked the attack.")

        print("Your HP:", player.hp)

    # PLAYER DEFEATED
    if player.hp <= 0:

        print("\n===== GAME OVER =====")
        print("You were defeated!")
        print("Your character has been defeated!")
        print("Better luck next time, hero!")

        return False

    # ENEMY DEFEATED
    if enemy.hp <= 0:

        print("\n", enemy.name, "defeated!")

        if enemy.is_boss:

            if enemy.name not in player.bosses_defeated:
                player.bosses_defeated.append(enemy.name)

            print("\n===== BOSS DEFEATED =====")
            print("Boss:", enemy.name)
            print("Total Bosses Defeated:", len(player.bosses_defeated))

        else:

            player.enemies_defeated += 1
            print("Enemies Defeated:", player.enemies_defeated)

        player.gain_exp(enemy.exp_reward)
        player.gold += enemy.gold_reward

        print("\n===== LOOT DROP =====")

        drop_type = random.choice(["weapon", "armor"])

        if drop_type == "weapon":

            loot = random.choice(WEAPONS)
            player.add_loot(loot["name"])

            if loot["name"] not in player.inventory:
                player.inventory.append(loot["name"])

            print("Weapon dropped:", loot["name"])
            print("Weapon Damage:", loot["damage"])
            print("Weapon Rarity:", loot["rarity"])

        else:

            loot = random.choice(ARMORS)
            player.add_loot(loot["name"])

            if loot["name"] not in player.inventory:
                player.inventory.append(loot["name"])

            print("Armor dropped:", loot["name"])
            print("Armor Defense:", loot["defense"])

        print("Gold gained:", enemy.gold_reward)
        print("Current Inventory:", player.inventory)

        return True

    return False
