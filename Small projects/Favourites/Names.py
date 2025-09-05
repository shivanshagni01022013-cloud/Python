import random

brand_names_amt = int(input("How many brand names do you want: "))
list1 = [
    # Professional / Business-like
    "Global", "Prime", "Vision", "Next", "Future", "Edge", "Summit", "Bright", "Core", "Peak",
    "Capital", "Growth", "United", "First", "Smart", "Swift", "Elite", "True", "Urban",
    "Blue", "Green", "Silver", "Gold", "Crystal", "Stone", "Iron", "Steel", "Dynamic", "Bold",
    "Matrix", "Vertex", "Nova", "Quantum", "Fusion", "Spark", "Royal", "Pure", "Infinite", "Horizon",
    "Creative", "Beacon", "Sky", "Cloud", "River", "Ocean", "Valley", "Harbor", "Bridge", "Tower",
    "Square", "Circle", "Axis", "Point", "Vista", "Metro", "City", "Nation", "World",
    "Nexus", "Alpha", "Beta", "Omega", "Zenith", "Pinnacle", "Legend", "Icon", "Epic", "Legacy",
    "Trust", "Alliance", "Network", "Solutions", "Systems", "Ventures", "Technologies",

    # Funny / Quirky (but still single words)
    "Potato", "Pickle", "Noodle", "Waffle", "Biscuit", "Muffin", "Donut", "Llama", "Penguin", "Moose",
    "Goose", "Chicken", "Frog", "Snail", "Pigeon", "Parrot", "Jellyfish", "Octopus", "Taco", "Marshmallow",
    "Sock", "Robot", "Ninja", "Pirate", "Wizard", "Knight", "Clumsy", "Sleepy", "Grumpy", "Fuzzy",
    "Spicy", "Bouncy", "Silly", "Giggle", "Dizzy", "Zappy", "Loopy", "Wobbly", "Jumpy", "Cheeky"
]

list2 = [
    # Professional / Business-like
    "Atlas", "Summitry", "Crest", "Momentum", "Pulse", "Vertexon", "Elevate", "Clarity", "Radius", "Vector",
    "Optima", "Strive", "Aspire", "Endure", "Noble", "Valor", "Integrity", "Unity", "Magnet", "Orbit",
    "Solaris", "Lunar", "Stellar", "Celestial", "Terra", "Aero", "Hydra", "Ignite", "Ember", "Radiant",
    "Keystone", "Monarch", "Crown", "Empire", "Domain", "Haven", "Summons", "Pillar", "Forge", "Titan",
    "Momentum", "Flow", "Rise", "Shift", "Aspect", "Element", "Vectora", "Frontier", "Cascade", "SummitX",
    "Prism", "Aurora", "Eclipse", "Orbitron", "Nebula", "Vortex", "Mirage", "Mythic", "Phantom", "Spectra",
    "Unityx", "Omni", "Synergy", "Paragon", "Kepler", "Cosmos", "Gravity", "Aether", "Pulseon", "Lumina",

    # Funny / Quirky
    "Picko", "Spud", "Carrot", "Cabbage", "Turnip", "Radish", "Peanut", "Cashew", "Walnut", "Hazelnut",
    "Choco", "Gummy", "Jelly", "Pudding", "Cookiez", "Popcorn", "Nacho", "Churro", "Burrito", "Queso",
    "Otter", "Seal", "Walrus", "Hedgehog", "Ferret", "Badger", "Koala", "Sloth", "Yak", "Zebra",
    "Bumble", "Buzz", "Chirpy", "Fluffy", "Squishy", "Boingy", "Cranky", "Zippy", "Whizzy", "Snappy"
]

list3 = [
    # Professional / Business-like
    "Summitron", "Evolve", "Pioneer", "Advance", "MomentumX", "Climb", "Ascent", "Vectorial", "Cobalt", "Platinum",
    "Diamond", "Emerald", "Onyx", "Topaz", "Obsidian", "Granite", "Marble", "Sapphire", "Opal", "Jade",
    "Keystar", "Centric", "Orbitum", "Velocity", "Propel", "Elevon", "Catalyst", "Engine", "Momentumis", "Ion",
    "Circuit", "Pixel", "Nano", "Micro", "Macro", "TerraX", "DataCore", "Infinitum", "Continuum", "Vertexa",
    "Spectrum", "Lumen", "Radiance", "Flare", "Glint", "Pulsecore", "Energyx", "Magnetron", "Axison", "Starlite",
    "Aurix", "Solara", "Eterna", "Mythos", "Legendary", "Chronos", "Krypton", "AtlasX", "Helios", "Orion",
    "Centauri", "Astral", "Astro", "Zenon", "Vectoris", "Polaris", "Titanic", "Cyclone", "Vanguard", "Guardian",

    # Funny / Quirky
    "Tater", "Squash", "Pumpkin", "Melonix", "Lemon", "Berry", "Cherry", "Mangoose", "Appleton", "Peachy",
    "Cupcake", "Brownie", "Donutz", "Cinnabon", "Scone", "Waffleez", "Noodlez", "Tortilla", "Dumpling", "Bao",
    "Otto", "Panda", "Yakky", "Meerkat", "Alpaca", "Goaty", "Horsey", "Doggo", "Kitty", "Birb",
    "Zonky", "Wacky", "Loony", "Blinky", "Chompy", "Munchy", "Flopsy", "Jumpyx", "Snorky", "Wiggly"
]

def names():
    print(random.choice(list1), random.choice(list2), random.choice(list3))

for i in range(1, brand_names_amt+1):
    names()

