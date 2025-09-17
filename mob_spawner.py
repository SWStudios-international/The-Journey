# engine/mob_spawner.py

import random
from engine.mob import Mob

def spawn_mobs(count=1):
    mobs = []
    for _ in range(count):
        mob = Mob(
            name=random.choice(["Rat", "Goblin", "Skeleton", "Worm"]),
            hp=random.randint(5, 15),
            attack=random.randint(2, 5),
            defense=random.randint(0, 2),
        )
        mobs.append(mob)
    return mobs
