import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.xp = 0
        self.level = 1
        self.gold = 0
        self.inventory = []
        self.skills = []  # [{'name': 'Slash', 'damage': 10}]
        self.spells = []  # [{'name': 'Fireball', 'damage': 12}]

    def is_alive(self):
        return self.hp > 0

    def get_base_damage(self):
        return 5 + self.level  # Example base damage logic

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level += 1
            self.max_hp += 10
            self.hp = self.max_hp
            print(f"{self.name} leveled up! Now level {self.level}!")

    def add_to_inventory(self, item):
        self.inventory.append(item)

class Combat:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob  # now a Mob class, not a dict

    def start(self):
        print(f"\n⚔️ Combat initiated between {self.player.name} and {self.mob.name}!")
        while self.player.is_alive() and self.mob.is_alive():
            self.show_status()
            action = input("Choose action (attack, skill, spell, flee): ").strip().lower()
            if action == "attack":
                self.player_attack()
            elif action == "skill":
                self.use_skill()
            elif action == "spell":
                self.use_spell()
            elif action == "flee":
                if self.attempt_flee():
                    print("You fled successfully.")
                    return
                else:
                    print("Failed to flee!")
            else:
                print("Invalid action.")
                continue

            if self.mob.is_alive():
                self.mob_attack()

        if self.player.is_alive():
            self.handle_victory()
        else:
            self.handle_defeat()

    def show_status(self):
        print(f"\n{self.player.name} HP: {self.player.hp}/{self.player.max_hp} | {self.mob.name} HP: {self.mob.hp}/{self.mob.max_hp}")

    def player_attack(self):
        dmg = self.player.get_base_damage()
        print(f"You strike the {self.mob.name} for {dmg} damage!")
        self.mob.take_damage(dmg)

    def mob_attack(self):
        self.mob.decide_action(self.player)

    def use_skill(self):
        if not self.player.skills:
            print("You have no skills yet.")
            return
        print("Available skills:")
        for idx, skill in enumerate(self.player.skills):
            print(f"  {idx + 1}. {skill['name']} (DMG: {skill['damage']})")
        try:
            choice = int(input("Choose skill number: ")) - 1
            if 0 <= choice < len(self.player.skills):
                skill = self.player.skills[choice]
                print(f"You use {skill['name']}! It hits for {skill['damage']} damage!")
                self.mob.take_damage(skill['damage'])
            else:
                print("Invalid choice.")
        except ValueError:
            print("Not a number.")

    def use_spell(self):
        if not self.player.spells:
            print("You have no spells yet.")
            return
        print("Available spells:")
        for idx, spell in enumerate(self.player.spells):
            print(f"  {idx + 1}. {spell['name']} (DMG: {spell['damage']})")
        try:
            choice = int(input("Choose spell number: ")) - 1
            if 0 <= choice < len(self.player.spells):
                spell = self.player.spells[choice]
                print(f"You cast {spell['name']}! It blasts for {spell['damage']} damage!")
                self.mob.take_damage(spell['damage'])
            else:
                print("Invalid choice.")
        except ValueError:
            print("Not a number.")

    def attempt_flee(self):
        return random.random() > 0.4

    def handle_victory(self):
        print(f"\nVictory! You defeated the {self.mob.name}!")

        # XP Gain
        xp_gain = self.mob.attack_power + random.randint(1, 3)
        self.player.gain_xp(xp_gain)

        # Gold Gain
        gold_loot = self.mob.loot.get('gold', 0)
        self.player.gold += gold_loot
        print(f"You gained {xp_gain} XP and {gold_loot} gold.")

        # Item Loot
        items = self.mob.loot.get('items', [])
        if items:
            for item in items:
                print(f"You found: {item['name']}")
                self.player.add_to_inventory(item)

    def handle_defeat(self):
        print("You have fallen in battle. Darkness takes you.")
