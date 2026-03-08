from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from BaseClasses import CollectionState
    from . import SaltSanctuaryWorld

# PROGRESSION SYSTEM

# Skill tree locations and level locations are gated by brand acquisition or boss thresholds.
# Brands are the primary progression items that unlock new areas.
# More brands = access to deeper skill tree nodes and higher levels.


# All brands for progression checks (in acquisition order)
ALL_BRANDS = [
    "Vertigo Brand",      # 1st - Sunken Keep
    "Shadowflip Brand",   # 2nd - Castle of Storms
    "Redshift Brand",     # 3rd - Mire of Stench
    "Hardlight Brand",    # 4th - Dome of the Forgotten
    "Dart Brand",         # 5th - Ziggurat of Dust
]

# Brand-based depth thresholds for skill tree nodes
# Key 0 = base depth with no brands
# Thresholds based on cumulative area access (salt income)
# Brand order: Vertigo → Shadowflip → Redshift → Hardlight → Dart
BRAND_DEPTH_THRESHOLDS = {
    "lenient": {
        0: 5,                    # No brands - early areas
        "Vertigo Brand": 9,      # + Castle of Storms
        "Shadowflip Brand": 11,  # + Red Hall, Hager's
        "Redshift Brand": 16,    # + Mire, Far Beach, Dome (big unlock)
        "Hardlight Brand": 20,   # + Cran's Pass, better navigation
        "Dart Brand": 23,        # Full tree access
    },
    "normal": {
        0: 3,
        "Vertigo Brand": 7,
        "Shadowflip Brand": 9,
        "Redshift Brand": 14,
        "Hardlight Brand": 19,
        "Dart Brand": 23,
    },
    "strict": {
        0: 1,
        "Vertigo Brand": 5,
        "Shadowflip Brand": 7,
        "Redshift Brand": 12,
        "Hardlight Brand": 17,
        "Dart Brand": 23,
    },
}
# LEVEL GATING SYSTEM

# Level locations are gated by boss reachability. Each boss kill milestone
# corresponds to a level the player is expected to reach before beating that boss.
# The rule for level N: the player must be able to reach the boss that
# corresponds to the highest threshold <= N.

# Boss progression milestones (from playtesting):
#   Sodden Knight        ~  5   (first boss, Shivering Shore)
#   Queen of Smiles      ~ 15   (Village of Smiles)
#   Mad Alchemist        ~ 20   (Watching Woods)
#   Kraekan Cyclops      ~ 25   (Sunken Keep)
#   False Jester         ~ 28   (Sunken Keep)
#   Kraekan Wyrm         ~ 35   (Castle of Storms)
#   Untouched Inquisitor ~ 40   (Dome of the Forgotten / Red Hall area)
#   Third Lamb           ~ 45   (Dome of the Forgotten)
#   Murdiella Mal        ~ 47   (Mal's Floating Castle)
#   Disemboweled Husk    ~ 50   (Hager's Cavern)
#   That Stench Most Foul~ 55   (Mire of Stench)
#   The Dried King       ~ 60   (Ziggurat of Dust)
#   The Bloodless Prince ~ 63   (Fort-Beyond-the-Mire area)
#   The Coveted          ~ 66   (Cran's Pass area)
#   Carsejaw the Cruel   ~ 70   (late game)
#   The Unskinned        ~ 73   (late game)
#   Kraekan Dragon Skourzh ~ 75 (near-final)
#   The Nameless God     ~ 80   (final boss, full playthrough)
#
# Levels 81-549 require The Nameless God for now.
# TODO: Implement NG+ gating for levels above 80 once NG+ logic is complete.
#
# Strictness adjusts thresholds by a flat offset:
#   lenient: +5 per tier (assumes more grinding)
#   normal:  exact values
#   strict:  -5 per tier (assumes minimal grinding)


# Boss-based level thresholds.
# Each entry is (level_cap, boss_location_name).
# Level N requires being able to reach the boss for the highest tier where
# level_cap >= N. None means no boss required (very early levels).
BOSS_LEVEL_THRESHOLDS = [
    (5,   None),                        # Levels 1-5: no boss required
    (15,  "The Sodden Knight"),         # Levels 6-15
    (20,  "The Queen of Smiles"),       # Levels 16-20
    (25,  "The Mad Alchemist"),         # Levels 21-25
    (28,  "Kraekan Cyclops"),           # Levels 26-28
    (35,  "The False Jester"),          # Levels 29-35
    (40,  "Kraekan Wyrm"),              # Levels 36-40
    (45,  "The Untouched Inquisitor"),  # Levels 41-45
    (47,  "The Third Lamb"),            # Levels 46-47
    (50,  "Murdiella Mal"),             # Levels 48-50
    (55,  "The Disemboweled Husk"),     # Levels 51-55
    (60,  "That Stench Most Foul"),     # Levels 56-60
    (63,  "The Dried King"),            # Levels 61-63
    (66,  "The Bloodless Prince"),      # Levels 64-66
    (70,  "The Coveted"),               # Levels 67-70
    (73,  "Carsejaw the Cruel"),        # Levels 71-73
    (75,  "The Unskinned"),             # Levels 74-75
    (80,  "Kraekan Dragon Skourzh"),    # Levels 76-80
    (549, "The Nameless God"),          # Levels 81-549 (NG+ TODO)
]

# Strictness offset applied to each tier's level cap (floor 1, no cap raised above 549)
LEVEL_STRICTNESS_OFFSET = {
    "lenient": 5,
    "normal":  0,
    "strict":  -5,
}


def create_combined_rules(
    world: 'SaltSanctuaryWorld',
    strictness: str = "normal",
    method: str = "brands",
    require_parents: bool = False,
    require_all_parents: bool = False
) -> None:
    """
    Apply access rules to skill tree locations based on depth and optionally parent requirements.
    """
    from .SkillTreeLocations import skilltree_locations
    
    player = world.player
    thresholds = BRAND_DEPTH_THRESHOLDS.get(strictness, BRAND_DEPTH_THRESHOLDS["normal"])
    
    # Find the Skill Tree region
    skill_tree_region = None
    for region in world.multiworld.regions:
        if region.name == "Skill Tree" and region.player == player:
            skill_tree_region = region
            break
    
    if skill_tree_region is None:
        return
    
    # Build node_id -> location name mapping for parent requirements
    node_id_to_name: Dict[int, str] = {}
    if require_parents:
        for name, data in skilltree_locations.items():
            node_id_to_name[data.node_id] = name
    
    # Apply rules to each location
    for location in skill_tree_region.locations:
        loc_name = location.name
        if loc_name not in skilltree_locations:
            continue
        
        loc_data = skilltree_locations[loc_name]
        loc_depth = loc_data.depth
        
        # Get parent item names if parent requirements are enabled
        parent_items: List[str] = []
        if require_parents and not loc_data.is_root:
            for parent_id in loc_data.parents:
                if parent_id >= 0 and parent_id in node_id_to_name:
                    parent_items.append(node_id_to_name[parent_id])
        
        # Create the access rule with proper closure capture
        # Access rules take only `state` as argument
        if parent_items:
            if require_all_parents:
                # Need depth check AND all parents
                location.access_rule = _make_rule_with_all_parents(
                    player, loc_depth, parent_items, thresholds
                )
            else:
                # Need depth check AND any parent
                location.access_rule = _make_rule_with_any_parent(
                    player, loc_depth, parent_items, thresholds
                )
        else:
            # Just depth check
            location.access_rule = _make_depth_rule(player, loc_depth, thresholds)


def _make_depth_rule(player: int, depth: int, thresholds: dict):
    """Create a rule that checks only depth requirements."""
    def rule(state) -> bool:
        max_depth = thresholds.get(0, 1)  # Base depth
        for brand in ALL_BRANDS:
            if state.has(brand, player):
                brand_depth = thresholds.get(brand, 0)
                if brand_depth > max_depth:
                    max_depth = brand_depth
        return depth <= max_depth
    return rule


def _make_rule_with_any_parent(player: int, depth: int, parents: List[str], thresholds: dict):
    """Create a rule that checks depth AND requires any one parent location to be reachable."""
    def rule(state) -> bool:
        # Check depth first
        max_depth = thresholds.get(0, 1)
        for brand in ALL_BRANDS:
            if state.has(brand, player):
                brand_depth = thresholds.get(brand, 0)
                if brand_depth > max_depth:
                    max_depth = brand_depth
        if depth > max_depth:
            return False
        # Check any parent location is reachable
        return any(state.can_reach_location(p, player) for p in parents)
    return rule


def _make_rule_with_all_parents(player: int, depth: int, parents: List[str], thresholds: dict):
    """Create a rule that checks depth AND requires all parent locations to be reachable."""
    def rule(state) -> bool:
        # Check depth first
        max_depth = thresholds.get(0, 1)
        for brand in ALL_BRANDS:
            if state.has(brand, player):
                brand_depth = thresholds.get(brand, 0)
                if brand_depth > max_depth:
                    max_depth = brand_depth
        if depth > max_depth:
            return False
        # Check all parent locations are reachable
        return all(state.can_reach_location(p, player) for p in parents)
    return rule


def get_locations_by_depth_range(min_depth: int, max_depth: int) -> List[str]:
    """Get all skill tree location names within a depth range."""
    from .SkillTreeLocations import skilltree_locations
    
    return [
        name for name, data in skilltree_locations.items()
        if min_depth <= data.depth <= max_depth
    ]


def create_level_rules(
    world: 'SaltSanctuaryWorld',
    strictness: str = "normal"
) -> None:
    """
    Apply access rules to level locations based on boss reachability.

    Each level location is gated by requiring the player to be able to reach
    the boss that corresponds to that level tier. The strictness offset shifts
    each tier's cap up (lenient) or down (strict) by 5 levels.
    """
    player = world.player
    offset = LEVEL_STRICTNESS_OFFSET.get(strictness, 0)

    # Build adjusted thresholds: clamp each cap to [1, 549]
    adjusted = []
    for cap, boss in BOSS_LEVEL_THRESHOLDS:
        adjusted_cap = max(1, min(549, cap + offset))
        adjusted.append((adjusted_cap, boss))

    # Find the Menu region where level locations live
    menu_region = None
    for region in world.multiworld.regions:
        if region.name == "Menu" and region.player == player:
            menu_region = region
            break

    if menu_region is None:
        return

    for location in menu_region.locations:
        if not location.name.startswith("Level "):
            continue
        try:
            level = int(location.name.split(" ")[1])
        except (IndexError, ValueError):
            continue

        location.access_rule = _make_level_rule(player, level, adjusted)


def _make_level_rule(player: int, level: int, adjusted_thresholds: list):
    """
    Create a rule that gates a level location by boss reachability.

    Finds the required boss by scanning thresholds in order and returning
    the first tier where adjusted_cap >= level.
    """
    required_boss = None
    for cap, boss in adjusted_thresholds:
        if level <= cap:
            required_boss = boss
            break

    if required_boss is None:
        # Level is beyond all defined tiers — gate by final boss
        required_boss = "The Nameless God"

    if required_boss is None:
        # Genuinely no boss required (very early levels with None tier)
        return lambda state: True

    boss_name = required_boss
    def rule(state) -> bool:
        return state.can_reach_location(boss_name, player)
    return rule
