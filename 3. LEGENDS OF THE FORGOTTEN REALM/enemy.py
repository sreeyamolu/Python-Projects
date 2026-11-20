
class Enemy:

    def __init__(self, name, level, hp, attack, defense, exp_reward, gold_reward, is_boss=False):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.is_boss = is_boss

    def show_details(self):
        print("\n===== ENEMY DETAILS =====")
        print("Name:", self.name)
        print("Level:", self.level)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Boss:", "Yes" if self.is_boss else "No")


# Normal Enemies
ENEMIES = [
    {"name": "Goblin", "level": 1, "hp": 100, "attack": 20, "defense": 5, "exp_reward": 50, "gold_reward": 30},
    {"name": "Wolf", "level": 2, "hp": 120, "attack": 25, "defense": 8, "exp_reward": 60, "gold_reward": 35},
    {"name": "Skeleton", "level": 3, "hp": 140, "attack": 30, "defense": 10, "exp_reward": 70, "gold_reward": 40},
    {"name": "Orc", "level": 4, "hp": 160, "attack": 35, "defense": 12, "exp_reward": 80, "gold_reward": 45},
    {"name": "Bandit", "level": 5, "hp": 180, "attack": 40, "defense": 15, "exp_reward": 90, "gold_reward": 50},
    {"name": "Giant Spider", "level": 6, "hp": 200, "attack": 45, "defense": 18, "exp_reward": 100, "gold_reward": 55},
    {"name": "Zombie", "level": 7, "hp": 220, "attack": 50, "defense": 20, "exp_reward": 110, "gold_reward": 60},
    {"name": "Dark Knight", "level": 8, "hp": 240, "attack": 55, "defense": 22, "exp_reward": 120, "gold_reward": 65},
    {"name": "Troll", "level": 9, "hp": 260, "attack": 60, "defense": 25, "exp_reward": 130, "gold_reward": 70},
    {"name": "Fire Demon", "level": 10, "hp": 300, "attack": 65, "defense": 28, "exp_reward": 200, "gold_reward": 100},
    {"name": "Ice Golem", "level": 11, "hp": 320, "attack": 70, "defense": 30, "exp_reward": 150, "gold_reward": 75},
    {"name": "Shadow Assassin", "level": 12, "hp": 340, "attack": 75, "defense": 32, "exp_reward": 160, "gold_reward": 80},
    {"name": "Vampire", "level": 13, "hp": 360, "attack": 80, "defense": 35, "exp_reward": 170, "gold_reward": 85},
    {"name": "Werewolf", "level": 14, "hp": 380, "attack": 85, "defense": 38, "exp_reward": 180, "gold_reward": 90},
    {"name": "Stone Guardian", "level": 15, "hp": 400, "attack": 90, "defense": 40, "exp_reward": 190, "gold_reward": 95},
    {"name": "Poison Beast", "level": 16, "hp": 420, "attack": 95, "defense": 42, "exp_reward": 200, "gold_reward": 100},
    {"name": "Dark Mage", "level": 17, "hp": 440, "attack": 100, "defense": 45, "exp_reward": 210, "gold_reward": 105},
    {"name": "Hellhound", "level": 18, "hp": 460, "attack": 105, "defense": 48, "exp_reward": 220, "gold_reward": 110},
    {"name": "Dragon Hatchling", "level": 19, "hp": 480, "attack": 110, "defense": 50, "exp_reward": 230, "gold_reward": 115},
    {"name": "Cursed Warrior", "level": 20, "hp": 500, "attack": 115, "defense": 52, "exp_reward": 240, "gold_reward": 120},
    {"name": "Thunder Beast", "level": 21, "hp": 520, "attack": 120, "defense": 55, "exp_reward": 250, "gold_reward": 125},
    {"name": "Lich", "level": 22, "hp": 540, "attack": 125, "defense": 58, "exp_reward": 260, "gold_reward": 130},
    {"name": "Demon Lord", "level": 23, "hp": 600, "attack": 135, "defense": 60, "exp_reward": 300, "gold_reward": 150},
    {"name": "Ancient Dragon", "level": 24, "hp": 700, "attack": 150, "defense": 65, "exp_reward": 350, "gold_reward": 175},
    {"name": "Shadow King", "level": 25, "hp": 800, "attack": 170, "defense": 70, "exp_reward": 500, "gold_reward": 250}
]


# Boss Enemies - One Boss for Every 10 Levels

BOSS_ENEMIES = [
    {"name": "Goblin King", "level": 10, "hp": 300, "attack": 25, "defense": 10, "exp_reward": 500, "gold_reward": 500, "is_boss": True},

    {"name": "Forest Guardian", "level": 20, "hp": 500, "attack": 35, "defense": 10, "exp_reward": 1000, "gold_reward": 1000, "is_boss": True},

    {"name": "Ancient Golem", "level": 30, "hp": 400, "attack": 30, "defense": 10, "exp_reward": 1500, "gold_reward": 1500, "is_boss": True},

    {"name": "Vampire Lord", "level": 40, "hp": 500, "attack": 35, "defense": 12, "exp_reward": 2000, "gold_reward": 2000, "is_boss": True},

    {"name": "Dragon Rider", "level": 50, "hp": 600, "attack": 40, "defense": 15, "exp_reward": 2500, "gold_reward": 2500, "is_boss": True},

    {"name": "Demon General", "level": 60, "hp": 700, "attack": 45, "defense": 18, "exp_reward": 3000, "gold_reward": 3000, "is_boss": True},

    {"name": "Ice Titan", "level": 70, "hp": 800, "attack": 50, "defense": 20, "exp_reward": 3500, "gold_reward": 3500, "is_boss": True},

    {"name": "Shadow Emperor", "level": 80, "hp": 900, "attack": 55, "defense": 22, "exp_reward": 4000, "gold_reward": 4000, "is_boss": True},

    {"name": "Celestial Dragon", "level": 90, "hp": 1000, "attack": 60, "defense": 25, "exp_reward": 4500, "gold_reward": 4500, "is_boss": True},

    {"name": "Ancient Demon King", "level": 100, "hp": 1200, "attack": 70, "defense": 30, "exp_reward": 10000, "gold_reward": 10000, "is_boss": True}
]



def create_enemy(enemy_data):
    return Enemy(
        name=enemy_data["name"],
        level=enemy_data["level"],
        hp=enemy_data["hp"],
        attack=enemy_data["attack"],
        defense=enemy_data["defense"],
        exp_reward=enemy_data["exp_reward"],
        gold_reward=enemy_data["gold_reward"],
        is_boss=enemy_data.get("is_boss", False)
    )
