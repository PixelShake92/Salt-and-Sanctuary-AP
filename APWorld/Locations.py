from BaseClasses import Location
from typing import Dict, NamedTuple, Optional, Set

BOSS_BASE_ID = 283650000
BOSS_DROP_BASE_ID = 283650100
BRAND_LOC_BASE_ID = 283660500


class SaltSanctuaryLocation(Location):
    game = "Salt and Sanctuary"
PICKUP_BASE_ID = 283660000

# Locations tied to the Unspeakable Deep boss
# This boss can only be fought once per save file at the very start
# If the player dies or skips it, these locations become permanently inaccessible
UNSPEAKABLE_DEEP_LOCATIONS: Set[str] = {
    "The Unspeakable Deep",
    "The Unspeakable Deep - Drop",
}


class SaltSanctuaryLocationData(NamedTuple):
    code: int
    flag: str
    region: str


boss_locations: Dict[str, SaltSanctuaryLocationData] = {
    "The Sodden Knight": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 0,
        flag="dread",
        region="The Festering Banquet"
    ),
    "The Queen of Smiles": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 1,
        flag="cutqueen",
        region="Village of Smiles"
    ),
    "Kraekan Cyclops": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 2,
        flag="bull",
        region="The Watching Woods"
    ),
    "Kraekan Wyrm": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 3,
        flag="dragon",
        region="Castle of Storms"
    ),
    "The Mad Alchemist": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 4,
        flag="alchemist",
        region="The Watching Woods"
    ),
    "Tree of Men": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 5,
        flag="torturetree",
        region="Red Hall of Cages"
    ),
    "The Disemboweled Husk": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 6,
        flag="pirate",
        region="Hager's Cavern"
    ),
    "The Unspeakable Deep": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 7,
        flag="leviathon",
        region="Shivering Shore"
    ),
    "That Stench Most Foul": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 8,
        flag="gasbag",
        region="Mire of Stench"
    ),
    "Ronin Cran": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 9,
        flag="broken",
        region="Cran's Pass"
    ),
    "The Third Lamb": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 10,
        flag="griffin",
        region="Dome of the Forgotten"
    ),
    "The Witch of the Lake": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 11,
        flag="lakewitch",
        region="Siam Lake"
    ),
    "The False Jester": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 12,
        flag="fauxjester",
        region="Sunken Keep"
    ),
    "The Dried King": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 13,
        flag="mummy",
        region="Ziggurat of Dust"
    ),
    "The Bloodless Prince": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 14,
        flag="clay",
        region="Ziggurat of Dust"
    ),
    "The Untouched Inquisitor": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 15,
        flag="inquisitor",
        region="Dome of the Forgotten"
    ),
    "The Unskinned": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 16,
        flag="monster",
        region="Salt Alkymancery"
    ),
    "The Architect": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 17,
        flag="monsterwitch",
        region="Salt Alkymancery"
    ),
    "The Coveted": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 18,
        flag="ruinaxe",
        region="The Ruined Temple"
    ),
    "Kraekan Dragon Skourzh": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 21,
        flag="squiddragon",
        region="Crypt of Dead Gods"
    ),
    "The Nameless God": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 22,
        flag="nameless",
        region="The Still Palace"
    ),
    "Carsejaw the Cruel": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 23,
        flag="cloak",
        region="Pitchwoods"
    ),
    "The Forgotten King": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 24,
        flag="deadking",
        region="Crypt of Dead Gods"
    ),
    "The Forgotten Knight": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 25,
        flag="deadknight",
        region="Crypt of Dead Gods"
    ),
    "The Forgotten Judge": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 26,
        flag="deadjudge",
        region="Crypt of Dead Gods"
    ),
    "Murdiella Mal": SaltSanctuaryLocationData(
        code=BOSS_BASE_ID + 27,
        flag="murderfly",
        region="Mal's Floating Castle"
    ),
}

# Boss drop locations - items dropped directly by bosses
boss_drop_locations: Dict[str, SaltSanctuaryLocationData] = {
    "The Sodden Knight - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 0,
        flag="boss_drop_dread",
        region="The Festering Banquet"
    ),
    "The Queen of Smiles - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 1,
        flag="boss_drop_cutqueen",
        region="Village of Smiles"
    ),
    "Kraekan Cyclops - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 2,
        flag="boss_drop_bull",
        region="The Watching Woods"
    ),
    "Kraekan Wyrm - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 3,
        flag="boss_drop_dragon",
        region="Castle of Storms"
    ),
    "The Mad Alchemist - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 4,
        flag="boss_drop_alchemist",
        region="The Watching Woods"
    ),
    "The Tree of Men - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 5,
        flag="boss_drop_torturetree",
        region="Red Hall of Cages"
    ),
    "The Disemboweled Husk - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 6,
        flag="boss_drop_pirate",
        region="Hager's Cavern"
    ),
    "The Unspeakable Deep - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 7,
        flag="boss_drop_leviathon",
        region="Shivering Shore"
    ),
    "That Stench Most Foul - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 8,
        flag="boss_drop_gasbag",
        region="Mire of Stench"
    ),
    "The Unskinned - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 9,
        flag="boss_drop_monster",
        region="Salt Alkymancery"
    ),
    "The Third Lamb - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 10,
        flag="boss_drop_griffin",
        region="Dome of the Forgotten"
    ),
    "The Witch of the Lake - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 11,
        flag="boss_drop_lakewitch",
        region="Siam Lake"
    ),
    "The False Jester - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 12,
        flag="boss_drop_fauxjester",
        region="Sunken Keep"
    ),
    "The Dried King - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 13,
        flag="boss_drop_mummy",
        region="Ziggurat of Dust"
    ),
    "The Bloodless Prince - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 14,
        flag="boss_drop_clay",
        region="Ziggurat of Dust"
    ),
    "The Untouched Inquisitor - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 15,
        flag="boss_drop_inquisitor",
        region="Dome of the Forgotten"
    ),
    "The Architect - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 16,
        flag="boss_drop_monsterwitch",
        region="Salt Alkymancery"
    ),
    "The Coveted - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 17,
        flag="boss_drop_ruinaxe",
        region="The Ruined Temple"
    ),
    "Kraekan Dragon Skourzh - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 18,
        flag="boss_drop_squiddragon",
        region="Crypt of Dead Gods"
    ),
    "The Nameless God - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 19,
        flag="boss_drop_nameless",
        region="The Still Palace"
    ),
    "Carsejaw the Cruel - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 20,
        flag="boss_drop_cloak",
        region="Pitchwoods"
    ),
    "The Forgotten King - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 21,
        flag="boss_drop_deadking",
        region="Crypt of Dead Gods"
    ),
    "The Forgotten Knight - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 22,
        flag="boss_drop_deadknight",
        region="Crypt of Dead Gods"
    ),
    "The Forgotten Judge - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 23,
        flag="boss_drop_deadjudge",
        region="Crypt of Dead Gods"
    ),
    "Murdiella Mal - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 24,
        flag="boss_drop_murderfly",
        region="Mal's Floating Castle"
    ),
    "Ronin Cran - Drop": SaltSanctuaryLocationData(
        code=BOSS_DROP_BASE_ID + 25,
        flag="boss_drop_broken",
        region="Cran's Pass"
    ),
}


pickup_locations: Dict[str, SaltSanctuaryLocationData] = {
    "The Festering Banquet - Pouch of Salt (8275)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 0,
        flag="sanc1salt",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Red Shard x3 (13829)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 1,
        flag="fortress_shield",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Self Bow": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 2,
        flag="fortress_bow",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Bundle of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 3,
        flag="fortresssalt2",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Throwing Dagger x25": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 4,
        flag="fortress_throw_dagger",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Stone Blacksmith": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 5,
        flag="fortress_lit_ball",
        region="The Festering Banquet"
    ),
    "Shivering Shore - Sanctuary Key": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 6,
        flag="key_sanc_5650",
        region="Shivering Shore"
    ),
    "Village of Smiles - Conduit of Mind": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 7,
        flag="village_knight_ring_mp",
        region="Village of Smiles"
    ),
    "Village of Smiles - Faithful Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 8,
        flag="village_knight2",
        region="Village of Smiles"
    ),
    "Village of Smiles - Bell of Return x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 9,
        flag="village_knight1",
        region="Village of Smiles"
    ),
    "Village of Smiles - Blessed Page x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 10,
        flag="village_buff_holy",
        region="Village of Smiles"
    ),
    "Village of Smiles - Bundle of Salt (10499)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 11,
        flag="village_salt2",
        region="Village of Smiles"
    ),
    "The Festering Banquet - Red Shard x3 (12986)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 12,
        flag="fortress_lit_bolt",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Grenado x5": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 13,
        flag="village_grenado",
        region="The Festering Banquet"
    ),
    "The Festering Banquet - Stone Cleric (4238)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 14,
        flag="village_statue_cleric",
        region="The Festering Banquet"
    ),
    "The Watching Woods - Whip": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 15,
        flag="forest_whip_18742",
        region="The Watching Woods"
    ),
    "The Watching Woods - Bag of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 16,
        flag="forest_amber_spark",
        region="The Watching Woods"
    ),
    "The Watching Woods - Stone Mage": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 17,
        flag="forest_redhigh_mage",
        region="The Watching Woods"
    ),
    "Bandit's Pass - Onyx Burgeonet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 18,
        flag="hidden_black_set",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Spirited Mend": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 19,
        flag="hidden_tree_heal2",
        region="Bandit's Pass"
    ),
    "The Festering Banquet - Stone Mage": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 20,
        flag="fortress_mage_16430",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Flanged Mace and Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 21,
        flag="stone_ledge_salt",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Storm Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 22,
        flag="hidden_sanctuary_mag_boost",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Flanged Mace": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 23,
        flag="hidden_sancledge_spark",
        region="Bandit's Pass"
    ),
    "Castle of Storms - Gray Pearl (32164)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 24,
        flag="castle_terror_ledge",
        region="Castle of Storms"
    ),
    "Village of Smiles - Haymaker": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 25,
        flag="under_village_scythe",
        region="Village of Smiles"
    ),
    "Village of Smiles - Warhorn": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 26,
        flag="under_village_salt",
        region="Village of Smiles"
    ),
    "Sunken Keep - Stone Blacksmith and Poem": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 27,
        flag="greenvillage_blacksmith",
        region="Sunken Keep"
    ),
    "The Festering Banquet - Jurney Bottle": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 28,
        flag="fortress_jurney_ld",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Bronze Key": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 29,
        flag="trap_cave_key_bronze",
        region="Bandit's Pass"
    ),
    "The Festering Banquet - Rogue's Mask": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 30,
        flag="village_thief_armor",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Cotton Tunic": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 31,
        flag="hidden_tunic_set",
        region="Bandit's Pass"
    ),
    "Castle of Storms - Lightning Ball": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 32,
        flag="castle_real_lit_ball",
        region="Castle of Storms"
    ),
    "Bandit's Pass - Chain Gauntlets": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 33,
        flag="midsecretchainmail_gloves",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Chain Coif": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 34,
        flag="midsecretchainmail_helm",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Chain Hauberk": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 35,
        flag="midsecretchainmail_armor",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Chain Chausses": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 36,
        flag="midsecretchainmail_boots",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Raider's Harness": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 37,
        flag="stone_ledge_tribe_armor",
        region="Bandit's Pass"
    ),
    "Castle of Storms - Stone Blacksmith": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 38,
        flag="castle_real_stat_black",
        region="Castle of Storms"
    ),
    "Sunken Keep - Voracious Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 39,
        flag="midsecretcharm_hp_leech",
        region="Sunken Keep"
    ),
    "Castle of Storms - Jagged Key": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 40,
        flag="castle_dragon_key",
        region="Castle of Storms"
    ),
    "The Watching Woods - Mossy Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 41,
        flag="forest_charm_speed",
        region="The Watching Woods"
    ),
    "The Watching Woods - Brightcoral Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 42,
        flag="forest_ring_stam",
        region="The Watching Woods"
    ),
    "The Watching Woods - Mossy Key": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 43,
        flag="forest_alchemist_key",
        region="The Watching Woods"
    ),
    "The Festering Banquet - Bandaged Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 44,
        flag="fortress_ring_vit",
        region="The Festering Banquet"
    ),
    "Sunken Keep - Plated Band": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 45,
        flag="greenvillage_ring_str",
        region="Sunken Keep"
    ),
    "Castle of Storms - Impen's Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 46,
        flag="castle_charm_fire",
        region="Castle of Storms"
    ),
    "Village of Smiles - Bloodflower Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 47,
        flag="village_charm_atk",
        region="Village of Smiles"
    ),
    "Sunken Keep - Link of Fire and Sky": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 48,
        flag="greenvillage_ring_magb",
        region="Sunken Keep"
    ),
    "Red Hall of Cages - Stone Merchant": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 49,
        flag="dungeon_health_shard",
        region="Red Hall of Cages"
    ),
    "The Ruined Temple - Shroud Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 50,
        flag="dungeon_holy_def",
        region="The Ruined Temple"
    ),
    "Hager's Cavern - Saper Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 51,
        flag="dungeon_charm_mp_leech",
        region="Hager's Cavern"
    ),
    "Red Hall of Cages - Bag of Salt (43324)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 52,
        flag="dungeon_salt3statue_blacksmith",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Endless Fang": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 53,
        flag="dungeon_beast_spark",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Tachi": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 54,
        flag="dungeon_sword_40349",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Lightning Storm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 55,
        flag="dungeon_lit_storm",
        region="Red Hall of Cages"
    ),
    "Castle of Storms - Stone Merchant": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 56,
        flag="castle_statue_merchant",
        region="Castle of Storms"
    ),
    "Red Hall of Cages - Vile Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 57,
        flag="dungeon_charm_poison",
        region="Red Hall of Cages"
    ),
    "Castle of Storms - Scrimshaw Cane": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 58,
        flag="castle_ivory_43710",
        region="Castle of Storms"
    ),
    "Castle of Storms - Grasping Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 59,
        flag="castle_ring_salt",
        region="Castle of Storms"
    ),
    "Red Hall of Cages - Red Shard x5": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 60,
        flag="dungeon_health_statue_mage",
        region="Red Hall of Cages"
    ),
    "Bandit's Pass - Jester's Slippers": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 61,
        flag="hidden_passage_jester_boots",
        region="Bandit's Pass"
    ),
    "The Watching Woods - Bundle of Salt (12542)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 62,
        flag="hidden_passage_salt_12542",
        region="The Watching Woods"
    ),
    "Red Hall of Cages - Stone Cleric": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 63,
        flag="dungeon_health_statue_cleric",
        region="Red Hall of Cages"
    ),
    "Village of Smiles - Fused Metal Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 64,
        flag="village_trees_ring_vit",
        region="Village of Smiles"
    ),
    "Hager's Cavern - Statue Mage5": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 65,
        flag="bluecave_statue_mage",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Goldenstone Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 66,
        flag="bluecave_charm_lit",
        region="Hager's Cavern"
    ),
    "Castle of Storms - Hunter's Tricorne": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 67,
        flag="village_hunter_armor",
        region="Castle of Storms"
    ),
    "Red Hall of Cages - Steel Armet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 68,
        flag="dungeon_knight_armor",
        region="Red Hall of Cages"
    ),
    "Hager's Cavern - Palatine Coif": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 69,
        flag="cave_paladin_armor",
        region="Hager's Cavern"
    ),
    "The Festering Banquet - Soldier's Spear": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 70,
        flag="fortress_spear",
        region="The Festering Banquet"
    ),
    "Sunken Keep - Brightcoral Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 71,
        flag="hidden_cave_ring_itemfind",
        region="Sunken Keep"
    ),
    "Village of Smiles - Wrapped Link": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 72,
        flag="village_ring_roll",
        region="Village of Smiles"
    ),
    "Sunken Keep - Forestfang x25": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 73,
        flag="knight_13992",
        region="Sunken Keep"
    ),
    "Sunken Keep - Askarian Scutum": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 74,
        flag="midsecret_shield_oval",
        region="Sunken Keep"
    ),
    "Red Hall of Cages - Sack of Salt (50301)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 75,
        flag="dungeon_salt_50208",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Bag of Salt (37279)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 76,
        flag="dungeon_37107",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Bag of Salt (38275)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 77,
        flag="dungeon_38275",
        region="Red Hall of Cages"
    ),
    "Village of Smiles - Lightning Arc": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 78,
        flag="village_trees_flame_storm",
        region="Village of Smiles"
    ),
    "Red Hall of Cages - Sack of Salt (47480)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 79,
        flag="dungeon_salt_47480",
        region="Red Hall of Cages"
    ),
    "Bandit's Pass - Pouch of Salt (17519)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 80,
        flag="hidden_salt_axe_16822",
        region="Bandit's Pass"
    ),
    "The Festering Banquet - Kismet Stone": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 81,
        flag="fortresssalt1_11670",
        region="The Festering Banquet"
    ),
    "Red Hall of Cages - Stone Guide (40293)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 82,
        flag="statue_guide_40293",
        region="Red Hall of Cages"
    ),
    "Hager's Cavern - Charred Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 83,
        flag="bluecave_red_spark_33749",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Endless Fang x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 84,
        flag="bluecave_beast_spark_31775",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - A Soldier's Poem": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 85,
        flag="bluecave_white_flame_33948",
        region="Hager's Cavern"
    ),
    "Village of Smiles - Lock of Hair x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 86,
        flag="village_white_spark_8031",
        region="Village of Smiles"
    ),
    "Red Hall of Cages - Flame Orbiters": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 87,
        flag="dungeon_fire_oribts",
        region="Red Hall of Cages"
    ),
    "Mire of Stench - Frozen Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 88,
        flag="swamp_blue_spark_23759",
        region="Mire of Stench"
    ),
    "Mire of Stench - Satchel of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 89,
        flag="swamp_salt5_23795",
        region="Mire of Stench"
    ),
    "Mire of Stench - Vile Vines Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 90,
        flag="swamp_poison_def_26836",
        region="Mire of Stench"
    ),
    "Mire of Stench - Cleric's Kite Shield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 91,
        flag="swamp_shield_cleric_26163",
        region="Mire of Stench"
    ),
    "Mire of Stench - Priest's Zucchetto": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 92,
        flag="swamp_cleric_set_16647",
        region="Mire of Stench"
    ),
    "Hager's Cavern - Boeotian Greatshield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 93,
        flag="bluecave_shield_antler_30391",
        region="Hager's Cavern"
    ),
    "Red Hall of Cages - Waterpot x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 94,
        flag="dungeon_waterpot_43939",
        region="Red Hall of Cages"
    ),
    "Hager's Cavern - Trickster's Band": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 95,
        flag="bluecave_statue_cleric_31349",
        region="Hager's Cavern"
    ),
    "Mire of Stench - Kaltic Razor": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 96,
        flag="swamp_dagger_shiv_20204",
        region="Mire of Stench"
    ),
    "Hager's Cavern - Rowan Crosier": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 97,
        flag="bluecave_staff_wood_28709",
        region="Hager's Cavern"
    ),
    "Village of Smiles - Claymore": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 98,
        flag="village_trees_claymore",
        region="Village of Smiles"
    ),
    "Sunken Keep - Leather Sallet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 99,
        flag="greenvillage_leather_set",
        region="Sunken Keep"
    ),
    "Sunken Keep - Return Bellp": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 100,
        flag="greenvillage_bell_31063",
        region="Sunken Keep"
    ),
    "Dome of the Forgotten - Bag of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 101,
        flag="dome_staff_60325",
        region="Dome of the Forgotten"
    ),
    "The Ruined Temple - A Soldier's Poem x3 (62759)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 102,
        flag="ruins_whiteflame_62759",
        region="The Ruined Temple"
    ),
    "The Ruined Temple - Sorcerer's Kurta": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 103,
        flag="ruins_armor_sorceror",
        region="The Ruined Temple"
    ),
    "Dome of the Forgotten - Scorpion Migfer": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 104,
        flag="dome_fat_set",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Patched Hood": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 105,
        flag="dome_patched_set",
        region="Dome of the Forgotten"
    ),
    "Bandit's Pass - Pouch of Salt (21019)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 106,
        flag="hidden_sanctuary_spear_pitchfork",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Outlaw Greataxe": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 107,
        flag="hidden_sanctuary_axe_great",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Flame Arrow x25": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 108,
        flag="hidden_sanctuary_31591",
        region="Bandit's Pass"
    ),
    "Sunken Keep - Pack of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 109,
        flag="greenvillage_salt6_32253",
        region="Sunken Keep"
    ),
    "Sunken Keep - Warhammer": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 110,
        flag="greenvillage_hammer_great",
        region="Sunken Keep"
    ),
    "Bandit's Pass - Shockstone x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 111,
        flag="pcastle_34312",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Bell of Return": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 112,
        flag="hidden_sancledge_22763",
        region="Bandit's Pass"
    ),
    "The Festering Banquet - Bell of Return": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 113,
        flag="fortress_bell_16140",
        region="The Festering Banquet"
    ),
    "Sunken Keep - Bell of Return": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 114,
        flag="greenvillage_bell_29341",
        region="Sunken Keep"
    ),
    "Village of Smiles - Bell of Return": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 115,
        flag="village_bell_9554",
        region="Village of Smiles"
    ),
    "Hager's Cavern - Cellar Key": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 116,
        flag="bluecave_key_cave_37705",
        region="Hager's Cavern"
    ),
    "The Festering Banquet - Black Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 117,
        flag="fortress_black_pearl",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Black Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 118,
        flag="hidden_black_pearl",
        region="Bandit's Pass"
    ),
    "The Watching Woods - Black Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 119,
        flag="forest_black_pearl",
        region="The Watching Woods"
    ),
    "Village of Smiles - Black Pearl4": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 120,
        flag="village_black_pearl",
        region="Village of Smiles"
    ),
    "Bandit's Pass - Heater Shield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 121,
        flag="hidden_passage_14332",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Lightning Arc": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 122,
        flag="hidden_passage_6058",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Ragged Hanten": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 123,
        flag="hidden_passage_7771",
        region="Bandit's Pass"
    ),
    "Mire of Stench - Bell of Return x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 124,
        flag="swamp_return_23587",
        region="Mire of Stench"
    ),
    "Mire of Stench - Corsair's Vest": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 125,
        flag="swamp_pirate_24248",
        region="Mire of Stench"
    ),
    "The Festering Banquet - Torch Oil (16916)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 126,
        flag="fortress_lit_15226",
        region="The Festering Banquet"
    ),
    "Sunken Keep - Lamprey Barbut": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 127,
        flag="hidden_blades_23019",
        region="Sunken Keep"
    ),
    "Sunken Keep - Lamprey Cuirass": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 128,
        flag="hidden_blades_24405",
        region="Sunken Keep"
    ),
    "Castle of Storms - Titan Armet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 129,
        flag="castle_golem_set_34559",
        region="Castle of Storms"
    ),
    "Fort-Beyond-the-Mire - Stardust Spire": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 130,
        flag="ruin_room_spear_14388",
        region="Fort-Beyond-the-Mire"
    ),
    "Fort-Beyond-the-Mire - Defender's Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 131,
        flag="ruin_ring_def_5939",
        region="Fort-Beyond-the-Mire"
    ),
    "Fort-Beyond-the-Mire - Pack of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 132,
        flag="ruin_salt_4420",
        region="Fort-Beyond-the-Mire"
    ),
    "Fort-Beyond-the-Mire - Bell of Return": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 133,
        flag="ruin_bell_4084",
        region="Fort-Beyond-the-Mire"
    ),
    "The Festering Banquet - Torch Oil (16187)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 134,
        flag="fortress_torch_16220",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Stone Merchant": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 135,
        flag="midsecret_25589",
        region="Bandit's Pass"
    ),
    "Red Hall of Cages - Fire2": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 136,
        flag="dungeon_fire2_33509",
        region="Red Hall of Cages"
    ),
    "The Festering Banquet - Heal": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 137,
        flag="fortress_heal_16902",
        region="The Festering Banquet"
    ),
    "Sunken Keep - Blessed Weapon": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 138,
        flag="greenvillage_holy_buff",
        region="Sunken Keep"
    ),
    "Hager's Cavern - Divine Blessed Weapon": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 139,
        flag="bluecave_holy_buff2",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Flame Guardian": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 140,
        flag="bluecave_fire_turret",
        region="Hager's Cavern"
    ),
    "Castle of Storms - Lightning Barrage": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 141,
        flag="castle_rapid_lit_34782",
        region="Castle of Storms"
    ),
    "Castle of Storms - Split Mask": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 142,
        flag="castle_split_helm",
        region="Castle of Storms"
    ),
    "Castle of Storms - Ray of Searing": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 143,
        flag="castle_holy_cone",
        region="Castle of Storms"
    ),
    "Ziggurat of Dust - Flame Barrage": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 144,
        flag="mag_rapid_fire_77867",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Charm Poiseh": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 145,
        flag="charm_poise_80996",
        region="Ziggurat of Dust"
    ),
    "Dome of the Forgotten - Flintlock Pistol": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 146,
        flag="dome_gun_flintlock_60325",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Buff Fire x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 147,
        flag="dome_buff_fire_59086",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Merchant's Fez": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 148,
        flag="dome_merchant_61077",
        region="Dome of the Forgotten"
    ),
    "The Festering Banquet - Stone Guide (11404)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 149,
        flag="fortressstatue_guide_11407",
        region="The Festering Banquet"
    ),
    "Bandit's Pass - Stone Alchemist": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 150,
        flag="midsecretstatue_alchemist",
        region="Bandit's Pass"
    ),
    "The Ruined Temple - Guide's Cap": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 151,
        flag="ruins_guide_armor_59910",
        region="The Ruined Temple"
    ),
    "The Ruined Temple - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 152,
        flag="ruins_statue_guide_61709",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Stone Guide (82894)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 153,
        flag="statue_guide_82894",
        region="Ziggurat of Dust"
    ),
    "Dome of the Forgotten - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 154,
        flag="statue_guide_62636",
        region="Dome of the Forgotten"
    ),
    "Castle of Storms - Stone Guide (35484)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 155,
        flag="statue_guide_35484",
        region="Castle of Storms"
    ),
    "Bandit's Pass - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 156,
        flag="statue_guide_27244",
        region="Bandit's Pass"
    ),
    "Village of Smiles - Stone Guide (667)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 157,
        flag="statue_guide_667",
        region="Village of Smiles"
    ),
    "Mire of Stench - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 158,
        flag="statue_guide_25428",
        region="Mire of Stench"
    ),
    "Hager's Cavern - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 159,
        flag="statue_guide_38964",
        region="Hager's Cavern"
    ),
    "Dome of the Forgotten - Stone Alchemist": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 160,
        flag="statue_alchemist_59047",
        region="Dome of the Forgotten"
    ),
    "Hager's Cavern - Stone Mage": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 161,
        flag="bluecave_statue_mage_34244",
        region="Hager's Cavern"
    ),
    "The Ruined Temple - Stone Cleric": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 162,
        flag="ruins_statue_cleric_65062",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Statue Blacksmithd": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 163,
        flag="statue_statue_blacksmith_76993",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Stone Cleric (86774)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 164,
        flag="statue_cleric_86774",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Martial Flail": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 165,
        flag="whip_chain_87089",
        region="Ziggurat of Dust"
    ),
    "Red Hall of Cages - Stone Alchemist": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 166,
        flag="dungeon_statue_alchemist_48137",
        region="Red Hall of Cages"
    ),
    "Bandit's Pass - Stone Leader": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 167,
        flag="midsecretcharm_statue_leader",
        region="Bandit's Pass"
    ),
    "Village of Smiles - Stone Leader": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 168,
        flag="village_statue_leader",
        region="Village of Smiles"
    ),
    "Mire of Stench - Stone Leader": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 169,
        flag="statue_leader_25068",
        region="Mire of Stench"
    ),
    "Mire of Stench - Alchemist's Mask": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 170,
        flag="alchemist_set_25603",
        region="Mire of Stench"
    ),
    "Sunken Keep - Holy Light": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 171,
        flag="greenvillage_light_26929",
        region="Sunken Keep"
    ),
    "Bandit's Pass - Stone Sellsword": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 172,
        flag="hidden_statue_sellsword_23996",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Silver Shield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 173,
        flag="midsecretshield_round",
        region="Bandit's Pass"
    ),
    "Castle of Storms - Phoenix Rondache": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 174,
        flag="castle_shield_silver",
        region="Castle of Storms"
    ),
    "Castle of Storms - Mending Band": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 175,
        flag="castle_real_ring_hp",
        region="Castle of Storms"
    ),
    "Dome of the Forgotten - Charged Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 176,
        flag="dome_ring_magic_61610",
        region="Dome of the Forgotten"
    ),
    "Red Hall of Cages - Relentless Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 177,
        flag="dungeon_ring_spirit_44551",
        region="Red Hall of Cages"
    ),
    "Mire of Stench - Mossy Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 178,
        flag="swamp_ring_stamina_18459",
        region="Mire of Stench"
    ),
    "Dome of the Forgotten - Symbol of Affluence": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 179,
        flag="ring_gold_40263",
        region="Dome of the Forgotten"
    ),
    "Red Hall of Cages - Type 46 Tower Shield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 180,
        flag="dungeon_shield_tower",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - Charred Doll x3 (38317)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 181,
        flag="red_spark_38317",
        region="Red Hall of Cages"
    ),
    "The Ruined Temple - Sprites": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 182,
        flag="ruins_holy_orbits_71482",
        region="The Ruined Temple"
    ),
    "The Ruined Temple - Breach Pike": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 183,
        flag="ruins_spear_pilum",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Statue Maged": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 184,
        flag="pyramid_statue_mage",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Ring Cheap Magd": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 185,
        flag="pyramid_ring_cheap_mag",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Stone Cleric": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 186,
        flag="pyramid_statue_cleric",
        region="Ziggurat of Dust"
    ),
    "Village of Smiles - Vinemesh Peltarion": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 187,
        flag="village_shield_branches",
        region="Village of Smiles"
    ),
    "The Ruined Temple - Bloodflower Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 188,
        flag="ruins_ring_damage",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Plate Mail": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 189,
        flag="stag_armor_84279",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Charred Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 190,
        flag="red_spark_82798",
        region="Ziggurat of Dust"
    ),
    "Salt Alkymancery - Frozen Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 191,
        flag="lab_blue_spark_51496",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Aster Monolith": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 192,
        flag="lab_axe_blue_50052",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 193,
        flag="lab_statue_guide_51459",
        region="Salt Alkymancery"
    ),
    "Red Hall of Cages - Pruina Scutum": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 194,
        flag="48065",
        region="Red Hall of Cages"
    ),
    "The Watching Woods - Shield Buckler": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 195,
        flag="forest_buckler_19508",
        region="The Watching Woods"
    ),
    "Castle of Storms - Assassin's Cowl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 196,
        flag="castle_ninja_38321",
        region="Castle of Storms"
    ),
    "Siam Lake - Stone Guide": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 197,
        flag="lake_statue_guide_67994",
        region="Siam Lake"
    ),
    "Salt Alkymancery - Ring of Meditation": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 198,
        flag="lake_ring_cheap_wis_65846",
        region="Salt Alkymancery"
    ),
    "The Watching Woods - Battle Axe": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 199,
        flag="forest_axe_18935",
        region="The Watching Woods"
    ),
    "Mire of Stench - Redhair Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 200,
        flag="swamp_cdo_26825",
        region="Mire of Stench"
    ),
    "The Ruined Temple - Divine Will": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 201,
        flag="ruin_holy_will_14878",
        region="The Ruined Temple"
    ),
    "Red Hall of Cages - Teuthis Shield": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 202,
        flag="dungeon_shield_iron_45075",
        region="Red Hall of Cages"
    ),
    "The Ruined Temple - Drowned Idol x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 203,
        flag="ruins_spark_63361",
        region="The Ruined Temple"
    ),
    "Fort-Beyond-the-Mire - Boatman's Mino": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 204,
        flag="fort_boat_5646",
        region="Fort-Beyond-the-Mire"
    ),
    "Salt Alkymancery - Frozen Locket": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 205,
        flag="lab_statue_flame_50824",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Frozen Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 206,
        flag="lab_statue_flame_53398",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Tainted Cuirass": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 207,
        flag="lab_saltknight_47048",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Tainted Ranseur": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 208,
        flag="lab_saltknight_50361",
        region="Salt Alkymancery"
    ),
    "The Watching Woods - Pouch of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 209,
        flag="forest_salt_13409",
        region="The Watching Woods"
    ),
    "Mal's Floating Castle - Stone Guide (52176)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 210,
        flag="vert_guide_52176",
        region="Mal's Floating Castle"
    ),
    "Crypt of Dead Gods - Case of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 211,
        flag="tomb_salt_42096",
        region="Crypt of Dead Gods"
    ),
    "Salt Alkymancery - Static Geist": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 212,
        flag="dungeon_lit_ghost",
        region="Salt Alkymancery"
    ),
    "Hager's Cavern - Ring of Brilliance": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 213,
        flag="lake_ring_light_58739",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Drowned Idol x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 214,
        flag="bluecave_spark_35480",
        region="Hager's Cavern"
    ),
    "Ziggurat of Dust - Bag of Earth": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 215,
        flag="earth_bag_85048",
        region="Ziggurat of Dust"
    ),
    "The Watching Woods - Pale Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 216,
        flag="hidden_passage_charm_reach",
        region="The Watching Woods"
    ),
    "Salt Alkymancery - Dancing Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 217,
        flag="lab_ring_slash_42721",
        region="Salt Alkymancery"
    ),
    "The Ruined Temple - Templar's Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 218,
        flag="ruins_charm_holy_65973",
        region="The Ruined Temple"
    ),
    "The Ruined Temple - War Scythe": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 219,
        flag="dome_war_scythe_61610",
        region="The Ruined Temple"
    ),
    "The Festering Banquet - Cavalier's Armet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 220,
        flag="fortress_dreadset_14620",
        region="The Festering Banquet"
    ),
    "The Ruined Temple - Bloodbrow Cuirass": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 221,
        flag="chest_devil_67709",
        region="The Ruined Temple"
    ),
    "Pitchwoods - Stone Guide (87639)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 222,
        flag="sack_guide_87639",
        region="Pitchwoods"
    ),
    "Mal's Floating Castle - Top Hat": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 223,
        flag="chest_dapper_76601",
        region="Mal's Floating Castle"
    ),
    "Pitchwoods - A Lord's Orders x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 224,
        flag="whiteblaze_81684",
        region="Pitchwoods"
    ),
    "The Ruined Temple - A Lord's Orders": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 225,
        flag="ruins_blaze_63821",
        region="The Ruined Temple"
    ),
    "Salt Alkymancery - A Lord's Orders x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 226,
        flag="lab_white_blaze_52768",
        region="Salt Alkymancery"
    ),
    "Pitchwoods - Salt8D": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 227,
        flag="wood_salt_97049",
        region="Pitchwoods"
    ),
    "Pitchwoods - Carapace Pavise": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 228,
        flag="shield_bug_98672",
        region="Pitchwoods"
    ),
    "The Ruined Temple - Drowning Blazed": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 229,
        flag="ruins_blaze_58795",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Warhorn": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 230,
        flag="sack_horn_59932",
        region="Ziggurat of Dust"
    ),
    "Red Hall of Cages - A Soldier's Poem x3 (35368)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 231,
        flag="castle_white_flame_35400",
        region="Red Hall of Cages"
    ),
    "Castle of Storms - Grenado x5": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 232,
        flag="castle_grenado_36186",
        region="Castle of Storms"
    ),
    "Red Hall of Cages - Charred Doll x3 (48102)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 233,
        flag="dungeon_redspark_48102",
        region="Red Hall of Cages"
    ),
    "The Ruined Temple - Bag of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 234,
        flag="ruins_lit_satellite",
        region="The Ruined Temple"
    ),
    "The Ruined Temple - A Soldier's Poem x3 (59717)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 235,
        flag="ruins_whiteflame_59879",
        region="The Ruined Temple"
    ),
    "The Blackest Vault - Statue Guided": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 236,
        flag="dark_guide_78731",
        region="The Blackest Vault"
    ),
    "The Blackest Vault - Drowned Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 237,
        flag="dark_drowning_72431",
        region="The Blackest Vault"
    ),
    "Dome of the Forgotten - Phial of Undersight x3 (57326)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 238,
        flag="vision_potion_57948",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Phial of Undersight x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 239,
        flag="vision_potion_59027",
        region="Dome of the Forgotten"
    ),
    "Red Hall of Cages - Pendragon Targe": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 240,
        flag="shield_snakes_36862",
        region="Red Hall of Cages"
    ),
    "Red Hall of Cages - A Soldier's Poem x3 (37585)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 241,
        flag="white_flame_36251",
        region="Red Hall of Cages"
    ),
    "Crypt of Dead Gods - Drowned Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 242,
        flag="tomb_drowning_39444",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - Drowned Censer": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 243,
        flag="tomb_drowning_34471",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - Stone Leader": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 244,
        flag="tomb_leader_33954",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - Stone Sellsword": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 245,
        flag="tomb_sellsword_32326",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - Stone Merchant": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 246,
        flag="tomb_merchant_41183",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - Charred Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 247,
        flag="tomb_red_43297",
        region="Crypt of Dead Gods"
    ),
    "Crypt of Dead Gods - A Lord's Orders x3 (36102)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 248,
        flag="tomb_blaze_36102",
        region="Crypt of Dead Gods"
    ),
    "The Ruined Temple - A King's Orders": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 249,
        flag="ruins_white_nova_62127",
        region="The Ruined Temple"
    ),
    "Salt Alkymancery - Blue Novas": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 250,
        flag="lake_blue_nova_58614",
        region="Salt Alkymancery"
    ),
    "Crypt of Dead Gods - A Lord's Orders x3 (43128)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 251,
        flag="tomb_white_blaze_43101",
        region="Crypt of Dead Gods"
    ),
    "Pitchwoods - Charred Tome": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 252,
        flag="red_nova_89055",
        region="Pitchwoods"
    ),
    "The Still Palace - A King's Orders": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 253,
        flag="white_nova_54936",
        region="The Still Palace"
    ),
    "Cran's Pass - Twisted Heart": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 254,
        flag="beast_nova_57914",
        region="Cran's Pass"
    ),
    "Salt Alkymancery - Drowned Tome": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 255,
        flag="drowning_nova_70536",
        region="Salt Alkymancery"
    ),
    "Salt Alkymancery - Drowned Idol x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 256,
        flag="lake_drowning_spark_63525",
        region="Salt Alkymancery"
    ),
    "The Blackest Vault - Drowned Censer x4": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 257,
        flag="drowning_blaze_99197",
        region="The Blackest Vault"
    ),
    "The Blackest Vault - Frozen Reliquary x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 258,
        flag="blue_blaze_89507",
        region="The Blackest Vault"
    ),
    "Salt Alkymancery - Frozen Reliquary x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 259,
        flag="lab_statue_flame_53285",
        region="Salt Alkymancery"
    ),
    "Crypt of Dead Gods - Frozen Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 260,
        flag="tomb_blueflame_32358",
        region="Crypt of Dead Gods"
    ),
    "The Ruined Temple - Charred Reliquary x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 261,
        flag="ruins_redblaze_62072",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Pack of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 262,
        flag="salt10_59096",
        region="Ziggurat of Dust"
    ),
    "Crypt of Dead Gods - Horn Will": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 263,
        flag="tomb_horn_33424",
        region="Crypt of Dead Gods"
    ),
    "Hager's Cavern - Warhorn": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 264,
        flag="cave_horn_40269",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Frozen Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 265,
        flag="dungeon_blueflame_41789",
        region="Hager's Cavern"
    ),
    "Village of Smiles - Silver Leaf": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 266,
        flag="amberspark_21678",
        region="Village of Smiles"
    ),
    "Sunken Keep - Forestfang x25 (29340)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 267,
        flag="amberspark_29340",
        region="Sunken Keep"
    ),
    "Red Hall of Cages - Silver Leaf (34967)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 268,
        flag="amberspark_34967",
        region="Red Hall of Cages"
    ),
    "Castle of Storms - Silver Leaf (44009)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 269,
        flag="amberspark_44009",
        region="Castle of Storms"
    ),
    "Dome of the Forgotten - Amber Idol": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 270,
        flag="amberflame_55884",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Amber Idol (63733)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 271,
        flag="amberflame_63733",
        region="Dome of the Forgotten"
    ),
    "The Ruined Temple - Amber Idol (57738)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 272,
        flag="amberflame_57738",
        region="The Ruined Temple"
    ),
    "Red Hall of Cages - Silver Leaf": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 273,
        flag="amberspark_35625",
        region="Red Hall of Cages"
    ),
    "Ziggurat of Dust - Silver Leaf": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 274,
        flag="amberspark_89011",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Amber Flamed": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 275,
        flag="amberflame_77460",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Amber Idol": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 276,
        flag="amberflame_74984",
        region="Ziggurat of Dust"
    ),
    "The Ruined Temple - Diamond Cluster": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 277,
        flag="amberblaze_63398",
        region="The Ruined Temple"
    ),
    "Siam Lake - Diamond Cluster": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 278,
        flag="amberblaze_65995",
        region="Siam Lake"
    ),
    "Hager's Cavern - Diamond Cluster": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 279,
        flag="amberblaze_44050",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Amber Idol": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 280,
        flag="amberflame_36690",
        region="Hager's Cavern"
    ),
    "Crypt of Dead Gods - Shimmering Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 281,
        flag="ambernova_37920",
        region="Crypt of Dead Gods"
    ),
    "Mire of Stench - Shimmering Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 282,
        flag="ambernova_26747",
        region="Mire of Stench"
    ),
    "Crypt of Dead Gods - Diamond Cluster": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 283,
        flag="amberblaze_35703",
        region="Crypt of Dead Gods"
    ),
    "Hager's Cavern - Silver Leaf x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 284,
        flag="amberspark_32400",
        region="Hager's Cavern"
    ),
    "Sunken Keep - Forestfang x25 (33302)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 285,
        flag="amberspark_33302",
        region="Sunken Keep"
    ),
    "Dome of the Forgotten - Sohei Kesa": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 286,
        flag="chest_monk_67709",
        region="Dome of the Forgotten"
    ),
    "Red Hall of Cages - Stone Leader": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 287,
        flag="statue_leader_40725",
        region="Red Hall of Cages"
    ),
    "Ziggurat of Dust - Horn Will": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 288,
        flag="pyramid_horn_will",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Bloodluster's Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 289,
        flag="pyramid_ring_bloody",
        region="Ziggurat of Dust"
    ),
    "Ziggurat of Dust - Castaway's Greatadze": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 290,
        flag="axe_anchor_76586",
        region="Ziggurat of Dust"
    ),
    "Pitchwoods - Amber Idol": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 291,
        flag="amberflame_96931",
        region="Pitchwoods"
    ),
    "Bandit's Pass - Amethyst Bodice": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 292,
        flag="purpledress",
        region="Bandit's Pass"
    ),
    "Ziggurat of Dust - Bloodwood Crossbow": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 293,
        flag="crossbow_84383",
        region="Ziggurat of Dust"
    ),
    "Bandit's Pass - Platoon Crossbow": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 294,
        flag="crossbow_27928",
        region="Bandit's Pass"
    ),
    "Pitchwoods - Russet Mask": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 295,
        flag="tater_80183",
        region="Pitchwoods"
    ),
    "Dome of the Forgotten - Predator Bascinet": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 296,
        flag="dome_gold_archer_62526",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Rowan Crosier": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 297,
        flag="dome_staff_61236",
        region="Dome of the Forgotten"
    ),
    "Ziggurat of Dust - Salt6D": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 298,
        flag="salt3_83579",
        region="Ziggurat of Dust"
    ),
    "Pitchwoods - Salt9D": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 299,
        flag="salt9_90297",
        region="Pitchwoods"
    ),
    "Pitchwoods - Case of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 300,
        flag="salt7_76309",
        region="Pitchwoods"
    ),
    "Cran's Pass - Crate of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 301,
        flag="salt9_38479",
        region="Cran's Pass"
    ),
    "Hager's Cavern - Sack of Salt (37688)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 302,
        flag="salt4_37688",
        region="Hager's Cavern"
    ),
    "Hager's Cavern - Sack of Salt (31461)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 303,
        flag="salt4_31461",
        region="Hager's Cavern"
    ),
    "Castle of Storms - Shroud Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 304,
        flag="castle_charm_dark",
        region="Castle of Storms"
    ),
    "Siam Lake - Goldenstone Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 305,
        flag="lit_def_65127",
        region="Siam Lake"
    ),
    "Castle of Storms - Impen Crest Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 306,
        flag="castle_fire_def_36739",
        region="Castle of Storms"
    ),
    "Sunken Keep - Crystalmoat Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 307,
        flag="ring_mp_moat_23891",
        region="Sunken Keep"
    ),
    "Mire of Stench - Sack of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 308,
        flag="swamp_salt4_19784",
        region="Mire of Stench"
    ),
    "Village of Smiles - Ghastly Gourd": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 309,
        flag="village_pumpkin_helm_16011",
        region="Village of Smiles"
    ),
    "Ziggurat of Dust - Ashen Effigy": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 310,
        flag="shield_skulls_77787",
        region="Ziggurat of Dust"
    ),
    "Village of Smiles - Chef's Toque": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 311,
        flag="village_chef_set_3635",
        region="Village of Smiles"
    ),
    "Mire of Stench - Virulent Scimitar": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 312,
        flag="swamp_rust_26825",
        region="Mire of Stench"
    ),
    "Hager's Cavern - Spiked Door - Venomous Blade": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 313,
        flag="mag_poison_buff_31947",
        region="Hager's Cavern - Spiked Door"
    ),
    "Village of Smiles - Blacksmith's Apron": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 314,
        flag="village_smith_armor6464",
        region="Village of Smiles"
    ),
    "The Watching Woods - Antidote x3 (18143)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 315,
        flag="forest_antidote_18143",
        region="The Watching Woods"
    ),
    "The Watching Woods - Antidote x3 (16501)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 316,
        flag="forest_antidote_16501",
        region="The Watching Woods"
    ),
    "Village of Smiles - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 317,
        flag="village_gray_pearl_14826",
        region="Village of Smiles"
    ),
    "The Watching Woods - Gray Pearl (23529)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 318,
        flag="frst_gray_pearl_23529",
        region="The Watching Woods"
    ),
    "Hager's Cavern - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 319,
        flag="cave_gray_pearl_30650",
        region="Hager's Cavern"
    ),
    "Red Hall of Cages - Gray Pearl (43910)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 320,
        flag="dng_gray_pearl_43910",
        region="Red Hall of Cages"
    ),
    "The Ruined Temple - Gray Pearl (62452)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 321,
        flag="ruins_gray_pearl_62452",
        region="The Ruined Temple"
    ),
    "Ziggurat of Dust - Gray Pearl (73816)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 322,
        flag="ruins_gray_pearl_73816",
        region="Ziggurat of Dust"
    ),
    "Pitchwoods - Gray Pearl (77413)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 323,
        flag="woods_gray_pearl_77413",
        region="Pitchwoods"
    ),
    "Pitchwoods - Gray Pearl (70430)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 324,
        flag="woods_gray_pearl_70430",
        region="Pitchwoods"
    ),
    "Red Hall of Cages - Gray Pearl (46576)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 325,
        flag="dng_gray_pearl_46576",
        region="Red Hall of Cages"
    ),
    "Dome of the Forgotten - Crystal Sphere": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 326,
        flag="dm_crystal_sphere_59492",
        region="Dome of the Forgotten"
    ),
    "Castle of Storms - Crystal Sphere (43675)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 327,
        flag="cos_crystal_sphere_43675",
        region="Castle of Storms"
    ),
    "Bandit's Pass - Crystal Sphere": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 328,
        flag="bp_crystal_sphere_26211",
        region="Bandit's Pass"
    ),
    "Crypt of Dead Gods - Crystal Sphere": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 329,
        flag="tomb_crys_sphere_39557",
        region="Crypt of Dead Gods"
    ),
    "The Watching Woods - A Soldier's Poem": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 330,
        flag="forest_flame_17206",
        region="The Watching Woods"
    ),
    "Castle of Storms - Demon Kabuto": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 331,
        flag="castle_samurai_48868",
        region="Castle of Storms"
    ),
    "The Watching Woods - Crimson Hood": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 332,
        flag="forest_redmage_13008",
        region="The Watching Woods"
    ),
    "Dome of the Forgotten - Aristocrat's Corset": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 333,
        flag="chest_princess_set",
        region="Dome of the Forgotten"
    ),
    "Hager's Cavern - Whistlebone Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 334,
        flag="bluecave_ease_34622",
        region="Hager's Cavern"
    ),
    "Mal's Floating Castle - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 335,
        flag="flying_blue_blaze",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Crystal Sphere": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 336,
        flag="flying_blue_blaze_47374",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Frozen Reliquary": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 337,
        flag="flying_blue_blaze_48951",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Silversalt Charm": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 338,
        flag="flying_blue_blaze_48867",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Box of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 339,
        flag="flying_salt_47999",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Stone Guide (49983)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 340,
        flag="vert_guide_49983",
        region="Mal's Floating Castle"
    ),
    "Mal's Floating Castle - Guardsman's Halberd": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 341,
        flag="vert_poleaxe_48693",
        region="Mal's Floating Castle"
    ),
    "Castle of Storms - Gray Pearl (50257)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 342,
        flag="castle_gpearl_50257",
        region="Castle of Storms"
    ),
    "Castle of Storms - Crystal Sphere (51796)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 343,
        flag="castle_csphere_51796",
        region="Castle of Storms"
    ),
    "The Still Palace - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 344,
        flag="graypearl_43563",
        region="The Still Palace"
    ),
    "Sunken Keep - Crystal Sphere": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 345,
        flag="crystalsphere_28712",
        region="Sunken Keep"
    ),
    "Village of Smiles - Stone Cleric (13574)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 346,
        flag="clerc_13574",
        region="Village of Smiles"
    ),
    "Pitchwoods - Gray Pearld": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 347,
        flag="graypearl_79116",
        region="Pitchwoods"
    ),
    "Pitchwoods - Gray Pearl (90392)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 348,
        flag="graypearl_90392",
        region="Pitchwoods"
    ),
    "The Still Palace - Gray Pearl (349)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 349,
        flag="graypearl_60274",
        region="The Still Palace"
    ),
    "The Still Palace - Gray Pearl (350)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 350,
        flag="graypearl_60705",
        region="The Still Palace"
    ),
    "Sunken Keep - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 351,
        flag="graypearl_33819",
        region="Sunken Keep"
    ),
    "Bandit's Pass - Infantry Poleaxe": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 352,
        flag="halberd_30452",
        region="Bandit's Pass"
    ),
    "Bandit's Pass - Twinmetal Ring": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 353,
        flag="hidden_sanctuary_ring_melee",
        region="Bandit's Pass"
    ),
    "Castle of Storms - Box of Salt": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 354,
        flag="castle_mal_reward",
        region="Castle of Storms"
    ),
    "Dome of the Forgotten - White Blazed": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 355,
        flag="dome_lords_mat",
        region="Dome of the Forgotten"
    ),
    "Shivering Shore - Gray Pearl": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 356,
        flag="beach_g_pearl_31",
        region="Shivering Shore"
    ),
    "Red Hall of Cages - Red Blazed": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 357,
        flag="red_blaze_39215",
        region="Red Hall of Cages"
    ),
    "Sunken Keep - Frozen Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 358,
        flag="blue_spark_31328",
        region="Sunken Keep"
    ),
    "Sunken Keep - Frozen Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 359,
        flag="blue_flame_13049",
        region="Sunken Keep"
    ),
    "Cran's Pass - Ring Wisdomd": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 360,
        flag="ring_wis_17942",
        region="Cran's Pass"
    ),
    "Sunken Keep - Blue Spark": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 361,
        flag="blue_spark_24466",
        region="Sunken Keep"
    ),
    "Fort-Beyond-the-Mire - Oar": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 362,
        flag="boat_oar_3128",
        region="Fort-Beyond-the-Mire"
    ),
    "The Watching Woods - Gray Pearl (22879)": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 363,
        flag="gray_pearl_22879",
        region="The Watching Woods"
    ),
    "Dome of the Forgotten - Red Flamed": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 364,
        flag="red_flame_39666",
        region="Dome of the Forgotten"
    ),
    "Dome of the Forgotten - Charred Locket x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 365,
        flag="red_flame_39924",
        region="Dome of the Forgotten"
    ),
    "Bandit's Pass - Charred Doll x3": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 366,
        flag="charred_doll_25592",
        region="Bandit's Pass"
    ),
    "Cran's Pass - Beast Novad": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 367,
        flag="beast_nova_37303",
        region="Cran's Pass"
    ),
    "Bandit's Pass - Charred Doll": SaltSanctuaryLocationData(
        code=PICKUP_BASE_ID + 368,
        flag="redspark_secret",
        region="Bandit's Pass"
    ),
}

brand_npc_locations: Dict[str, SaltSanctuaryLocationData] = {
    "Sunken Keep - Vertigo Brand NPC": SaltSanctuaryLocationData(
        code=BRAND_LOC_BASE_ID + 0,
        flag="rune_upside_down",
        region="Sunken Keep post False Jester"
    ),
    "Castle of Storms - Shadowflip Brand NPC": SaltSanctuaryLocationData(
        code=BRAND_LOC_BASE_ID + 1,
        flag="rune_wall_jump",
        region="Castle of Storms post Kraeken Wyrm"
    ),
    "Mire of Stench - Redshift Brand NPC": SaltSanctuaryLocationData(
        code=BRAND_LOC_BASE_ID + 2,
        flag="rune_red_block",
        region="Mire of Stench"
    ),
    "Dome of the Forgotten - Hardlight Brand NPC": SaltSanctuaryLocationData(
        code=BRAND_LOC_BASE_ID + 3,
        flag="rune_blue_ether",
        region="Dome of the Forgotten post Third Lamb"
    ),
    "Ziggurat of Dust - Dart Brand NPC": SaltSanctuaryLocationData(
        code=BRAND_LOC_BASE_ID + 4,
        flag="rune_dash",
        region="Ziggurat of Dust post Dried King"
    ),
}


location_table: Dict[str, SaltSanctuaryLocationData] = {**boss_locations, **boss_drop_locations, **pickup_locations, **brand_npc_locations}

