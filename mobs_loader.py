import json
import os

class Mob:
    def __init__(self, _id, name, mob_type, level, hp, stats, loot, behavior):
        self.id = _id
        self.name = name
        self.type = mob_type
        self.level = level
        self.hp = hp
        self.stats = stats
        self.loot = loot
        self.behavior = behavior

    def __str__(self):
        return f"{self.name} (Lvl {self.level}, {self.hp} HP) - {self.behavior}"


def load_mobs(file_path="data/mobs.json"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find mobs.json at path: {file_path}")

    with open(file_path, 'r') as f:
        mob_data = json.load(f)

    mobs = {}
    for mob_entry in mob_data:
        mobs[mob_entry['id']] = Mob(
            _id=mob_entry['id'],
            name=mob_entry['name'],
            mob_type=mob_entry['type'],
            level=mob_entry['level'],
            hp=mob_entry['hp'],
            stats=mob_entry['stats'],
            loot=mob_entry['loot'],
            behavior=mob_entry['behavior']
        )

    return mobs

# Example usage
if __name__ == "__main__":
    mob_dict = load_mobs()
    for mob_id, mob_instance in mob_dict.items():
        print(mob_instance)
