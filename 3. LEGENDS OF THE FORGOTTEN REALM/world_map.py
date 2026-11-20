
WORLD_MAP = [
    {
        "name": "Village",
        "level": 1,
        "required_boss": None,
        "description": "A peaceful village where every hero begins their journey.",
        "enemies": ["Goblin", "Wolf"]
    },
    {
        "name": "Forest",
        "level": 5,
        "required_boss": "Goblin King",
        "description": "A dark forest filled with dangerous creatures.",
        "enemies": ["Goblin", "Wolf", "Skeleton", "Orc", "Bandit"]
    },
    {
        "name": "Cave",
        "level": 10,
        "required_boss": "Forest Guardian",
        "description": "A mysterious cave guarded by powerful creatures.",
        "enemies": ["Giant Spider", "Zombie", "Dark Knight", "Troll", "Ice Golem"]
    },
    {
        "name": "Desert",
        "level": 20,
        "required_boss": "Ancient Golem",
        "description": "A dangerous desert filled with fire and poison creatures.",
        "enemies": ["Fire Demon", "Poison Beast"]
    },
    {
        "name": "Ruins",
        "level": 30,
        "required_boss": "Vampire Lord",
        "description": "Ancient ruins filled with cursed enemies.",
        "enemies": ["Shadow Assassin", "Skeleton", "Stone Guardian"]
    },
    {
        "name": "Castle",
        "level": 40,
        "required_boss": "Dragon Rider",
        "description": "An ancient castle controlled by dark forces.",
        "enemies": ["Vampire", "Werewolf", "Dark Mage", "Hellhound"]
    },
    {
        "name": "Volcano",
        "level": 50,
        "required_boss": "Demon General",
        "description": "A burning land filled with deadly monsters.",
        "enemies": ["Fire Demon", "Demon Lord", "Thunder Beast"]
    },
    {
        "name": "Frozen Mountain",
        "level": 60,
        "required_boss": "Ice Titan",
        "description": "A frozen region guarded by powerful enemies.",
        "enemies": ["Ice Golem", "Troll", "Dark Knight"]
    },
    {
        "name": "Sky Temple",
        "level": 70,
        "required_boss": "Shadow Emperor",
        "description": "A sacred temple protected by ancient creatures.",
        "enemies": ["Ancient Dragon", "Lich", "Dragon Hatchling"]
    },
    {
        "name": "Demon Realm",
        "level": 80,
        "required_boss": "Celestial Dragon",
        "description": "The final realm filled with terrifying enemies.",
        "enemies": ["Demon Lord", "Shadow King", "Ancient Dragon"]
    }
]


# TESTING MODE
# Set this to False for normal game progression.
TESTING_MODE = False


def is_location_unlocked(player, location):

    if TESTING_MODE:
        return True

    required_level = location["level"]
    required_boss = location["required_boss"]

    level_unlocked = player.level >= required_level

    if required_boss is None:
        boss_unlocked = True
    else:
        boss_unlocked = required_boss in player.bosses_defeated

    return level_unlocked and boss_unlocked


def show_world_map(player):

    print("\n===== WORLD MAP =====")

    if TESTING_MODE:
        print("TESTING MODE: All locations are unlocked!")

    for i, location in enumerate(WORLD_MAP, start=1):

        if is_location_unlocked(player, location):
            status = "UNLOCKED"
        else:
            status = "LOCKED"

        print(
            i, ".", location["name"],
            "- Required Level:", location["level"],
            "-", status
        )

    print("0. Back")


def choose_location(player):

    show_world_map(player)

    try:
        choice = int(input("\nChoose a location (0 to go back): "))

        if choice == 0:
            return None

        if choice < 1 or choice > len(WORLD_MAP):
            print("Invalid location choice!")
            return None

        location = WORLD_MAP[choice - 1]

        if not is_location_unlocked(player, location):
            print("\nThis location is locked!")
            print("Required Level:", location["level"])

            if location["required_boss"] is not None:
                print("Boss to defeat:", location["required_boss"])

            return None

        print("\n===== LOCATION SELECTED =====")
        print("Location:", location["name"])
        print(location["description"])

        print("\nAvailable Enemies:")
        for enemy in location["enemies"]:
            print("-", enemy)

        return location

    except ValueError:
        print("Please enter a valid number!")
        return None
