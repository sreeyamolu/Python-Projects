
POTIONS = [
    {"name": "Small Health Potion", "type": "Health", "value": 30},
    {"name": "Medium Health Potion", "type": "Health", "value": 50},
    {"name": "Large Health Potion", "type": "Health", "value": 100},
    {"name": "Greater Health Potion", "type": "Health", "value": 150},
    {"name": "Small Mana Potion", "type": "Mana", "value": 30},
    {"name": "Medium Mana Potion", "type": "Mana", "value": 50},
    {"name": "Large Mana Potion", "type": "Mana", "value": 100},
    {"name": "Greater Mana Potion", "type": "Mana", "value": 150},
    {"name": "Strength Potion", "type": "Strength", "value": 10},
    {"name": "Defense Potion", "type": "Defense", "value": 10},
    {"name": "Critical Potion", "type": "Critical", "value": 10},
    {"name": "Speed Potion", "type": "Speed", "value": 10},
    {"name": "Fire Resistance Potion", "type": "Resistance", "value": 20},
    {"name": "Ice Resistance Potion", "type": "Resistance", "value": 20},
    {"name": "Full Recovery Potion", "type": "Recovery", "value": 100}
]


def show_potions(player):

    print("\n===== POTION INVENTORY =====")

    found = False

    # Count purchased potions from inventory
    for potion in POTIONS:

        quantity = player.inventory.count(potion["name"])

        # Add starting Health potions
        if potion["name"] == "Small Health Potion":
            purchased_health = sum(
                player.inventory.count(p["name"])
                for p in POTIONS
                if p["type"] == "Health"
            )

            quantity += max(0, player.potions - purchased_health)

        # Add starting Mana potions
        elif potion["name"] == "Small Mana Potion":
            purchased_mana = sum(
                player.inventory.count(p["name"])
                for p in POTIONS
                if p["type"] == "Mana"
            )

            quantity += max(0, player.mana_potions - purchased_mana)

        if quantity > 0:

            found = True

            print(
                potion["name"],
                "-",
                potion["type"],
                "- Value:",
                potion["value"],
                "- Quantity:",
                quantity
            )

    if not found:
        print("No potions available in your inventory!")
