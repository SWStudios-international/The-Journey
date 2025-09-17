from engine.room import Room
from engine.ui import display_room, display_inventory, display_stats
from engine.combat import Combat
from engine.mob import Mob
from engine.mob_spawner import spawn_mobs

def generate_dungeon(name="Dungeon", depth=3):
    dungeon = {}
    for level in range(depth):
        room_name = f"{name}-Level-{level}"
        description = f"{name} at depth {level}. Cold. Dark. You hear something move."
        exits = {}
        if level > 0:
            exits["up"] = f"{name}-Level-{level - 1}"
        if level < depth - 1:
            exits["down"] = f"{name}-Level-{level + 1}"

        dungeon[room_name] = Room(
            name=room_name,
            description=description,
            exits=exits,
            items=["rusty_knife"] if level == 0 else [],
        )
    return dungeon

def start_dungeon(player):
    print("🧱 Entering the dungeon...\n")

    dungeon = generate_dungeon("Abyssal Depths", depth=5)
    current_room_key = "Abyssal Depths-Level-0"
    current_room = dungeon[current_room_key]

    while player.is_alive():
        display_room(current_room)

        # Spawn mobs if room has none
        if not current_room.mobs:
            current_room.mobs = spawn_mobs(1)

        # Begin combat if mobs exist
        if current_room.mobs:
            for mob in current_room.mobs[:]:  # make a shallow copy
                if isinstance(mob, dict):
                    mob = Mob.from_dict(mob)
                combat = Combat(player, mob)
                combat.start()
                current_room.mobs.remove(mob)  # Remove defeated mob

        command = input("\n🗝️ What will you do? ").strip().lower()

        if command.startswith("go "):
            direction = command[3:]
            if direction in current_room.exits:
                current_room_key = current_room.exits[direction]
                current_room = dungeon[current_room_key]
            else:
                print("🚫 There's no passage that way.")

        elif command in ["inventory", "i"]:
            display_inventory(player)

        elif command in ["stats", "s"]:
            display_stats(player)

        elif command == "exit":
            print("🏃 You escape the dungeon... barely.")
            break

        else:
            print("Unknown command. Try 'go up', 'go down', 'inventory', 'stats', or 'exit'.")
