# main.py
from engine import game

if __name__ == "__main__":
    game.main()




def main():
    try:
        player = load_game()
        print(f"Loaded character: {player.name}")
    except:
        name = input("Enter your name, brave one: ")
        player = Player(name)

    display_welcome(player)  # <- Fixed here ✅
    # ✅ Move here, AFTER 'player' exists
  # <- Now it's called AFTER player is defined

    world = World()
    current_room = world.get_starting_room()
    display_room(current_room)

    handle_room_event(player, current_room)

from engine import game

if __name__ == "__main__":
    game.main()

