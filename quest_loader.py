import os
import json


def load_quests():
    file_path = os.path.join(os.path.dirname(__file__), "data", "quests.json")

    with open(file_path, "r") as f:
        raw_data = json.load(f)

    quests = {}
    for entry in raw_data:
        quests[entry["id"]] = {
            "name": entry["title"],
            "type": entry["type"],
            "objective": entry["objective"],
            "location_hint": entry.get("location_hint", ""),
            "required_level": entry.get("required_level", 1),
            "reward_xp": entry["rewards"].get("xp", 0),
            "reward_gold": entry["rewards"].get("gold", 0),
            "reward_items": entry["rewards"].get("items", []),
            "followup": entry.get("followup")
        }

    return quests
