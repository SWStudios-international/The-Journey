import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as f:
        return json.load(f)

def load_all_data():
    return {
        "prefixes": load_json("prefixes.json"),
        "affixes": load_json("affixes.json"),
        "rarities": load_json("rarities.json"),
        "base_items": load_json("base_items.json")
    }
