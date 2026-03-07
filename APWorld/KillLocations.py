from typing import Dict, NamedTuple

KILL_BASE_ID = 283710000


class KillLocationData(NamedTuple):
    code: int
    bestiary_name: str  # monsterDef.name - the key used by PlayerBeasts
    display_name: str   # title[0] from MonsterCatalog
    region: str         # Sub-region for AP logic (earliest vanilla spawn)


# 71 regular bestiary enemies with a few that seem unshuffled in the randomizer
# Region = earliest area where the enemy appears in vanilla
kill_locations: Dict[str, KillLocationData] = {
    # === Shivering Shore / Prologue ===
    "Kill - Marauder": KillLocationData(
        code=KILL_BASE_ID + 32, bestiary_name="marauder",
        display_name="Marauder", region="Shivering Shore post Sanctuary"),

    # === The Festering Banquet ===
    "Kill - Drowned Soldier": KillLocationData(
        code=KILL_BASE_ID + 0, bestiary_name="soldier",
        display_name="Drowned Soldier", region="Festering Banquet pre Fortress Key"),
    "Kill - Drowned Peasant": KillLocationData(
        code=KILL_BASE_ID + 3, bestiary_name="rags",
        display_name="Drowned Peasant", region="Festering Banquet pre Fortress Key"),
    "Kill - Armor Mite": KillLocationData(
        code=KILL_BASE_ID + 24, bestiary_name="crab",
        display_name="Armor Mite", region="Festering Banquet pre Fortress Key"),

    # === Bandit's Pass ===
    "Kill - Drowned Raider": KillLocationData(
        code=KILL_BASE_ID + 1, bestiary_name="raider",
        display_name="Drowned Raider", region="Bandits Pass"),
    "Kill - Drowned Bandit": KillLocationData(
        code=KILL_BASE_ID + 10, bestiary_name="bandit",
        display_name="Drowned Bandit", region="Bandits Pass"),
    "Kill - Feral Beast": KillLocationData(
        code=KILL_BASE_ID + 5, bestiary_name="dog",
        display_name="Feral Beast", region="Bandits Pass"),
    "Kill - Bloated Monstrosity": KillLocationData(
        code=KILL_BASE_ID + 9, bestiary_name="ogre",
        display_name="Bloated Monstrosity", region="Bandits Pass"),
    "Kill - Red Lord": KillLocationData(
        code=KILL_BASE_ID + 47, bestiary_name="guardian_rotten",
        display_name="Red Lord", region="Bandits Pass"),

    # === Village of Smiles ===
    "Kill - Drowned Archer": KillLocationData(
        code=KILL_BASE_ID + 2, bestiary_name="archer",
        display_name="Drowned Archer", region="Village of Smiles"),
    "Kill - Drowned Berzerker": KillLocationData(
        code=KILL_BASE_ID + 4, bestiary_name="drowned",
        display_name="Drowned Berzerker", region="Village of Smiles"),
    "Kill - Bronze Knight": KillLocationData(
        code=KILL_BASE_ID + 6, bestiary_name="knight",
        display_name="Bronze Knight", region="Village of Smiles"),
    "Kill - Blade Wraith": KillLocationData(
        code=KILL_BASE_ID + 7, bestiary_name="wraith",
        display_name="Blade Wraith", region="Village of Smiles"),
    "Kill - Skullbat": KillLocationData(
        code=KILL_BASE_ID + 12, bestiary_name="bat",
        display_name="Skullbat", region="Village of Smiles"),
    "Kill - Saltless": KillLocationData(
        code=KILL_BASE_ID + 59, bestiary_name="cult",
        display_name="Saltless", region="Village of Smiles"),

    # === Castle of Storms ===
    "Kill - Court Sorcerer": KillLocationData(
        code=KILL_BASE_ID + 11, bestiary_name="sorceror",
        display_name="Court Sorcerer", region="Castle of Storms"),
    "Kill - Armor Guardian": KillLocationData(
        code=KILL_BASE_ID + 13, bestiary_name="golem",
        display_name="Armor Guardian", region="Castle of Storms"),
    "Kill - Bronze Axe Knight": KillLocationData(
        code=KILL_BASE_ID + 37, bestiary_name="knight_axe",
        display_name="Bronze Axe Knight", region="Castle of Storms"),

    # === Sunken Keep ===
    "Kill - Rotten Walker": KillLocationData(
        code=KILL_BASE_ID + 25, bestiary_name="zombie",
        display_name="Rotten Walker", region="Sunken Keep"),
    "Kill - Rotten Crossbowman": KillLocationData(
        code=KILL_BASE_ID + 26, bestiary_name="zombow",
        display_name="Rotten Crossbowman", region="Sunken Keep"),

    # === Watching Woods ===
    "Kill - Poison Cytoplasm": KillLocationData(
        code=KILL_BASE_ID + 8, bestiary_name="blob",
        display_name="Poison Cytoplasm", region="Watching Woods"),
    "Kill - Retchfeeder": KillLocationData(
        code=KILL_BASE_ID + 14, bestiary_name="fiend",
        display_name="Retchfeeder", region="Watching Woods"),
    "Kill - Vilehawk": KillLocationData(
        code=KILL_BASE_ID + 15, bestiary_name="hawk",
        display_name="Vilehawk", region="Watching Woods"),
    "Kill - Spear Imp": KillLocationData(
        code=KILL_BASE_ID + 19, bestiary_name="imp",
        display_name="Spear Imp", region="Watching Woods"),
    "Kill - Clay Phantom": KillLocationData(
        code=KILL_BASE_ID + 17, bestiary_name="phantasm",
        display_name="Clay Phantom", region="Watching Woods"),

    # === Red Hall of Cages ===
    "Kill - Gaoler": KillLocationData(
        code=KILL_BASE_ID + 16, bestiary_name="gaoler",
        display_name="Gaoler", region="Red Hall of Cages"),
    "Kill - Torturer": KillLocationData(
        code=KILL_BASE_ID + 18, bestiary_name="torturer",
        display_name="Torturer", region="Red Hall of Cages"),
    "Kill - Chained Man": KillLocationData(
        code=KILL_BASE_ID + 20, bestiary_name="tortured",
        display_name="Chained Man", region="Red Hall of Cages"),
    "Kill - Caged Man": KillLocationData(
        code=KILL_BASE_ID + 21, bestiary_name="hookman",
        display_name="Caged Man", region="Red Hall of Cages"),
    "Kill - Vile Guard": KillLocationData(
        code=KILL_BASE_ID + 34, bestiary_name="torturer_bow",
        display_name="Vile Guard", region="Red Hall of Cages"),

    # === Hager's Cavern ===
    "Kill - Bedspider": KillLocationData(
        code=KILL_BASE_ID + 31, bestiary_name="spider",
        display_name="Bedspider", region="Hagers Cavern"),
    "Kill - Dropspider": KillLocationData(
        code=KILL_BASE_ID + 35, bestiary_name="spider_blue",
        display_name="Dropspider", region="Hagers Cavern"),
    "Kill - Spindlebeast": KillLocationData(
        code=KILL_BASE_ID + 39, bestiary_name="littlecorn",
        display_name="Spindlebeast", region="Hagers Cavern"),
    "Kill - Cave Keeper": KillLocationData(
        code=KILL_BASE_ID + 54, bestiary_name="angler",
        display_name="Cave Keeper", region="Hagers Cavern"),

    # === Mire of Stench ===
    "Kill - Stenchpod": KillLocationData(
        code=KILL_BASE_ID + 29, bestiary_name="gasface",
        display_name="Stenchpod", region="Mire of Stench"),
    "Kill - Lepris": KillLocationData(
        code=KILL_BASE_ID + 30, bestiary_name="bandages",
        display_name="Lepris", region="Mire of Stench"),

    # === Dome of the Forgotten ===
    "Kill - Angsty Bones": KillLocationData(
        code=KILL_BASE_ID + 22, bestiary_name="skeleton",
        display_name="Angsty Bones", region="Dome of the Forgotten"),
    "Kill - Primitive Bones": KillLocationData(
        code=KILL_BASE_ID + 23, bestiary_name="skeleton_tribe",
        display_name="Primitive Bones", region="Dome of the Forgotten"),
    "Kill - Emberskull": KillLocationData(
        code=KILL_BASE_ID + 27, bestiary_name="skull",
        display_name="Emberskull", region="Dome of the Forgotten"),
    "Kill - Pale Witch": KillLocationData(
        code=KILL_BASE_ID + 28, bestiary_name="witch",
        display_name="Pale Witch", region="Dome of the Forgotten"),
    "Kill - Hunting Bones": KillLocationData(
        code=KILL_BASE_ID + 33, bestiary_name="skeleton_archer",
        display_name="Hunting Bones", region="Dome of the Forgotten"),
    "Kill - Whisperman": KillLocationData(
        code=KILL_BASE_ID + 36, bestiary_name="ghost",
        display_name="Whisperman", region="Dome of the Forgotten"),
    "Kill - Lietch": KillLocationData(
        code=KILL_BASE_ID + 40, bestiary_name="lich",
        display_name="Lietch", region="Dome of the Forgotten"),
    "Kill - Whisperlady": KillLocationData(
        code=KILL_BASE_ID + 62, bestiary_name="ghostwitch",
        display_name="Whisperlady", region="Dome of the Forgotten"),

    # === Mal's Floating Castle ===
    "Kill - Bound Arrox": KillLocationData(
        code=KILL_BASE_ID + 41, bestiary_name="troll",
        display_name="Bound Arrox", region="Mals Floating Castle"),
    "Kill - Vexing Brat": KillLocationData(
        code=KILL_BASE_ID + 42, bestiary_name="bluetroll",
        display_name="Vexing Brat", region="Mals Floating Castle"),
    "Kill - Vacant Blades": KillLocationData(
        code=KILL_BASE_ID + 43, bestiary_name="bluewraith",
        display_name="Vacant Blades", region="Mals Floating Castle"),
    "Kill - Fetal Brat": KillLocationData(
        code=KILL_BASE_ID + 44, bestiary_name="betus",
        display_name="Fetal Brat", region="Mals Floating Castle"),
    "Kill - Mother Merle": KillLocationData(
        code=KILL_BASE_ID + 69, bestiary_name="birdy",
        display_name="Mother Merle", region="Mals Floating Castle"),

    # === Salt Alkymancery ===
    "Kill - Split Swordsman": KillLocationData(
        code=KILL_BASE_ID + 45, bestiary_name="split",
        display_name="Split Swordsman", region="Salt Alkymancery"),
    "Kill - Hornet Steel": KillLocationData(
        code=KILL_BASE_ID + 46, bestiary_name="gold_archer",
        display_name="Hornet Steel", region="Salt Alkymancery"),
    "Kill - Heartseeker": KillLocationData(
        code=KILL_BASE_ID + 49, bestiary_name="eyeball",
        display_name="Heartseeker", region="Salt Alkymancery"),
    "Kill - Bola Eye": KillLocationData(
        code=KILL_BASE_ID + 51, bestiary_name="eyescorpion",
        display_name="Bola Eye", region="Salt Alkymancery"),
    "Kill - Saltbat": KillLocationData(
        code=KILL_BASE_ID + 55, bestiary_name="saltbat",
        display_name="Saltbat", region="Salt Alkymancery"),
    "Kill - Alkymancery Knight": KillLocationData(
        code=KILL_BASE_ID + 56, bestiary_name="saltknight",
        display_name="Alkymancery Knight", region="Salt Alkymancery"),

    # === The Ruined Temple ===
    "Kill - Thing of Arms": KillLocationData(
        code=KILL_BASE_ID + 57, bestiary_name="arms",
        display_name="Thing of Arms", region="Ruined Temple"),
    "Kill - Flying Spider": KillLocationData(
        code=KILL_BASE_ID + 58, bestiary_name="greenspider",
        display_name="Flying Spider", region="Ruined Temple"),

    # === Pitchwoods ===
    "Kill - Hanged Man": KillLocationData(
        code=KILL_BASE_ID + 48, bestiary_name="hangman",
        display_name="Hanged Man", region="Pitchwoods"),
    "Kill - Dread Horseman": KillLocationData(
        code=KILL_BASE_ID + 50, bestiary_name="horseknight",
        display_name="Dread Horseman", region="Pitchwoods"),
    "Kill - Impaled Knight": KillLocationData(
        code=KILL_BASE_ID + 65, bestiary_name="horsehead",
        display_name="Impaled Knight", region="Pitchwoods"),

    # === Siam Lake ===
    "Kill - Saltfin Creature": KillLocationData(
        code=KILL_BASE_ID + 38, bestiary_name="piranha",
        display_name="Saltfin Creature", region="Siam Lake"),

    # === Crypt of Dead Gods ===
    "Kill - Gravewalker": KillLocationData(
        code=KILL_BASE_ID + 60, bestiary_name="stonesoul",
        display_name="Gravewalker", region="Crypt of Dead Gods"),
    "Kill - Crypt Keeper": KillLocationData(
        code=KILL_BASE_ID + 61, bestiary_name="cryptkeeper",
        display_name="Crypt Keeper", region="Crypt of Dead Gods"),

    # === Ziggurat of Dust ===
    "Kill - Clay Hybrid": KillLocationData(
        code=KILL_BASE_ID + 52, bestiary_name="squidface",
        display_name="Clay Hybrid", region="Ziggurat of Dust"),
    "Kill - Mimku": KillLocationData(
        code=KILL_BASE_ID + 70, bestiary_name="squidmimic",
        display_name="Mimku", region="Ziggurat of Dust"),

    # === The Still Palace ===
    "Kill - Drowned Porcelain": KillLocationData(
        code=KILL_BASE_ID + 63, bestiary_name="doll",
        display_name="Drowned Porcelain", region="The Still Palace"),
    "Kill - Wrathful Dead": KillLocationData(
        code=KILL_BASE_ID + 64, bestiary_name="nightmare",
        display_name="Wrathful Dead", region="The Still Palace"),
    "Kill - Drowned Marauder": KillLocationData(
        code=KILL_BASE_ID + 66, bestiary_name="maraudzom",
        display_name="Drowned Marauder", region="The Still Palace"),
    "Kill - Rotten Raider": KillLocationData(
        code=KILL_BASE_ID + 67, bestiary_name="zomblack",
        display_name="Rotten Raider", region="The Still Palace"),
    "Kill - White Knight": KillLocationData(
        code=KILL_BASE_ID + 68, bestiary_name="knight_white",
        display_name="White Knight", region="The Still Palace"),

    # Sanctuary Desecration (no fixed location) ===
    "Kill - Sanctuary Guard": KillLocationData(
        code=KILL_BASE_ID + 53, bestiary_name="guardian_gen",
        display_name="Sanctuary Guard", region="Menu"),
}

# Reverse lookup: bestiary_name -> AP location name
bestiary_to_location: Dict[str, str] = {
    data.bestiary_name: loc_name
    for loc_name, data in kill_locations.items()
}
