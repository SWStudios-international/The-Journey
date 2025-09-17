import random

class Combat:
    def __init__(self, player, mob):
        self.player = player
        self.mob = mob

    def start(self):
        print(f"\n⚔️ Combat initiated between {self.player.name} and {self.mob.name}!")
        while self.player.is_alive() and self.mob.hp > 0:
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

            if self.mob.hp > 0:
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
        self.mob.hp -= dmg

    def mob_attack(self):
        dmg = self.mob.attack
        print(f"The {self.mob.name} claws at you for {dmg} damage!")
        self.player.take_damage(dmg)

    def use_skill(self):
        if not hasattr(self.player, "skills") or not self.player.skills:
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
                self.mob.hp -= skill['damage']
            else:
                print("Invalid choice.")
        except ValueError:
            print("Not a number.")

    def use_spell(self):
        if not hasattr(self.player, "spells") or not self.player.spells:
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
                self.mob.hp -= spell['damage']
            else:
                print("Invalid choice.")
        except ValueError:
            print("Not a number.")

    def attempt_flee(self):
        return random.random() > 0.4

    def handle_victory(self):
        print(f"\nVictory! You defeated the {self.mob.name}!")
        self.player.gain_xp(self.mob.xp)
        self.player.gold += getattr(self.mob, "gold", 0)
        print(f"You gained {self.mob.xp} XP and {getattr(self.mob, 'gold', 0)} gold.")
        for item in getattr(self.mob, "loot", []):
            print(f"You found: {item}")
            self.player.add_to_inventory(item)

    def handle_defeat(self):
        print("You have fallen in battle. Darkness takes you.")
