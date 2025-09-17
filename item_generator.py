import random
from .item_loader import load_all_data
from .item import Item

data = load_all_data()


def generate_item(level=1):
    prefix = random.choice(data["prefixes"])
    affix = random.choice(data["affixes"])
    base = random.choice(data["base_items"])
    rarity = random.choices(
        population=data["rarities"],
        weights=[r["chance"] for r in data["rarities"]],
        k=1
    )[0]

    name = f"{prefix['name']} {base['name']} of {affix['name']}"
    slot = base["slot"]

    # Merge stats from all sources and apply rarity multiplier
    combined_stats = {}
    for source in [prefix["modifiers"], base["base_stats"], affix["modifiers"]]:
        for k, v in source.items():
            combined_stats[k] = combined_stats.get(k, 0) + v

    # Apply rarity multiplier & level scaling
    for stat in combined_stats:
        scaled = combined_stats[stat] * rarity["stat_multiplier"]
        scaled *= (1 + (level - 1) * 0.05)
        combined_stats[stat] = round(scaled)

    return Item(name=name, slot=slot, base_stats=combined_stats, rarity=rarity["name"], color=rarity["color"])
