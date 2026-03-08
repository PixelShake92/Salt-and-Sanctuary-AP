# Region data for Salt and Sanctuary APWorld
# Sub-region system based on working reference logic
# Provides granular entrance-based logic for brand/key/lever gates
from typing import Dict, List, Set, Optional, NamedTuple, TYPE_CHECKING
from BaseClasses import Region, Entrance, Item, ItemClassification, Location
from .Items import SaltSanctuaryItem
from .Locations import SaltSanctuaryLocation

if TYPE_CHECKING:
    from . import SaltSanctuaryWorld

# ============================================================================
# SUB-REGION DEFINITIONS
# These divide each game area into sections gated by bosses, keys, brands, 
# or levers. The connections between sub-regions carry the logic rules.
# ============================================================================

SUBREGION_NAMES = [
    "Menu",
    # Shivering Shore
    "Shivering Shore pre Sanctuary",
    "Shivering Shore post Sanctuary",
    # Festering Banquet
    "Festering Banquet pre Fortress Key",
    "Festering Banquet post Fortress Key",
    "Festering Banquet post Vertigo West",
    "Festering Banquet post Vertigo East",
    # Bandit's Pass
    "Bandits Pass",
    "Bandits Pass post Bronze Key",
    "Bandits Pass post Vertigo",
    # Village of Smiles
    "Village of Smiles",
    "Village of Smiles post Vertigo",
    "Village of Smiles post Shadowflip",
    # Watching Woods
    "Watching Woods",
    "Watching Woods post Mad Alchemist",
    # Sunken Keep
    "Sunken Keep",
    "Sunken Keep post Kraeken Cyclops",
    "Sunken Keep post False Jester",
    "Sunken Keep post Vertigo pre Jester",
    "Sunken Keep post Vertigo East",
    "Sunken Keep post Vertigo West",
    "Sunken Keep post Shadowflip",
    # Castle of Storms (requires Vertigo to reach)
    "Castle of Storms",
    "Castle of Storms post Kraeken Wyrm",
    "Castle of Storms post Shadowflip",
    "Castle of Storms post Jagged Key",
    "Castle of Storms post Hardlight",
    "Castle of Storms post Shadowflip and Hardlight",
    # Red Hall of Cages
    "Red Hall of Cages",
    # Hager's Cavern
    "Hagers Cavern",
    "Hagers Cavern post Cellar Key",
    "Hagers Cavern post Spiked Key",
    "Hagers Cavern post Mire of Stench",
    "Hagers Cavern post Brands",
    # Mire of Stench
    "Mire of Stench",
    # Fort Beyond the Mire
    "Fort Beyond the Mire",
    "Fort Beyond the Mire post Hardlight",
    # Cran's Pass
    "Crans Pass",
    "Crans Pass post Ronin Cran",
    "Crans Pass post Salt Alkymancery",
    # The Far Beach
    "The Far Beach",
    # Dome of the Forgotten
    "Dome of the Forgotten",
    "Dome of the Forgotten post Untouched Inquisitor",
    "Dome of the Forgotten post Hardlight",
    "Dome of the Forgotten post Third Lamb",
    # Ziggurat of Dust
    "Ziggurat of Dust",
    "Ziggurat of Dust post Dried King",
    "Ziggurat of Dust post Redshift post Dart",
    "Ziggurat of Dust post Hardlight",
    # Mal's Floating Castle (requires Vertigo + Hardlight)
    "Mals Floating Castle",
    "Mals Floating Castle post Murdiella Mal",
    # Ruined Temple
    "Ruined Temple",
    "Ruined Temple post Hardlight",
    "Ruined Temple post Dart",
    "Ruined Temple post The Coveted",
    # Pitchwoods
    "Pitchwoods",
    "Pitchwoods Far Beach entrance",
    "Pitchwoods post Dart",
    "Pitchwoods post Carsejaw the Cruel",
    # Siam Lake
    "Siam Lake",
    "Siam Lake post Salt Alkymancery",
    # The Blackest Vault
    "The Blackest Vault",
    "The Blackest Vault post Bone Key",
    # Salt Alkymancery (requires Dart + Shadowflip to reach)
    "Salt Alkymancery",
    "Salt Alkymancery post Hardlight",
    "Salt Alkymancery post The Unskinned and The Architect",
    # Crypt of Dead Gods
    "Crypt of Dead Gods",
    # The Still Palace
    "The Still Palace",
]


# ============================================================================
# LOCATION-TO-SUBREGION MAPPING
# Maps our location names to their correct sub-region.
# Default: all locations in an area go to the base (most accessible) sub-region
# Overrides: boss fights and gated items go to specific sub-regions
# ============================================================================

# Default mapping: our old coarse region name -> default sub-region name
_DEFAULT_SUBREGION = {
    "Shivering Shore": "Shivering Shore post Sanctuary",
    "The Festering Banquet": "Festering Banquet pre Fortress Key",
    "Bandit's Pass": "Bandits Pass",
    "Village of Smiles": "Village of Smiles",
    "The Watching Woods": "Watching Woods",
    "Sunken Keep": "Sunken Keep",
    "Castle of Storms": "Castle of Storms",
    "Mal's Floating Castle": "Mals Floating Castle",
    "Red Hall of Cages": "Red Hall of Cages",
    "Hager's Cavern": "Hagers Cavern",
    "Hager's Cavern - Spiked Door": "Hagers Cavern post Spiked Key",
    "Cran's Pass": "Crans Pass",
    "Mire of Stench": "Mire of Stench",
    "Fort-Beyond-the-Mire": "Fort Beyond the Mire",
    "The Far Beach": "The Far Beach",
    "Dome of the Forgotten": "Dome of the Forgotten",
    "Ziggurat of Dust": "Ziggurat of Dust",
    "The Ruined Temple": "Ruined Temple",
    "Pitchwoods": "Pitchwoods",
    "Siam Lake": "Siam Lake",
    "The Blackest Vault": "The Blackest Vault",
    "Salt Alkymancery": "Salt Alkymancery",
    "Crypt of Dead Gods": "Crypt of Dead Gods",
    "The Still Palace": "The Still Palace",
}

# Specific location overrides for boss fights and gated content
_LOCATION_OVERRIDES = {
    # Shivering Shore - Unspeakable Deep is before first sanctuary
    "The Unspeakable Deep": "Shivering Shore pre Sanctuary",
    "The Unspeakable Deep - Drop": "Shivering Shore pre Sanctuary",
    "Shivering Shore - Sanctuary Key": "Shivering Shore pre Sanctuary",

    # Watching Woods - Mad Alchemist is in a gated area
    "The Mad Alchemist": "Watching Woods post Mad Alchemist",
    "The Mad Alchemist - Drop": "Watching Woods post Mad Alchemist",

    # Mal's Floating Castle - Murdiella Mal is the boss
    "Murdiella Mal": "Mals Floating Castle post Murdiella Mal",
    "Murdiella Mal - Drop": "Mals Floating Castle post Murdiella Mal",

    # Dome of the Forgotten - Bosses are in post-boss sub-regions
    "The Untouched Inquisitor": "Dome of the Forgotten post Untouched Inquisitor",
    "The Untouched Inquisitor - Drop": "Dome of the Forgotten post Untouched Inquisitor",
    "The Third Lamb": "Dome of the Forgotten post Third Lamb",
    "The Third Lamb - Drop": "Dome of the Forgotten post Third Lamb",

    # Ziggurat of Dust - Dried King is post-hardlight boss
    "The Dried King": "Ziggurat of Dust post Dried King",
    "The Dried King - Drop": "Ziggurat of Dust post Dried King",

    # Cran's Pass - Ronin Cran requires Hardlight + Redshift
    "Ronin Cran": "Crans Pass post Ronin Cran",
    "Ronin Cran - Drop": "Crans Pass post Ronin Cran",

    # Ruined Temple - The Coveted is a boss gate
    "The Coveted": "Ruined Temple post The Coveted",
    "The Coveted - Drop": "Ruined Temple post The Coveted",

    # Pitchwoods - Carsejaw requires Dart
    "Carsejaw the Cruel": "Pitchwoods post Carsejaw the Cruel",
    "Carsejaw the Cruel - Drop": "Pitchwoods post Carsejaw the Cruel",

    # Castle of Storms - Kraeken Wyrm
    "Kraekan Wyrm": "Castle of Storms post Kraeken Wyrm",
    "Kraekan Wyrm - Drop": "Castle of Storms post Kraeken Wyrm",

    # Castle of Storms - Assassin Set requires Hardlight (or elevator + Dart)
    "Castle of Storms - Assassin's Cowl": "Castle of Storms post Hardlight",
    "Castle of Storms - Assassin Set (1)": "Castle of Storms post Hardlight",
    "Castle of Storms - Assassin Set (2)": "Castle of Storms post Hardlight",
    "Castle of Storms - Assassin Set (3)": "Castle of Storms post Hardlight",
    "Castle of Storms - Assassin Set (4)": "Castle of Storms post Hardlight",

    # Hager's Cavern - Frozen Locket x3 requires Redshift + Hardlight + Shadowflip
    "Hager's Cavern - Frozen Locket x3": "Hagers Cavern post Brands",

    # Fort-Beyond-the-Mire - Stardust Spire requires Hardlight
    "Fort-Beyond-the-Mire - Stardust Spire": "Fort Beyond the Mire post Hardlight",

    # Sunken Keep - Lamprey Set requires Shadowflip
    "Sunken Keep - Lamprey Barbut": "Sunken Keep post Shadowflip",
    "Sunken Keep - Lamprey Cuirass": "Sunken Keep post Shadowflip",
    "Sunken Keep - Lamprey Barbut Set (1)": "Sunken Keep post Shadowflip",
    "Sunken Keep - Lamprey Barbut Set (2)": "Sunken Keep post Shadowflip",
    "Sunken Keep - Lamprey Cuirass Set (1)": "Sunken Keep post Shadowflip",
    "Sunken Keep - Lamprey Cuirass Set (2)": "Sunken Keep post Shadowflip",
}


def get_subregion_for_location(loc_name: str, old_region: str) -> str:
    """Get the sub-region name for a location, using overrides or default mapping."""
    if loc_name in _LOCATION_OVERRIDES:
        return _LOCATION_OVERRIDES[loc_name]
    return _DEFAULT_SUBREGION.get(old_region, old_region)


# ============================================================================
# LEVER / GATE DATA
# Levers are Character entities that use script command 37 to:
#   - Call MapMgr.FireSequence(c.drops[]) to open gates  
#   - Call PlayerMgr.SetMainPlayerFlag(c.flag) to persist state
#
# Each lever has:
#   item_name:       AP item name (gates entrance rules)
#   sub_region:      which sub-region the lever location lives in
#   location_name:   AP location name (client sends check when pulled)
#   game_flag:       c.flag - the player flag set by SetMainPlayerFlag()
#   game_sequences:  c.drops[] - sequence names fired by MapMgr.FireSequence()
#
# The client mod should:
#   ON RECEIVING LEVER ITEM:
#     PlayerMgr.SetMainPlayerFlag(game_flag);
#     MapMgr.FireSequence(game_sequences);  // if on same map
#   ON PLAYER PULLING LEVER IN-GAME:
#     Intercept → send AP location check (don't let vanilla activation happen)
#
# Lever data populated from dnSpy inspection of CharScript entities
# ============================================================================

LEVER_ITEM_BASE_ID = 283640700
LEVER_LOC_BASE_ID = 283660400


class LeverData(NamedTuple):
    item_name: str
    sub_region: str
    location_name: str
    game_flag: str          # c.flag - player flag name
    game_sequences: List[str]  # c.drops[] - sequence names to fire
    item_id_offset: int     # offset from LEVER_ITEM_BASE_ID
    loc_id_offset: int      # offset from LEVER_LOC_BASE_ID


LEVERS = [
    LeverData(
        item_name="Bandit's Pass - Cave Door",
        sub_region="Bandits Pass",
        location_name="Bandit's Pass - Cave Door Lever",
        game_flag="cavedoorswitch1",
        game_sequences=["cavedoor"],
        item_id_offset=0, loc_id_offset=0,
    ),
    LeverData(
        item_name="Castle of Storms - Castle Bridge",
        sub_region="Castle of Storms",
        location_name="Castle of Storms - Castle Bridge Lever",
        game_flag="castlebridgedropf",
        game_sequences=["castlebridgedrop"],
        item_id_offset=1, loc_id_offset=1,
    ),
    LeverData(
        item_name="Castle of Storms - Ledge Elevator",
        sub_region="Castle of Storms",
        location_name="Castle of Storms - Ledge Elevator",
        game_flag="ledge_edge_plat1",
        game_sequences=["ledge_edge_plat"],
        item_id_offset=2, loc_id_offset=2,
    ),
    LeverData(
        item_name="Castle of Storms - Middle Elevator",
        sub_region="Castle of Storms",
        location_name="Castle of Storms - Middle Elevator",
        game_flag="middle_double_plat1",
        game_sequences=["middle_double_plat"],
        item_id_offset=3, loc_id_offset=3,
    ),
    LeverData(
        item_name="Castle of Storms - Dual Gate",
        sub_region="Castle of Storms",
        location_name="Castle of Storms - Dual Gate Lever",
        game_flag="stormdualgatef",
        game_sequences=["stormdualgate"],
        item_id_offset=4, loc_id_offset=4,
    ),
    LeverData(
        item_name="Crypt of Dead Gods - Tomb Entrance Gate",
        sub_region="Crypt of Dead Gods",
        location_name="Crypt of Dead Gods - Tomb Entrance Lever",
        game_flag="cavetombgate2",
        game_sequences=["cavetombgate2"],
        item_id_offset=5, loc_id_offset=5,
    ),
    LeverData(
        item_name="Crypt of Dead Gods - Hidden Wall",
        sub_region="Crypt of Dead Gods",
        location_name="Crypt of Dead Gods - Hidden Wall Lever",
        game_flag="cryptgodswall",
        game_sequences=["cryptgodswall"],
        item_id_offset=6, loc_id_offset=6,
    ),
    LeverData(
        item_name="Crypt of Dead Gods - Back Gate",
        sub_region="Crypt of Dead Gods",
        location_name="Crypt of Dead Gods - Back Gate Lever",
        game_flag="tombbackgate",
        game_sequences=["tombbackgate"],
        item_id_offset=7, loc_id_offset=7,
    ),
    LeverData(
        item_name="Dome of the Forgotten - Dome Elevator",
        sub_region="Dome of the Forgotten",
        location_name="Dome of the Forgotten - Dome Elevator",
        game_flag="dome_plat_f",
        game_sequences=["dome_plat"],
        item_id_offset=8, loc_id_offset=8,
    ),
    LeverData(
        item_name="Dome of the Forgotten - Dome Gate",
        sub_region="Dome of the Forgotten",
        location_name="Dome of the Forgotten - Dome Gate Lever",
        game_flag="domegates",
        game_sequences=["domegate"],
        item_id_offset=9, loc_id_offset=9,
    ),
    LeverData(
        item_name="Hager's Cavern - Blue Cave Entrance",
        sub_region="Hagers Cavern",
        location_name="Hager's Cavern - Blue Cave Entrance Lever",
        game_flag="bluecaveentrance",
        game_sequences=["bluecaveentrance"],
        item_id_offset=10, loc_id_offset=10,
    ),
    LeverData(
        item_name="Hager's Cavern - Boss Door",
        sub_region="Hagers Cavern",
        location_name="Hager's Cavern - Boss Door Lever",
        game_flag="cavebossdoor",
        game_sequences=["cavebossdoor"],
        item_id_offset=11, loc_id_offset=11,
    ),
    LeverData(
        item_name="Hager's Cavern - Spider Gate",
        sub_region="Hagers Cavern",
        location_name="Hager's Cavern - Spider Gate Lever",
        game_flag="cavespigate",
        game_sequences=["cavespigate"],
        item_id_offset=12, loc_id_offset=12,
    ),
    LeverData(
        item_name="Mal's Floating Castle - Sky Castle Gate",
        sub_region="Mals Floating Castle",
        location_name="Mal's Floating Castle - Sky Castle Gate Lever",
        game_flag="skycastlegate",
        game_sequences=["skycastlegate"],
        item_id_offset=13, loc_id_offset=13,
    ),
    LeverData(
        item_name="Mire of Stench - Swamp Shrine Gate",
        sub_region="Mire of Stench",
        location_name="Mire of Stench - Swamp Shrine Gate Lever",
        game_flag="caveswampshrine",
        game_sequences=["caveswampshrine"],
        item_id_offset=14, loc_id_offset=14,
    ),
    LeverData(
        item_name="Mire of Stench - Swamp Gate",
        sub_region="Mire of Stench",
        location_name="Mire of Stench - Swamp Gate Lever",
        game_flag="swampgate",
        game_sequences=["swampgate"],
        item_id_offset=15, loc_id_offset=15,
    ),
    LeverData(
        item_name="Mire of Stench - Swamp Gate 2",
        sub_region="Mire of Stench",
        location_name="Mire of Stench - Swamp Gate 2 Lever",
        game_flag="swampgate2",
        game_sequences=["swampgate2"],
        item_id_offset=16, loc_id_offset=16,
    ),
    LeverData(
        item_name="Pitchwoods - Pitchwoods Shortcut",
        sub_region="Pitchwoods",
        location_name="Pitchwoods - Shortcut Lever",
        game_flag="pitchwoodcut1",
        game_sequences=["pitchwoodcut"],
        item_id_offset=17, loc_id_offset=17,
    ),
    LeverData(
        item_name="Pitchwoods - Lake Shortcut",
        sub_region="Pitchwoods",
        location_name="Pitchwoods - Lake Shortcut Lever",
        game_flag="rpitchlakeshortcut2",
        game_sequences=["rpitchlakeshortcut"],
        item_id_offset=18, loc_id_offset=18,
    ),
    LeverData(
        item_name="Red Hall of Cages - Mine Shaft",
        sub_region="Red Hall of Cages",
        location_name="Red Hall of Cages - Mine Shaft Elevator",
        game_flag="cave_mine_shaft1",
        game_sequences=["cave_mine_shaft1"],
        item_id_offset=19, loc_id_offset=19,
    ),
    LeverData(
        item_name="Red Hall of Cages - Dungeon to Cave Gate",
        sub_region="Red Hall of Cages",
        location_name="Red Hall of Cages - Dungeon to Cave Lever",
        game_flag="dungeon2cave",
        game_sequences=["dungeon2cave"],
        item_id_offset=20, loc_id_offset=20,
    ),
    LeverData(
        item_name="Red Hall of Cages - Double Elevator",
        sub_region="Red Hall of Cages",
        location_name="Red Hall of Cages - Double Elevator",
        game_flag="dungeon_double_plat1",
        game_sequences=["dungeon_double_plat"],
        item_id_offset=21, loc_id_offset=21,
    ),
    LeverData(
        item_name="Red Hall of Cages - Mid Shortcut",
        sub_region="Red Hall of Cages",
        location_name="Red Hall of Cages - Mid Shortcut Elevator",
        game_flag="dungeonmidshrtf",
        game_sequences=["dungeonmidshrt"],
        item_id_offset=22, loc_id_offset=22,
    ),
    LeverData(
        item_name="Red Hall of Cages - Shortcut Door",
        sub_region="Red Hall of Cages",
        location_name="Red Hall of Cages - Shortcut Door Lever",
        game_flag="dungeonshrtdrf",
        game_sequences=["dungeonshrtdr"],
        item_id_offset=23, loc_id_offset=23,
    ),
    LeverData(
        item_name="Salt Alkymancery - Dungeon to Lab Gate",
        sub_region="Salt Alkymancery",
        location_name="Salt Alkymancery - Dungeon to Lab Lever",
        game_flag="dungeontolab",
        game_sequences=["dungeontolab"],
        item_id_offset=24, loc_id_offset=24,
    ),
    LeverData(
        item_name="Salt Alkymancery - Lab Tunnel Gate",
        sub_region="Salt Alkymancery",
        location_name="Salt Alkymancery - Lab Tunnel Gate Lever",
        game_flag="labtunnelgate",
        game_sequences=["labtunnelgate"],
        item_id_offset=25, loc_id_offset=25,
    ),
    LeverData(
        item_name="Salt Alkymancery - Lake to Ruins Gate",
        sub_region="Salt Alkymancery",
        location_name="Salt Alkymancery - Lake to Ruins Lever",
        game_flag="lakelabruins",
        game_sequences=["lakelabruins"],
        item_id_offset=26, loc_id_offset=26,
    ),
    LeverData(
        item_name="Siam Lake - Lake Shortcut",
        sub_region="Siam Lake",
        location_name="Siam Lake - Lake Shortcut Lever",
        game_flag="lpitchlakeshortcut1",
        game_sequences=["lpitchlakeshortcut"],
        item_id_offset=27, loc_id_offset=27,
    ),
    LeverData(
        item_name="Sunken Keep - Forest Shrine Gate",
        sub_region="Sunken Keep",
        location_name="Sunken Keep - Forest Shrine Gate Lever",
        game_flag="forestshrinegatef",
        game_sequences=["forestshrinegate"],
        item_id_offset=28, loc_id_offset=28,
    ),
    LeverData(
        item_name="Sunken Keep - Under Village Elevator",
        sub_region="Sunken Keep",
        location_name="Sunken Keep - Under Village Elevator",
        game_flag="under_village_boards_plat1",
        game_sequences=["under_village_boards_plat1"],
        item_id_offset=29, loc_id_offset=29,
    ),
    LeverData(
        item_name="The Festering Banquet - Fort Gate",
        sub_region="Festering Banquet pre Fortress Key",
        location_name="The Festering Banquet - Fort Gate Lever",
        game_flag="fortblackset1",
        game_sequences=["fortblackset"],
        item_id_offset=30, loc_id_offset=30,
    ),
    LeverData(
        item_name="The Ruined Temple - Dungeon to Ruins Gate",
        sub_region="Ruined Temple",
        location_name="The Ruined Temple - Dungeon to Ruins Lever",
        game_flag="dungeontoruins",
        game_sequences=["dungeontoruins"],
        item_id_offset=31, loc_id_offset=31,
    ),
    LeverData(
        item_name="The Ruined Temple - Block Floor",
        sub_region="Ruined Temple",
        location_name="The Ruined Temple - Block Floor Lever",
        game_flag="ruinblockfloor1",
        game_sequences=["ruinblockfloor"],
        item_id_offset=32, loc_id_offset=32,
    ),
    LeverData(
        item_name="The Ruined Temple - Twin Gate Left",
        sub_region="Ruined Temple",
        location_name="The Ruined Temple - Twin Gate Left Lever",
        game_flag="ruinstwinleft1",
        game_sequences=["ruinstwinleft"],
        item_id_offset=33, loc_id_offset=33,
    ),
    LeverData(
        item_name="The Ruined Temple - Twin Gate Right",
        sub_region="Ruined Temple",
        location_name="The Ruined Temple - Twin Gate Right Lever",
        game_flag="ruinstwinright1",
        game_sequences=["ruinstwinright"],
        item_id_offset=34, loc_id_offset=34,
    ),
    LeverData(
        item_name="Village of Smiles - Fort to Under Village Gate",
        sub_region="Village of Smiles",
        location_name="Village of Smiles - Fort to Under Village Lever",
        game_flag="forttoundervillagegate",
        game_sequences=["forttoundervillagegate"],
        item_id_offset=35, loc_id_offset=35,
    ),
    LeverData(
        item_name="Village of Smiles - Secret Under Village Gate",
        sub_region="Village of Smiles",
        location_name="Village of Smiles - Secret Under Village Lever",
        game_flag="secretundervillagegate1",
        game_sequences=["secretundervillagegate"],
        item_id_offset=36, loc_id_offset=36,
    ),
    LeverData(
        item_name="Village of Smiles - Tunnel to Forest Bottom",
        sub_region="Village of Smiles",
        location_name="Village of Smiles - Tunnel to Forest Bottom Lever",
        game_flag="tunneltoforestbottom1",
        game_sequences=["tunneltoforestbottom"],
        item_id_offset=37, loc_id_offset=37,
    ),
    LeverData(
        item_name="Village of Smiles - Tunnel to Forest Top",
        sub_region="Village of Smiles",
        location_name="Village of Smiles - Tunnel to Forest Top Lever",
        game_flag="tunneltoforesttop1",
        game_sequences=["tunneltoforesttop"],
        item_id_offset=38, loc_id_offset=38,
    ),
    LeverData(
        item_name="Ziggurat of Dust - Pyramid Elevator",
        sub_region="Ziggurat of Dust",
        location_name="Ziggurat of Dust - Pyramid Elevator",
        game_flag="pyramid_plat_sf",
        game_sequences=["pyramid_plat_sf"],
        item_id_offset=39, loc_id_offset=39,
    ),
    LeverData(
        item_name="Ziggurat of Dust - Pyramid Right Exit",
        sub_region="Ziggurat of Dust",
        location_name="Ziggurat of Dust - Pyramid Right Exit Lever",
        game_flag="pyramidrightout",
        game_sequences=["pyramidrightout"],
        item_id_offset=40, loc_id_offset=40,
    ),
    LeverData(
        item_name="Ziggurat of Dust - Ziggurat Gates",
        sub_region="Ziggurat of Dust",
        location_name="Ziggurat of Dust - Ziggurat Gates Lever",
        game_flag="zigguratgates",
        game_sequences=["zigguratgates"],
        item_id_offset=41, loc_id_offset=41,
    ),
    LeverData(
        item_name="Ziggurat of Dust - Ziggurat Upper Gate",
        sub_region="Ziggurat of Dust",
        location_name="Ziggurat of Dust - Ziggurat Upper Gate Lever",
        game_flag="zigguratupgate",
        game_sequences=[],
        item_id_offset=42, loc_id_offset=42,
    ),
    LeverData(
        item_name="Sunken Keep - Blade Bandit Gate",
        sub_region="Sunken Keep post Shadowflip",
        location_name="Sunken Keep - Blade Bandit Gate Lever",
        game_flag="bladebanditgate1",
        game_sequences=["bladebanditgate"],
        item_id_offset=43, loc_id_offset=43,
    ),
    LeverData(
        item_name="The Festering Banquet - Castle Gate",
        sub_region="Festering Banquet pre Fortress Key",
        location_name="The Festering Banquet - Castle Gate Lever",
        game_flag="fortresscastlegate1",
        game_sequences=["castlegate"],
        item_id_offset=44, loc_id_offset=44,
    ),
    LeverData(
        item_name="Ziggurat of Dust - Ziggurat Shortcut Gate",
        sub_region="Ziggurat of Dust",
        location_name="Ziggurat of Dust - Ziggurat Shortcut Gate Lever",
        game_flag="zigguratshortgate",
        game_sequences=["zigguratshortgate"],
        item_id_offset=45, loc_id_offset=45,
    ),
    LeverData(
        item_name="Hager's Cavern - Cave to Dungeon Gate",
        sub_region="Hagers Cavern",
        location_name="Hager's Cavern - Cave to Dungeon Lever",
        game_flag="cave2dungeonb",
        game_sequences=["cave2dungeonb"],
        item_id_offset=46, loc_id_offset=46,
    ),
    LeverData(
        item_name="Salt Alkymancery - Lab to Gold Gate",
        sub_region="Salt Alkymancery",
        location_name="Salt Alkymancery - Lab to Gold Lever",
        game_flag="labtogold1",
        game_sequences=["labtogold"],
        item_id_offset=47, loc_id_offset=47,
    ),
    LeverData(
        item_name="The Still Palace - Palace Escape",
        sub_region="The Still Palace",
        location_name="The Still Palace - Palace Escape Lever",
        game_flag="palaceescape1",
        game_sequences=["palaceescape"],
        item_id_offset=48, loc_id_offset=48,
    ),
    LeverData(
        item_name="Castle of Storms - Castle Exit",
        sub_region="Castle of Storms",
        location_name="Castle of Storms - Castle Exit Lever",
        game_flag="castleexit",
        game_sequences=["castleexit"],
        item_id_offset=49, loc_id_offset=49,
    ),
    LeverData(
        item_name="The Festering Banquet - Dungeon Gate",
        sub_region="Festering Banquet pre Fortress Key",
        location_name="The Festering Banquet - Dungeon Gate Lever",
        game_flag="castledungeongate",
        game_sequences=["castledungeongate"],
        item_id_offset=50, loc_id_offset=50,
    ),
]

# Completion event 
COMPLETION_EVENT = ("Victory - The Nameless God", "The Still Palace", "The Nameless God - Victory")


LEVER_ITEM_NAMES = {lever.item_name for lever in LEVERS}
LEVER_ITEM_NAMES.add(COMPLETION_EVENT[0])

LEVER_LOCATION_NAMES = {lever.location_name for lever in LEVERS}

# Item ID and Location ID mappings
LEVER_ITEM_IDS = {lever.item_name: LEVER_ITEM_BASE_ID + lever.item_id_offset for lever in LEVERS}
LEVER_LOC_IDS = {lever.location_name: LEVER_LOC_BASE_ID + lever.loc_id_offset for lever in LEVERS}

# Build lever data dict for slot_data (client reads this)
def get_lever_slot_data() -> dict:
    """Build lever data for slot_data so the client mod knows how to activate each lever.
    
    Returns dict mapping lever item AP ID -> {flag, sequences, location_id}
    Client mod uses this to:
      - Know which items are levers
      - Call PlayerMgr.SetMainPlayerFlag(flag)
      - Call MapMgr.FireSequence(sequences)
    """
    result = {}
    for lever in LEVERS:
        item_id = LEVER_ITEM_BASE_ID + lever.item_id_offset
        loc_id = LEVER_LOC_BASE_ID + lever.loc_id_offset
        result[item_id] = {
            "name": lever.item_name,
            "flag": lever.game_flag,
            "sequences": lever.game_sequences,
            "location_id": loc_id,
            "location_name": lever.location_name,
        }
    return result


# REGION CONNECTIONS
# Defines how sub-regions connect to each other.
# Format: (from_region, to_region)
# Rules are applied separately in set_region_rules()

CONNECTIONS = [
    # Start
    ("Menu", "Shivering Shore pre Sanctuary"),
    ("Shivering Shore pre Sanctuary", "Shivering Shore post Sanctuary"),
    ("Shivering Shore post Sanctuary", "Festering Banquet pre Fortress Key"),

    # Festering Banquet
    ("Festering Banquet pre Fortress Key", "Festering Banquet post Fortress Key"),
    ("Festering Banquet pre Fortress Key", "Festering Banquet post Vertigo West"),
    ("Festering Banquet post Fortress Key", "Festering Banquet post Vertigo East"),
    ("Festering Banquet post Fortress Key", "Bandits Pass"),
    ("Festering Banquet post Fortress Key", "Village of Smiles"),

    # Bandit's Pass
    ("Bandits Pass", "Bandits Pass post Bronze Key"),
    ("Bandits Pass", "Bandits Pass post Vertigo"),
    ("Bandits Pass", "Castle of Storms"),

    # Village of Smiles
    ("Village of Smiles", "Village of Smiles post Vertigo"),
    ("Village of Smiles", "Village of Smiles post Shadowflip"),
    ("Village of Smiles", "Watching Woods"),

    # Watching Woods
    ("Watching Woods", "Sunken Keep"),
    ("Watching Woods", "Watching Woods post Mad Alchemist"),

    # Sunken Keep
    ("Sunken Keep", "Sunken Keep post Kraeken Cyclops"),
    ("Sunken Keep post Kraeken Cyclops", "Sunken Keep post Vertigo pre Jester"),
    ("Sunken Keep post Kraeken Cyclops", "Sunken Keep post False Jester"),
    ("Sunken Keep post False Jester", "Sunken Keep post Vertigo East"),
    ("Sunken Keep post False Jester", "Sunken Keep post Vertigo West"),
    ("Sunken Keep post Vertigo West", "Festering Banquet post Fortress Key"),
    ("Sunken Keep post Vertigo West", "Sunken Keep post Shadowflip"),
    ("Sunken Keep post Shadowflip", "Festering Banquet post Fortress Key"),
    ("Sunken Keep post Vertigo East", "Bandits Pass"),

    # Castle of Storms
    ("Castle of Storms", "Castle of Storms post Kraeken Wyrm"),
    ("Castle of Storms post Kraeken Wyrm", "Castle of Storms post Shadowflip"),
    ("Castle of Storms", "Castle of Storms post Jagged Key"),
    ("Castle of Storms", "Castle of Storms post Hardlight"),
    ("Castle of Storms post Shadowflip", "Castle of Storms post Shadowflip and Hardlight"),
    ("Castle of Storms post Shadowflip", "Red Hall of Cages"),

    # Red Hall of Cages (hub area)
    ("Red Hall of Cages", "Hagers Cavern"),
    ("Red Hall of Cages", "Dome of the Forgotten"),
    ("Red Hall of Cages", "Mals Floating Castle"),
    ("Red Hall of Cages", "Crans Pass"),
    ("Red Hall of Cages", "Sunken Keep post Vertigo East"),

    # Hager's Cavern
    ("Hagers Cavern", "Hagers Cavern post Cellar Key"),
    ("Hagers Cavern post Cellar Key", "Hagers Cavern post Spiked Key"),
    ("Hagers Cavern post Spiked Key", "Mire of Stench"),
    ("Hagers Cavern post Mire of Stench", "Hagers Cavern"),
    ("Hagers Cavern", "Hagers Cavern post Brands"),
    ("Hagers Cavern", "Sunken Keep post Kraeken Cyclops"),

    # Mire of Stench
    ("Mire of Stench", "Hagers Cavern post Mire of Stench"),
    ("Mire of Stench", "Fort Beyond the Mire"),

    # Fort Beyond the Mire
    ("Fort Beyond the Mire", "The Far Beach"),
    ("Fort Beyond the Mire", "Fort Beyond the Mire post Hardlight"),

    # The Far Beach
    ("The Far Beach", "Ziggurat of Dust"),
    ("The Far Beach", "Pitchwoods Far Beach entrance"),

    # Dome of the Forgotten
    ("Dome of the Forgotten", "Dome of the Forgotten post Untouched Inquisitor"),
    ("Dome of the Forgotten post Untouched Inquisitor", "Dome of the Forgotten post Hardlight"),
    ("Dome of the Forgotten post Untouched Inquisitor", "Dome of the Forgotten post Third Lamb"),
    ("Dome of the Forgotten post Hardlight", "Mals Floating Castle"),
    ("Dome of the Forgotten post Hardlight", "Ziggurat of Dust"),

    # Ziggurat of Dust
    ("Ziggurat of Dust", "Ziggurat of Dust post Hardlight"),
    ("Ziggurat of Dust post Hardlight", "Ziggurat of Dust post Dried King"),
    ("Ziggurat of Dust", "Ziggurat of Dust post Redshift post Dart"),
    ("Ziggurat of Dust post Redshift post Dart", "Ruined Temple"),

    # Mal's Floating Castle
    ("Mals Floating Castle", "Mals Floating Castle post Murdiella Mal"),

    # Cran's Pass
    ("Crans Pass", "Crans Pass post Ronin Cran"),
    ("Crans Pass post Salt Alkymancery", "Crans Pass"),
    ("Crans Pass post Ronin Cran", "Ruined Temple"),

    # Ruined Temple
    ("Ruined Temple", "Siam Lake"),
    ("Ruined Temple", "Ruined Temple post The Coveted"),
    ("Ruined Temple post The Coveted", "Ruined Temple post Dart"),
    ("Ruined Temple", "Ruined Temple post Hardlight"),
    ("Ruined Temple", "Dome of the Forgotten"),
    ("Ruined Temple", "Pitchwoods"),

    # Siam Lake
    ("Siam Lake post Salt Alkymancery", "Crans Pass post Salt Alkymancery"),
    ("Siam Lake", "Salt Alkymancery"),
    ("Siam Lake", "Siam Lake post Salt Alkymancery"),
    ("Siam Lake", "The Blackest Vault"),

    # Pitchwoods
    ("Pitchwoods", "Pitchwoods post Carsejaw the Cruel"),
    ("Pitchwoods", "Pitchwoods post Dart"),
    ("Pitchwoods post Dart", "Pitchwoods Far Beach entrance"),
    ("Pitchwoods post Dart", "The Blackest Vault"),

    # The Blackest Vault
    ("The Blackest Vault", "The Blackest Vault post Bone Key"),
    ("The Blackest Vault post Bone Key", "Pitchwoods"),

    # Salt Alkymancery
    ("Salt Alkymancery", "Salt Alkymancery post Hardlight"),
    ("Salt Alkymancery", "Siam Lake post Salt Alkymancery"),
    ("Salt Alkymancery", "Salt Alkymancery post The Unskinned and The Architect"),
    ("Salt Alkymancery post The Unskinned and The Architect", "Crypt of Dead Gods"),
    ("Salt Alkymancery", "Red Hall of Cages"),

    # Crypt of Dead Gods
    ("Crypt of Dead Gods", "Hagers Cavern"),
    ("Crypt of Dead Gods", "The Still Palace"),

    # The Still Palace
    ("The Still Palace", "Salt Alkymancery"),
]

# ENTRANCE RULES
# Defines which items are required for each connection.

def set_region_rules(world: 'SaltSanctuaryWorld') -> None:
    """Apply all entrance rules to the world's region connections.
    
    Lever items are required to access each area. When multiple levers exist
    for an area, having ANY one of them is sufficient (each opens a different path).
    Lever rules are AND'd with existing brand/key requirements.
    """
    from worlds.generic.Rules import set_rule, add_rule

    player = world.player
    multiworld = world.multiworld

    def rule(entrance_name: str, *items: str):
        """Helper to set a rule requiring all listed items."""
        set_rule(
            multiworld.get_entrance(entrance_name, player),
            lambda state, reqs=items: all(state.has(r, player) for r in reqs)
        )

    def lever_rule(entrance_name: str, lever_items: list):
        """Add a lever requirement (any one of the listed levers) to an entrance.
        This is AND'd with any existing rules on that entrance."""
        add_rule(
            multiworld.get_entrance(entrance_name, player),
            lambda state, levers=lever_items: any(state.has(l, player) for l in levers)
        )

    # --- Festering Banquet ---
    rule("Festering Banquet pre Fortress Key -> Festering Banquet post Fortress Key",
         "Fortress Key")
    rule("Festering Banquet pre Fortress Key -> Festering Banquet post Vertigo West",
         "Vertigo Brand")
    rule("Festering Banquet post Fortress Key -> Festering Banquet post Vertigo East",
         "Vertigo Brand")

    # --- Bandit's Pass ---
    rule("Bandits Pass -> Bandits Pass post Bronze Key", "Bronze Key")
    rule("Bandits Pass -> Bandits Pass post Vertigo", "Vertigo Brand")
    rule("Bandits Pass -> Castle of Storms", "Vertigo Brand")

    # --- Village of Smiles ---
    rule("Village of Smiles -> Village of Smiles post Vertigo", "Vertigo Brand")
    rule("Village of Smiles -> Village of Smiles post Shadowflip", "Shadowflip Brand")

    # --- Sunken Keep ---
    rule("Sunken Keep post Kraeken Cyclops -> Sunken Keep post Vertigo pre Jester",
         "Vertigo Brand")
    rule("Sunken Keep post False Jester -> Sunken Keep post Vertigo East",
         "Vertigo Brand")
    rule("Sunken Keep post False Jester -> Sunken Keep post Vertigo West",
         "Vertigo Brand")
    rule("Sunken Keep post Vertigo West -> Festering Banquet post Fortress Key",
         "Vertigo Brand")
    rule("Sunken Keep post Vertigo West -> Sunken Keep post Shadowflip",
         "Shadowflip Brand")
    rule("Sunken Keep post Shadowflip -> Festering Banquet post Fortress Key",
         "Shadowflip Brand")

    # --- Castle of Storms ---
    rule("Castle of Storms post Kraeken Wyrm -> Castle of Storms post Shadowflip",
         "Shadowflip Brand")
    rule("Castle of Storms -> Castle of Storms post Jagged Key", "Jagged Key")
    rule("Castle of Storms -> Castle of Storms post Hardlight", "Hardlight Brand")
    rule("Castle of Storms post Shadowflip -> Castle of Storms post Shadowflip and Hardlight",
         "Hardlight Brand")

    # --- Red Hall of Cages ---
    rule("Red Hall of Cages -> Mals Floating Castle",
         "Hardlight Brand", "Vertigo Brand")

    # --- Hager's Cavern ---
    rule("Hagers Cavern -> Hagers Cavern post Cellar Key", "Cellar Key")
    rule("Hagers Cavern post Cellar Key -> Hagers Cavern post Spiked Key", "Spiked Key")
    rule("Hagers Cavern -> Sunken Keep post Kraeken Cyclops",
         "Shadowflip Brand")
    rule("Hagers Cavern -> Hagers Cavern post Brands",
         "Redshift Brand", "Hardlight Brand", "Shadowflip Brand")

    # --- Mire of Stench ---
    rule("Mire of Stench -> Fort Beyond the Mire", "Redshift Brand")

    # --- Fort Beyond the Mire ---
    rule("Fort Beyond the Mire -> Fort Beyond the Mire post Hardlight", "Hardlight Brand")

    # --- Ziggurat of Dust ---
    rule("Ziggurat of Dust -> Ziggurat of Dust post Hardlight", "Hardlight Brand")
    rule("Ziggurat of Dust -> Ziggurat of Dust post Redshift post Dart",
         "Redshift Brand", "Dart Brand")

    # --- Dome of the Forgotten ---
    rule("Dome of the Forgotten post Untouched Inquisitor -> Dome of the Forgotten post Hardlight",
         "Hardlight Brand")

    # --- Cran's Pass ---
    rule("Crans Pass -> Crans Pass post Ronin Cran", "Hardlight Brand", "Redshift Brand")

    # --- Ruined Temple ---
    rule("Ruined Temple -> Siam Lake", "Dart Brand", "Redshift Brand")
    rule("Ruined Temple -> Pitchwoods", "Dart Brand", "Redshift Brand")
    rule("Ruined Temple post The Coveted -> Ruined Temple post Dart",
         "Dart Brand", "Redshift Brand")
    rule("Ruined Temple -> Ruined Temple post Hardlight",
         "Hardlight Brand", "Redshift Brand")

    # --- Pitchwoods ---
    rule("Pitchwoods -> Pitchwoods post Carsejaw the Cruel", "Dart Brand")
    rule("Pitchwoods -> Pitchwoods post Dart", "Dart Brand")
    rule("Pitchwoods post Dart -> Pitchwoods Far Beach entrance", "Dart Brand")

    # --- The Blackest Vault ---
    rule("The Blackest Vault -> The Blackest Vault post Bone Key", "Bone Key")
    rule("The Blackest Vault post Bone Key -> Pitchwoods",
         "Vertigo Brand")

    # --- Salt Alkymancery ---
    rule("Salt Alkymancery -> Salt Alkymancery post Hardlight", "Hardlight Brand")
    rule("Salt Alkymancery post The Unskinned and The Architect -> Crypt of Dead Gods",
         "Shadowflip Brand")
    rule("Salt Alkymancery -> Red Hall of Cages",
         "Shadowflip Brand")

    # --- Crypt of Dead Gods ---
    rule("Crypt of Dead Gods -> Hagers Cavern",
         "Dart Brand")
    rule("Crypt of Dead Gods -> The Still Palace", "Dart Brand")

    # --- The Still Palace ---
    rule("The Still Palace -> Salt Alkymancery",
         "Dart Brand", "Shadowflip Brand")

    # LEVER GATE RULES
    # Each area's levers are required (any one) to enter that area.
    # These are AND'd with the brand/key rules above via add_rule.

    lever_rule("Festering Banquet post Fortress Key -> Bandits Pass",
         ["Bandit's Pass - Cave Door"])
    lever_rule("Sunken Keep post Vertigo East -> Bandits Pass",
         ["Bandit's Pass - Cave Door"])

    lever_rule("Bandits Pass -> Castle of Storms",
         ["Castle of Storms - Castle Bridge", "Castle of Storms - Ledge Elevator",
          "Castle of Storms - Middle Elevator", "Castle of Storms - Dual Gate"])

    lever_rule("Salt Alkymancery post The Unskinned and The Architect -> Crypt of Dead Gods",
         ["Crypt of Dead Gods - Tomb Entrance Gate", "Crypt of Dead Gods - Hidden Wall",
          "Crypt of Dead Gods - Back Gate"])

    lever_rule("Red Hall of Cages -> Dome of the Forgotten",
         ["Dome of the Forgotten - Dome Elevator", "Dome of the Forgotten - Dome Gate"])
    lever_rule("Ruined Temple -> Dome of the Forgotten",
         ["Dome of the Forgotten - Dome Elevator", "Dome of the Forgotten - Dome Gate"])

    lever_rule("Red Hall of Cages -> Hagers Cavern",
         ["Hager's Cavern - Blue Cave Entrance", "Hager's Cavern - Boss Door",
          "Hager's Cavern - Spider Gate"])
    lever_rule("Crypt of Dead Gods -> Hagers Cavern",
         ["Hager's Cavern - Blue Cave Entrance", "Hager's Cavern - Boss Door",
          "Hager's Cavern - Spider Gate"])

    lever_rule("Red Hall of Cages -> Mals Floating Castle",
         ["Mal's Floating Castle - Sky Castle Gate"])
    lever_rule("Dome of the Forgotten post Hardlight -> Mals Floating Castle",
         ["Mal's Floating Castle - Sky Castle Gate"])

    lever_rule("Hagers Cavern post Spiked Key -> Mire of Stench",
         ["Mire of Stench - Swamp Shrine Gate", "Mire of Stench - Swamp Gate",
          "Mire of Stench - Swamp Gate 2"])

    lever_rule("Ruined Temple -> Pitchwoods",
         ["Pitchwoods - Pitchwoods Shortcut", "Pitchwoods - Lake Shortcut"])
    lever_rule("The Blackest Vault post Bone Key -> Pitchwoods",
         ["Pitchwoods - Pitchwoods Shortcut", "Pitchwoods - Lake Shortcut"])

    lever_rule("Castle of Storms post Shadowflip -> Red Hall of Cages",
         ["Red Hall of Cages - Mine Shaft", "Red Hall of Cages - Dungeon to Cave Gate",
          "Red Hall of Cages - Double Elevator", "Red Hall of Cages - Mid Shortcut",
          "Red Hall of Cages - Shortcut Door"])
    lever_rule("Salt Alkymancery -> Red Hall of Cages",
         ["Red Hall of Cages - Mine Shaft", "Red Hall of Cages - Dungeon to Cave Gate",
          "Red Hall of Cages - Double Elevator", "Red Hall of Cages - Mid Shortcut",
          "Red Hall of Cages - Shortcut Door"])

    lever_rule("Ziggurat of Dust post Redshift post Dart -> Ruined Temple",
         ["The Ruined Temple - Dungeon to Ruins Gate", "The Ruined Temple - Block Floor",
          "The Ruined Temple - Twin Gate Left", "The Ruined Temple - Twin Gate Right"])
    lever_rule("Crans Pass post Ronin Cran -> Ruined Temple",
         ["The Ruined Temple - Dungeon to Ruins Gate", "The Ruined Temple - Block Floor",
          "The Ruined Temple - Twin Gate Left", "The Ruined Temple - Twin Gate Right"])

    lever_rule("Siam Lake -> Salt Alkymancery",
         ["Salt Alkymancery - Dungeon to Lab Gate", "Salt Alkymancery - Lab Tunnel Gate",
          "Salt Alkymancery - Lake to Ruins Gate"])
    lever_rule("The Still Palace -> Salt Alkymancery",
         ["Salt Alkymancery - Dungeon to Lab Gate", "Salt Alkymancery - Lab Tunnel Gate",
          "Salt Alkymancery - Lake to Ruins Gate"])

    lever_rule("Ruined Temple -> Siam Lake",
         ["Siam Lake - Lake Shortcut"])

    lever_rule("Watching Woods -> Sunken Keep",
         ["Sunken Keep - Forest Shrine Gate", "Sunken Keep - Under Village Elevator"])

    lever_rule("Festering Banquet post Fortress Key -> Village of Smiles",
         ["Village of Smiles - Fort to Under Village Gate",
          "Village of Smiles - Secret Under Village Gate",
          "Village of Smiles - Tunnel to Forest Bottom",
          "Village of Smiles - Tunnel to Forest Top"])

    lever_rule("The Far Beach -> Ziggurat of Dust",
         ["Ziggurat of Dust - Pyramid Elevator", "Ziggurat of Dust - Pyramid Right Exit",
          "Ziggurat of Dust - Ziggurat Gates", "Ziggurat of Dust - Ziggurat Upper Gate"])
    lever_rule("Dome of the Forgotten post Hardlight -> Ziggurat of Dust",
         ["Ziggurat of Dust - Pyramid Elevator", "Ziggurat of Dust - Pyramid Right Exit",
          "Ziggurat of Dust - Ziggurat Gates", "Ziggurat of Dust - Ziggurat Upper Gate"])

def create_regions(world: 'SaltSanctuaryWorld', skill_tree_randomized: bool = False,
                   excluded_pickup_flags: set = None) -> None:
    """Create all sub-regions, locations, connections, and event items.
    
    Args:
        excluded_pickup_flags: Set of pickup flags to skip (used when split_multi_items
            is enabled, so the base pickup is replaced by individual multi-item locations).
    """
    from .Locations import location_table, UNSPEAKABLE_DEEP_LOCATIONS

    player = world.player
    multiworld = world.multiworld
    include_unspeakable_deep = world.options.include_unspeakable_deep.value

    # Build location-to-subregion mapping ---
    subregion_locations: Dict[str, List[str]] = {name: [] for name in SUBREGION_NAMES}

    for loc_name, loc_data in location_table.items():
        # Skip Unspeakable Deep locations if disabled
        if loc_name in UNSPEAKABLE_DEEP_LOCATIONS and not include_unspeakable_deep:
            continue

        # Skip base pickup locations that are replaced by multi-item splits
        if excluded_pickup_flags and loc_data.flag in excluded_pickup_flags:
            continue

        subregion = get_subregion_for_location(loc_name, loc_data.region)
        if subregion in subregion_locations:
            subregion_locations[subregion].append(loc_name)
        else:
            # Fallback: if sub-region not found, put in the default
            default = _DEFAULT_SUBREGION.get(loc_data.region, loc_data.region)
            if default in subregion_locations:
                subregion_locations[default].append(loc_name)

    # Create all regions
    regions: Dict[str, Region] = {}

    for region_name in SUBREGION_NAMES:
        region = Region(region_name, player, multiworld)
        regions[region_name] = region
        multiworld.regions.append(region)

        # Add game locations to region
        for loc_name in subregion_locations.get(region_name, []):
            if loc_name in location_table:
                loc_data = location_table[loc_name]
                location = SaltSanctuaryLocation(player, loc_name, loc_data.code, region)
                region.locations.append(location)

    # Create lever locations
    for lever in LEVERS:
        if lever.sub_region in regions:
            region = regions[lever.sub_region]
        else:
            # Fallback to Menu if sub_region not found
            region = regions["Menu"]
        loc_id = LEVER_LOC_BASE_ID + lever.loc_id_offset
        lever_location = SaltSanctuaryLocation(player, lever.location_name, loc_id, region)
        region.locations.append(lever_location)

    # Create completion event 
    comp_item_name, comp_region, comp_loc_name = COMPLETION_EVENT
    if comp_region in regions:
        comp_location = SaltSanctuaryLocation(player, comp_loc_name, None, regions[comp_region])
        comp_item = SaltSanctuaryItem(comp_item_name, ItemClassification.progression, None, player)
        comp_location.place_locked_item(comp_item)
        regions[comp_region].locations.append(comp_location)

    # Create Skill Tree region if enabled
    if skill_tree_randomized:
        from .SkillTreeLocations import skilltree_locations

        skill_tree_region = Region("Skill Tree", player, multiworld)
        regions["Skill Tree"] = skill_tree_region
        multiworld.regions.append(skill_tree_region)

        for loc_name, loc_data in skilltree_locations.items():
            location = SaltSanctuaryLocation(player, loc_name, loc_data.code, skill_tree_region)
            skill_tree_region.locations.append(location)

        # Connect Skill Tree to Menu (always accessible)
        skill_entrance = Entrance(player, "Open Skill Tree", regions["Menu"])
        regions["Menu"].exits.append(skill_entrance)
        skill_entrance.connect(skill_tree_region)

    # Create all connections
    for from_name, to_name in CONNECTIONS:
        if from_name not in regions or to_name not in regions:
            continue
        entrance = Entrance(player, f"{from_name} -> {to_name}", regions[from_name])
        regions[from_name].exits.append(entrance)
        entrance.connect(regions[to_name])
