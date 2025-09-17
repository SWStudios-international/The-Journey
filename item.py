class Item:
    def __init__(self, name, slot, base_stats, rarity=None, color=None):
        self.name = name
        self.slot = slot
        self.stats = base_stats
        self.rarity = rarity
        self.color = color

    def display_name(self):
        if self.color:
            return f"{self.color}{self.name}\033[0m"
        return self.name

    def __str__(self):
        stats_display = ", ".join(f"{k}: {v}" for k, v in self.stats.items())
        return f"{self.display_name()} [{self.slot}] → {stats_display}"
