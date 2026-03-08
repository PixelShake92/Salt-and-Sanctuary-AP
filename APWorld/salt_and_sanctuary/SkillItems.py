from BaseClasses import ItemClassification
from typing import NamedTuple, Dict

SKILL_ITEM_BASE_ID = 283680000

class SkillItemData(NamedTuple):
    code: int
    classification: ItemClassification
    quantity: int  # How many of this item exist in the pool

skill_item_table: Dict[str, SkillItemData] = {

    # Swordfighter (Swords/Daggers) - itemClass 3
    # lootDef.type 0 -> num = 3
    # NOTE: Swords and Daggers SHARE itemClass 3 in the game code!
    "Swordfighter Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 0, classification=ItemClassification.useful, quantity=2),
    "Swordfighter Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 1, classification=ItemClassification.useful, quantity=2),
    "Swordfighter Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 2, classification=ItemClassification.useful, quantity=2),
    "Swordfighter Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 3, classification=ItemClassification.useful, quantity=2),
    "Swordfighter Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 4, classification=ItemClassification.useful, quantity=2),
    
    # Two-Hander (Greatswords/Greataxes) - itemClass 0
    # lootDef.type 1, 6, 17, 18, 20 -> num = 0
    # NOTE: Greatswords and Greataxes SHARE itemClass 0 in the game code!
    "Two-Hander Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 5, classification=ItemClassification.useful, quantity=2),
    "Two-Hander Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 6, classification=ItemClassification.useful, quantity=2),
    "Two-Hander Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 7, classification=ItemClassification.useful, quantity=2),
    "Two-Hander Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 8, classification=ItemClassification.useful, quantity=2),
    "Two-Hander Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 9, classification=ItemClassification.useful, quantity=2),
    
    # Heavy Macefighter (Greathammers) - itemClass 8
    # lootDef.type 7, 12 -> num = 8
    "Greathammer Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 10, classification=ItemClassification.useful, quantity=1),
    "Greathammer Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 11, classification=ItemClassification.useful, quantity=1),
    "Greathammer Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 12, classification=ItemClassification.useful, quantity=1),
    "Greathammer Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 13, classification=ItemClassification.useful, quantity=1),
    "Greathammer Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 14, classification=ItemClassification.useful, quantity=1),
    
    # Berzerker (Hammers/Axes) - itemClass 2
    # lootDef.type 2, 3 -> num = 2
    "Berzerker Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 15, classification=ItemClassification.useful, quantity=1),
    "Berzerker Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 16, classification=ItemClassification.useful, quantity=1),
    "Berzerker Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 17, classification=ItemClassification.useful, quantity=1),
    "Berzerker Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 18, classification=ItemClassification.useful, quantity=1),
    "Berzerker Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 19, classification=ItemClassification.useful, quantity=1),
    
    # Defender (Shields) - itemClass 5
    # category 1 uses itemClass[5]
    "Shield Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 20, classification=ItemClassification.useful, quantity=1),
    "Shield Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 21, classification=ItemClassification.useful, quantity=1),
    "Shield Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 22, classification=ItemClassification.useful, quantity=1),
    "Shield Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 23, classification=ItemClassification.useful, quantity=1),
    "Shield Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 24, classification=ItemClassification.useful, quantity=1),
    
    # Hunter (Whips) - itemClass 9
    # lootDef.type 11 -> num = 9
    "Hunter Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 25, classification=ItemClassification.useful, quantity=1),
    "Hunter Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 26, classification=ItemClassification.useful, quantity=1),
    "Hunter Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 27, classification=ItemClassification.useful, quantity=1),
    "Hunter Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 28, classification=ItemClassification.useful, quantity=1),
    "Hunter Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 29, classification=ItemClassification.useful, quantity=1),
    
    # Pikeman (Poleaxes/Spears/Reapers) - itemClass 14
    # lootDef.type 4, 5, 13, 19, 21 -> num = 14
    # NOTE: Reapers SHARE itemClass 14 with Poleaxes/Spears in the game code!
    "Pikeman Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 30, classification=ItemClassification.useful, quantity=2),
    "Pikeman Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 31, classification=ItemClassification.useful, quantity=2),
    "Pikeman Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 32, classification=ItemClassification.useful, quantity=2),
    "Pikeman Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 33, classification=ItemClassification.useful, quantity=2),
    "Pikeman Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 34, classification=ItemClassification.useful, quantity=2),
    
    # Archer (Bows) - itemClass 11
    # lootDef.type 8 -> num = 11
    "Bow Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 35, classification=ItemClassification.useful, quantity=1),
    "Bow Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 36, classification=ItemClassification.useful, quantity=1),
    "Bow Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 37, classification=ItemClassification.useful, quantity=1),
    "Bow Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 38, classification=ItemClassification.useful, quantity=1),
    "Bow Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 39, classification=ItemClassification.useful, quantity=1),
    
    # Marksman (Crossbows/Pistols) - itemClass 12
    # lootDef.type 9, 14 -> num = 12
    # NOTE: Crossbows and Pistols SHARE itemClass 12 in the game code!
    "Marksman Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 40, classification=ItemClassification.useful, quantity=2),
    "Marksman Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 41, classification=ItemClassification.useful, quantity=2),
    "Marksman Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 42, classification=ItemClassification.useful, quantity=2),
    "Marksman Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 43, classification=ItemClassification.useful, quantity=2),
    "Marksman Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 44, classification=ItemClassification.useful, quantity=1),  # Only 1 Class 5 node
    
    # ========== MAGIC CLASS UNLOCKS ==========
    
    # Mage (Magic/Spells) - itemClass 26
    # category 2, lootDef.values[7] <= 0 -> itemClass[26]
    "Magic Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 45, classification=ItemClassification.useful, quantity=1),
    "Magic Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 46, classification=ItemClassification.useful, quantity=1),
    "Magic Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 47, classification=ItemClassification.useful, quantity=1),
    "Magic Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 48, classification=ItemClassification.useful, quantity=1),
    "Magic Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 49, classification=ItemClassification.useful, quantity=1),
    
    # Cleric (Prayers) - itemClass 25
    # category 2, lootDef.values[7] > 0 -> checks itemClass[25] or [26] based on flags
    "Prayer Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 50, classification=ItemClassification.useful, quantity=1),
    "Prayer Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 51, classification=ItemClassification.useful, quantity=1),
    "Prayer Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 52, classification=ItemClassification.useful, quantity=1),
    "Prayer Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 53, classification=ItemClassification.useful, quantity=1),
    "Prayer Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 54, classification=ItemClassification.useful, quantity=1),
    
    # Channeler (Wands) - itemClass 27
    # lootDef.type 16 -> num = 27
    "Wand Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 55, classification=ItemClassification.useful, quantity=1),
    "Wand Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 56, classification=ItemClassification.useful, quantity=1),
    "Wand Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 57, classification=ItemClassification.useful, quantity=1),
    "Wand Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 58, classification=ItemClassification.useful, quantity=1),
    "Wand Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 59, classification=ItemClassification.useful, quantity=1),
    
    # Staff Wielder (Staves) - itemClass 10
    # lootDef.type 10 -> num = 10
    "Staff Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 60, classification=ItemClassification.useful, quantity=1),
    "Staff Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 61, classification=ItemClassification.useful, quantity=1),
    "Staff Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 62, classification=ItemClassification.useful, quantity=1),
    "Staff Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 63, classification=ItemClassification.useful, quantity=1),
    "Staff Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 64, classification=ItemClassification.useful, quantity=1),
    
    # ========== ARMOR CLASS UNLOCKS ==========
    
    # Light Armor - itemClass 28
    "Light Armor Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 65, classification=ItemClassification.useful, quantity=1),
    "Light Armor Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 66, classification=ItemClassification.useful, quantity=1),
    "Light Armor Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 67, classification=ItemClassification.useful, quantity=1),
    "Light Armor Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 68, classification=ItemClassification.useful, quantity=1),
    "Light Armor Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 69, classification=ItemClassification.useful, quantity=1),
    
    # Heavy Armor - itemClass 16
    "Heavy Armor Class 1": SkillItemData(code=SKILL_ITEM_BASE_ID + 70, classification=ItemClassification.useful, quantity=1),
    "Heavy Armor Class 2": SkillItemData(code=SKILL_ITEM_BASE_ID + 71, classification=ItemClassification.useful, quantity=1),
    "Heavy Armor Class 3": SkillItemData(code=SKILL_ITEM_BASE_ID + 72, classification=ItemClassification.useful, quantity=1),
    "Heavy Armor Class 4": SkillItemData(code=SKILL_ITEM_BASE_ID + 73, classification=ItemClassification.useful, quantity=1),
    "Heavy Armor Class 5": SkillItemData(code=SKILL_ITEM_BASE_ID + 74, classification=ItemClassification.useful, quantity=1),
    
    # ========== STAT UPGRADES ==========
    # Quantities match actual node counts in the skill tree (297 stat nodes total)
    
    "Strength Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 75, classification=ItemClassification.useful, quantity=58),
    "Endurance Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 76, classification=ItemClassification.useful, quantity=50),
    "Dexterity Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 77, classification=ItemClassification.useful, quantity=47),
    "Willpower Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 78, classification=ItemClassification.useful, quantity=62),
    "Magic Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 79, classification=ItemClassification.useful, quantity=21),
    "Wisdom Upgrade": SkillItemData(code=SKILL_ITEM_BASE_ID + 80, classification=ItemClassification.useful, quantity=29),
    
    
    "Extra Flask": SkillItemData(code=SKILL_ITEM_BASE_ID + 81, classification=ItemClassification.useful, quantity=16),
    "Extra Hearth": SkillItemData(code=SKILL_ITEM_BASE_ID + 82, classification=ItemClassification.useful, quantity=14),
}

# Mapping from skill tree location names to item names
# This handles cases where multiple skill tree nodes give the same unlock
LOCATION_TO_ITEM_MAP: Dict[str, str] = {
    # Swordfighter - covers Swordfighter and Assassin nodes (both itemClass 3)
    "Skill Tree - Class 1 Swordfighter": "Swordfighter Class 1",
    "Skill Tree - Class 2 Swordfighter": "Swordfighter Class 2",
    "Skill Tree - Class 3 Swordfighter": "Swordfighter Class 3",
    "Skill Tree - Class 4 Swordfighter": "Swordfighter Class 4",
    "Skill Tree - Class 5 Swordfighter": "Swordfighter Class 5",
    "Skill Tree - Class 1 Assassin": "Swordfighter Class 1",
    "Skill Tree - Class 2 Assassin": "Swordfighter Class 2",
    "Skill Tree - Class 3 Assassin": "Swordfighter Class 3",
    "Skill Tree - Class 4 Assassin": "Swordfighter Class 4",
    "Skill Tree - Class 5 Assassin": "Swordfighter Class 5",
    
    # Two-Hander - Heavy Swordfighter and Heavy Berzerker (both itemClass 0)
    "Skill Tree - Class 4 Heavy Swordfighter": "Two-Hander Class 4",
    "Skill Tree - Class 5 Heavy Swordfighter": "Two-Hander Class 5",
    "Skill Tree - Class 4 Heavy Berzerker": "Two-Hander Class 4",
    "Skill Tree - Class 5 Heavy Berzerker": "Two-Hander Class 5",
    
    # Heavy Macefighter (Greathammers)
    "Skill Tree - Class 1 Heavy Macefighter": "Greathammer Class 1",
    "Skill Tree - Class 2 Heavy Macefighter": "Greathammer Class 2",
    "Skill Tree - Class 3 Heavy Macefighter": "Greathammer Class 3",
    "Skill Tree - Class 4 Heavy Macefighter": "Greathammer Class 4",
    "Skill Tree - Class 5 Heavy Macefighter": "Greathammer Class 5",
    
    # Berzerker (Hammers/Axes)
    "Skill Tree - Class 1 Berzerker": "Berzerker Class 1",
    "Skill Tree - Class 2 Berzerker": "Berzerker Class 2",
    "Skill Tree - Class 3 Berzerker": "Berzerker Class 3",
    "Skill Tree - Class 4 Berzerker": "Berzerker Class 4",
    "Skill Tree - Class 5 Berzerker": "Berzerker Class 5",
    
    # Defender (Shields)
    "Skill Tree - Class 1 Defender": "Shield Class 1",
    "Skill Tree - Class 2 Defender": "Shield Class 2",
    "Skill Tree - Class 3 Defender": "Shield Class 3",
    "Skill Tree - Class 4 Defender": "Shield Class 4",
    "Skill Tree - Class 5 Defender": "Shield Class 5",
    
    # Hunter - Whip Master and Hunter nodes (itemClass 9)
    "Skill Tree - Class 1 Hunter": "Hunter Class 1",
    "Skill Tree - Class 2 Hunter": "Hunter Class 2",
    "Skill Tree - Class 3 Hunter": "Hunter Class 3",
    "Skill Tree - Class 4 Hunter": "Hunter Class 4",
    "Skill Tree - Class 5 Hunter": "Hunter Class 5",
    "Skill Tree - Class 1 Whip Master": "Hunter Class 1",
    "Skill Tree - Class 2 Whip Master": "Hunter Class 2",
    "Skill Tree - Class 3 Whip Master": "Hunter Class 3",
    "Skill Tree - Class 4 Whip Master": "Hunter Class 4",
    "Skill Tree - Class 5 Whip Master": "Hunter Class 5",
    
    # Reaper nodes use Pikeman (itemClass 14, same as Poleaxes/Spears)
    "Skill Tree - Class 1 Reaper": "Pikeman Class 1",
    "Skill Tree - Class 2 Reaper": "Pikeman Class 2",
    "Skill Tree - Class 3 Reaper": "Pikeman Class 3",
    "Skill Tree - Class 4 Reaper": "Pikeman Class 4",
    "Skill Tree - Class 5 Reaper": "Pikeman Class 5",
    
    # Pikeman (Poleaxes/Spears)
    "Skill Tree - Class 1 Pikeman": "Pikeman Class 1",
    "Skill Tree - Class 2 Pikeman": "Pikeman Class 2",
    "Skill Tree - Class 3 Pikeman": "Pikeman Class 3",
    "Skill Tree - Class 4 Pikeman": "Pikeman Class 4",
    "Skill Tree - Class 5 Pikeman": "Pikeman Class 5",
    
    # Archer (Bows)
    "Skill Tree - Class 1 Archer": "Bow Class 1",
    "Skill Tree - Class 2 Archer": "Bow Class 2",
    "Skill Tree - Class 3 Archer": "Bow Class 3",
    "Skill Tree - Class 4 Archer": "Bow Class 4",
    "Skill Tree - Class 5 Archer": "Bow Class 5",
    
    # Marksman (Crossbows/Pistols)
    "Skill Tree - Class 1 Marksman": "Marksman Class 1",
    "Skill Tree - Class 2 Marksman": "Marksman Class 2",
    "Skill Tree - Class 3 Marksman": "Marksman Class 3",
    "Skill Tree - Class 4 Marksman": "Marksman Class 4",
    "Skill Tree - Class 5 Marksman": "Marksman Class 5",
    
    # Magic User (Spells) - itemClass 26
    "Skill Tree - Class 1 Magic User": "Magic Class 1",
    "Skill Tree - Class 2 Magic User": "Magic Class 2",
    "Skill Tree - Class 3 Magic User": "Magic Class 3",
    "Skill Tree - Class 4 Magic User": "Magic Class 4",
    "Skill Tree - Class 5 Magic User": "Magic Class 5",
    
    # Cleric (Prayers) 
    "Skill Tree - Class 1 Cleric": "Prayer Class 1",
    "Skill Tree - Class 2 Cleric": "Prayer Class 2",
    "Skill Tree - Class 3 Cleric": "Prayer Class 3",
    "Skill Tree - Class 4 Cleric": "Prayer Class 4",
    "Skill Tree - Class 5 Cleric": "Prayer Class 5",
    
    # Channeler (Wands)
    "Skill Tree - Class 1 Channeler": "Wand Class 1",
    "Skill Tree - Class 2 Channeler": "Wand Class 2",
    "Skill Tree - Class 3 Channeler": "Wand Class 3",
    "Skill Tree - Class 4 Channeler": "Wand Class 4",
    "Skill Tree - Class 5 Channeler": "Wand Class 5",
    
    # Light Armor
    "Skill Tree - Class 1 Light Armor": "Light Armor Class 1",
    "Skill Tree - Class 2 Light Armor": "Light Armor Class 2",
    "Skill Tree - Class 3 Light Armor": "Light Armor Class 3",
    "Skill Tree - Class 4 Light Armor": "Light Armor Class 4",
    "Skill Tree - Class 5 Light Armor": "Light Armor Class 5",
    
    # Heavy Armor
    "Skill Tree - Class 1 Heavy Armor": "Heavy Armor Class 1",
    "Skill Tree - Class 2 Heavy Armor": "Heavy Armor Class 2",
    "Skill Tree - Class 3 Heavy Armor": "Heavy Armor Class 3",
    "Skill Tree - Class 4 Heavy Armor": "Heavy Armor Class 4",
    "Skill Tree - Class 5 Heavy Armor": "Heavy Armor Class 5",
}


def get_total_skill_items():
    """Calculate total number of skill items in pool"""
    return sum(data.quantity for data in skill_item_table.values())
