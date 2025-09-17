from engine.player import Player
from engine.world import World
from engine.save_load import save_game, load_game

from engine.ui import (
    display_room,
    display_stats,
    display_inventory,
    display_help,
    display_quests,
    display_welcome,
    display_exit,
)

from engine.combat import Combat
from engine.mob import Mob
from engine.mob_spawner import spawn_mobs


def handle_room_event(player, room):
    if room.mobs:
        for mob_data in room.mobs:
            mob = Mob.from_dict(mob_data) if isinstance(mob_data, dict) else mob_data
            combat = Combat(player, mob)
            combat.start()


def main():
    try:
        player = load_game()
        print(f"Loaded character: {player.name}")
    except:
        name = input("Enter your name, brave one: ")
        player = Player(name)

    display_welcome(player)  # ✅ Now it's always safe to use `player`

    world = World()
    current_room = world.get_starting_room()
    display_room(current_room)

    handle_room_event(player, current_room)

    while player.is_alive():
        command = input("\n> ").lower().strip()

        if command in ["quit", "exit"]:
            save_game(player)
            display_exit()
            break

        elif command in ["look", "l"]:
            display_room(current_room)

        elif command in ["inventory", "i"]:
            display_inventory(player)

        elif command in ["stats", "s"]:
            display_stats(player)

        elif command in ["help", "h", "?"]:
            display_help()


        elif command.startswith("go "):

            direction = command[3:].strip()

            if direction in current_room.exits:

                next_room_key = current_room.exits[direction]

                current_room = world.get_room(next_room_key)

                display_room(current_room)

                # 🎯 BEGIN DUNGEON IF OUTSIDE

                if current_room.name.lower() == "street":

                    print("\nYou feel the world shift as you step onto the cracked asphalt...")

                    print("🌀 The journey begins now. Dungeons await.\n")

                    # Import and trigger your procedural generator

                    from engine.dungeon_generator import start_dungeon

                    start_dungeon(player)

                    break  # Exit current loop once dungeon takes over

                else:

                    handle_room_event(player, current_room)

            else:

                print("You can't go that way.")


        elif command in ["quests", "q"]:
            display_quests(player)

        elif command == "save":
            save_game(player)
            print("Game saved.")

        elif command == "spawn":
            # Dev-only command to test mobs in current room
            mob = spawn_mobs(1)[0]
            current_room.mobs.append(mob)
            print(f"A wild {mob.name} appears!")
            handle_room_event(player, current_room)

        else:
            print("Unknown command. Type 'help' for options.")

