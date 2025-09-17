import json
import random

# --- Utility Functions ---

def load_mobs(filepath="data/mobs.json"):
    with open(filepath, "r") as file:
        mobs = json.load(file)
    return mobs

def spawn_mob(mobs, level=None, behavior=None):
    eligible = mobs
    if level is not None:
        eligible = [mob for mob in mobs if mob["level"] == level]
    if behavior is not None:
        eligible = [mob for mob in eligible if mob["behavior"] == behavior]

    if not eligible:
        return None
    return random.choice(eligible)

# --- Mob Class ---

# engine/mob.py

# engine/mob.py

class Mob:
    def __init__(self, name, hp, attack=1, defense=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
        }

    @staticmethod
    def from_dict(data):
        return Mob(
            name=data["name"],
            hp=data["hp"],
            attack=data.get("attack", 1),
            defense=data.get("defense", 0),
        )



    def take_damage(self, amount):
        self.hp -= amount
        return self.hp <= 0

    def decide_action(self, player):
        if self.hp < self.max_hp * 0.3 and self.items:
            used_item = self.items.pop(0)
            self.hp += used_item.get("heal", 0)
            print(f"The {self.name} uses a {used_item['name']} and heals to {self.hp}/{self.max_hp} HP!")
            return "heal"

        if self.abilities and random.random() < 0.3:
            ability = random.choice(self.abilities)
            dmg = random.randint(ability['min_dmg'], ability['max_dmg'])
            player.hp -= dmg
            print(f"The {self.name} uses {ability['name']} and hits you for {dmg} damage!")
            return "ability"

        dmg = random.randint(1, self.attack_power)
        player.hp -= dmg
        print(f"The {self.name} attacks you for {dmg} damage!")
        return "attack"

# --- Room Class ---

class Room:
    def __init__(self, name, description, level=1):
        self.name = name
        self.description = description
        self.level = level
        self.items = []
        self.mobs = []

        all_mobs = load_mobs()
        maybe_mob = spawn_mob(all_mobs, level=self.level)
        if maybe_mob:
            self.mobs.append(maybe_mob)
