from engine.room import Room

class World:
    def __init__(self):
        self.rooms = self.generate_rooms()

    def generate_rooms(self):
        return {
            "start": Room(
                name="Living Room",
                description="You wake up in your living room. Dust dances in a beam of light.",
                exits={"north": "hallway"}
            ),
            "hallway": Room(
                name="Hallway",
                description="The hallway is narrow. Pictures of a forgotten family line the walls.",
                exits={"south": "start", "east": "kitchen", "west": "bedroom"}
            ),
            "kitchen": Room(
                name="Kitchen",
                description="Grease-stained counters and a humming fridge. There's a back door.",
                exits={"west": "hallway", "north": "backyard"}
            ),
            "bedroom": Room(
                name="Bedroom",
                description="A small room with a messy bed. Clothes are scattered everywhere.",
                exits={"east": "hallway"}
            ),
            "backyard": Room(
                name="Backyard",
                description="An overgrown backyard. A broken fence leads to a narrow alley.",
                exits={"south": "kitchen", "north": "alley"}
            ),
            "alley": Room(
    name="Alley",
    description="A dark alley filled with graffiti. Trash bins overflow.",
    exits={"south": "backyard", "north": "street"},
),

            "street": Room(
                name="Street",
                description="Cracked pavement and the sounds of distant chaos. The real world begins.",
                exits={}  # No exits—dungeon will take over here
            ),
        }

    def get_starting_room(self):
        return self.rooms["start"]

    def get_room(self, key):
        return self.rooms.get(key)
