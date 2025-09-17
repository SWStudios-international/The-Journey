class Room:
    def __init__(self, name, description, exits, items=None, actions=None, mobs=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items if items else []
        self.actions = actions if actions else {}
        self.mobs = mobs if mobs else []

    def describe(self):
        output = f"\n{self.name}\n{self.description}\n"
        if self.items:
            output += f"Items here: {', '.join(self.items)}\n"
        if self.mobs:
            mob_names = ", ".join(mob["name"] for mob in self.mobs)
            output += f"Enemies nearby: {mob_names}\n"
        output += "Exits: " + ", ".join(self.exits.keys())
        return output
