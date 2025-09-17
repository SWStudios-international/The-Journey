# ui.py

def display_welcome(player):
    print(f"Welcome back, {player.name}!")
    # ... more UI text

def display_room(room: object) -> None:
    print("\n" + room.describe())

def display_inventory(inventory):
    if inventory:
        print("\nYou rummage through your belongings:")
        for item in inventory:
            print(f" - {item}")
    else:
        print("\nYou're carrying nothing but a heavy soul.")

def display_stats(player):
    print(f"\n{player.name}'s Vital Stats")
    print("-" * 30)
    print(f"Level: {player.level}  |  XP: {player.xp}/{player.xp_to_next_level()}")
    print(f"HP: {player.hp}/{player.max_hp}")
    for stat, value in player.stats.items():
        print(f"{stat}: {value}")

def display_help():
    print("\nAvailable Commands:")
    print("- look : observe your surroundings")
    print("- go <direction> : travel to another area")
    print("- take <item> : collect an item")
    print("- inventory : view your belongings")
    print("- stats : view your character's stats")
    print("- save : save your current game")
    print("- help : show this help list")
    print("- quit : exit the game")

def display_invalid_command():
    print("\nThat ain't valid. Try again, pilgrim.")

def display_save_confirmation():
    print("\nYour grim progress has been saved.")

def display_exit():
    print("\nYou fade back into the void. Game Over.")

def display_quests(active_quests):
    print("\nActive Quests:")
    if not active_quests:
        print("- None. You're free... for now.")
    for qid, quest in active_quests.items():
        print(f"- {quest['name']}: {quest['objective']} ({quest['type']})")
