
class Player:

    def __init__(self, name, player_class):

        self.name = name
        self.player_class = player_class

        self.level = 1
        self.exp = 0
        self.gold = 100

        self.potions = 3
        self.mana_potions = 2
        self.inventory = []
        self.loot_items = []
        self.equipped_weapon = None
        self.equipped_armor = None

        # Enemy and Boss Tracking
        self.bosses_defeated = []
        self.enemies_defeated = 0

        if player_class == "Warrior":
            self.max_hp = 200
            self.max_mana = 50
            self.attack = 30
            self.defense = 25
            self.critical_chance = 5

        elif player_class == "Mage":
            self.max_hp = 120
            self.max_mana = 200
            self.attack = 40
            self.defense = 10
            self.critical_chance = 10

        elif player_class == "Archer":
            self.max_hp = 150
            self.max_mana = 100
            self.attack = 25
            self.defense = 15
            self.critical_chance = 20

        elif player_class == "Assassin":
            self.max_hp = 100
            self.max_mana = 100
            self.attack = 45
            self.defense = 10
            self.critical_chance = 30

        self.hp = self.max_hp
        self.mana = self.max_mana
        self.critical_damage = 2

        # Potion Effects
        self.strength_bonus = 0
        self.defense_bonus = 0
        self.critical_bonus = 0

        self.speed_active = False
        self.fire_resistance = 0
        self.ice_resistance = 0

        self.buff_turns = 0
        self.resistance_turns = 0

        # Class Skills
        if player_class == "Warrior":
            self.skill_name = "Power Strike"
            self.skill_damage = 60

        elif player_class == "Mage":
            self.skill_name = "Fireball"
            self.skill_damage = 70

        elif player_class == "Archer":
            self.skill_name = "Arrow Rain"
            self.skill_damage = 50

        elif player_class == "Assassin":
            self.skill_name = "Shadow Attack"
            self.skill_damage = 80

    def gain_exp(self, amount):

        if self.level >= 100:
            print("Maximum Level Reached!")
            return

        self.exp += amount

        print("\nEXP Gained:", amount)
        print("Total EXP:", self.exp)

        self.level_up()

    
    def level_up(self):

        boss_levels = {
            10: "Goblin King",
            20: "Forest Guardian",
            30: "Ancient Golem",
            40: "Vampire Lord",
            50: "Dragon Rider",
            60: "Demon General",
            70: "Ice Titan",
            80: "Shadow Emperor",
            90: "Celestial Dragon",
            100: "Ancient Demon King"
        }

        while self.level < 100:

            required_exp = self.level * 100

            if self.exp < required_exp:
                break

            next_level = self.level + 1

            # Check whether the next level is blocked by a boss
            if self.level in boss_levels:
                required_boss = boss_levels[self.level]

                if required_boss not in self.bosses_defeated:
                    print("\n===== LEVEL CAP REACHED =====")
                    print("You must defeat", required_boss)
                    print("before progressing to the next level.")
                    break

            self.exp -= required_exp
            self.level = next_level

            self.max_hp += 20
            self.max_mana += 10
            self.attack += 5
            self.defense += 3

            self.hp = self.max_hp
            self.mana = self.max_mana

            print("\n===== LEVEL UP! =====")
            print("Congratulations!")
            print("Your Level:", self.level)
            print("Your HP and Mana increased!")
            print("Your Attack and Defense increased!")

        if self.level >= 100:
            print("\nMaximum Level Reached!")


    def add_loot(self, item):
        self.loot_items.append(item)
        print("\nLoot collected:", item)

    def show_stats(self):

        print("\n===== PLAYER STATS =====")
        print("Name:", self.name)
        print("Class:", self.player_class)
        print("Level:", self.level)
        print("EXP:", self.exp)
        print("HP:", self.hp, "/", self.max_hp)
        print("Mana:", self.mana, "/", self.max_mana)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Critical Chance:", self.critical_chance, "%")
        print("Gold:", self.gold)
        print("Enemies Defeated:", self.enemies_defeated)
        print("Bosses Defeated:", len(self.bosses_defeated))
