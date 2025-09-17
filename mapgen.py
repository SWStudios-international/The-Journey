import random

ROOM_DESCRIPTORS = [
    "A flickering bulb sways from the ceiling, casting fractured shadows on the walls.",
    "The air smells like mildew and old secrets—something definitely died here.",
    "Cracked linoleum crunches beneath your feet, each step echoing like a threat.",
    "A broken vending machine hums unnaturally in the corner, blinking with corrupted code.",
    "Water drips rhythmically from a rusted pipe, like the ticking of a nervous clock.",
    "Graffiti scrawled in unknown symbols coats the walls—none of it friendly.",
    "A shattered mirror reflects everything except you.",
    "The floor is soaked in something sticky and dark. You decide not to ask questions.",
    "A faint whisper seems to follow you, but when you turn, no one is there.",
    "Stacks of ruined books lie scattered, their pages fused together by time and rot.",
    "A steel door has been welded shut with melted bone.",
    "Blood is smeared across the floor in a looping spiral pattern.",
    "The walls seem to breathe when you aren't looking directly at them.",
    "You hear breathing. It's not yours.",
    "A doll with no face sits alone in the middle of the room.",
    "Ceiling tiles hang by threads, like decaying teeth.",
    "The smell of burning hair wafts from a nearby vent.",
    "Something oily seeps from cracks in the concrete.",
    "A single shoe sits abandoned near a dark corner.",
    "A radio crackles to life, then immediately dies.",
    "There are scratch marks on the floor leading to a trapdoor.",
    "A hole in the wall pulses with faint green light.",
    "Pipes clatter above your head, followed by a splash.",
    "A rat watches you intently. It does not blink.",
    "The temperature in here is noticeably colder than the last room.",
    "All the doors are painted shut.",
    "There is a message on the wall: 'GET OUT'... freshly painted.",
    "The lights strobe violently for a few seconds, then stabilize.",
    "A breeze flows through though there are no windows.",
    "A pile of teeth is arranged neatly on a silver tray.",
    "The room smells of cinnamon and copper.",
    "A voice hums a lullaby from inside the walls.",
    "A ceiling fan spins above, slowly and loudly.",
    "A projector loops an image of an empty room.",
    "Something just brushed against your leg, but nothing's there.",
    "The wallpaper is peeling away, revealing symbols beneath.",
    "A skeletal hand sticks out from a nearby vent.",
    "There is no sound. Not even yours.",
    "The floor tilts slightly toward the center, like a shallow bowl.",
    "A locked safe hums quietly in the corner.",
    "Fungus grows in patches along the ceiling.",
    "The walls are covered in claw marks.",
    "Every light bulb is shattered, yet the room glows faintly.",
    "An eye is drawn on the floor. It blinks.",
    "You hear a child laughing. You're alone.",
    "The smell of gunpowder lingers in the air.",
    "A broken chair lies on its side, surrounded by feathers.",
    "There are drag marks leading to a heavy curtain.",
    "You swear the shadows are longer than they should be.",
    "This room was recently disturbed. But by who?"
]

def get_random_descriptor():
    return random.choice(ROOM_DESCRIPTORS)

# Example usage
if __name__ == "__main__":
    print(get_random_descriptor())