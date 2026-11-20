
import json
import os

SAVE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "savegame.json"
)


def save_game(player):

    data = {
        "name": player.name,
        "player_class": player.player_class,
        "level": player.level,
        "exp": player.exp,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "mana": player.mana,
        "max_mana": player.max_mana,
        "attack": player.attack,
        "defense": player.defense,
        "gold": player.gold,
        "potions": player.potions,
        "mana_potions": player.mana_potions,
        "inventory": player.inventory,
        "loot_items": player.loot_items,
        "equipped_weapon": player.equipped_weapon,
        "equipped_armor": player.equipped_armor,
        "bosses_defeated": player.bosses_defeated,
        "enemies_defeated": player.enemies_defeated
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Game saved successfully!")


def load_game():

    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)

        print("Saved game loaded successfully!")
        return data

    except FileNotFoundError:
        print("No saved game found!")
        return None

    except json.JSONDecodeError:
        print("Save file is corrupted!")
        return None
