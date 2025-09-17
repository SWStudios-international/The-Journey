import json

def save_game(player, current_room):
    data = {
        "player": player.to_dict(),
        "current_room": current_room.key
    }
    with open("save_game.json", "w") as f:
        json.dump(data, f)
    print("[DEBUG] Game saved to save_game.json")

def load_game(PlayerClass, world):
    with open("save_game.json", "r") as f:
        data = json.load(f)
    player = PlayerClass.from_dict(data["player"])
    current_room = world.get_room(data["current_room"])
    print(f"[DEBUG] Game loaded from save_game.json: {player.name} in {current_room.key}")
    return player, current_room
