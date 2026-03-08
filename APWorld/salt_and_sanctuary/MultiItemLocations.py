# Multi-Item Location data
# When enabled, each item in a multi-item pickup becomes its own AP location
from typing import Dict, List, NamedTuple

MULTI_ITEM_BASE_ID = 283700000

class MultiItemLocationData(NamedTuple):
    code: int
    flag: str
    sub_index: int  # Which item in the multi-pickup (0, 1, 2, etc.)
    item_name: str  # The vanilla item at this location
    region: str


# Maps flag -> region for multi-item locations
MULTI_ITEM_REGIONS = {
    "sanc1salt": "The Festering Banquet",
    "fortresssalt2": "The Festering Banquet",
    "fortress_throw_dagger": "The Festering Banquet",
    "village_thief_armor": "The Festering Banquet",
    "fortress_lit_ball": "The Festering Banquet",
    "hidden_sanctuary_spear_pitchfork": "Bandit's Pass",
    "hidden_sanctuary_ring_melee": "Bandit's Pass",
    "hidden_sancledge_spark": "Bandit's Pass",
    "crossbow_27928": "Bandit's Pass",
    "stone_ledge_tribe_armor": "Bandit's Pass",
    "stone_ledge_salt": "Bandit's Pass",
    "hidden_tree_heal2": "Bandit's Pass",
    "fortress_bow": "The Festering Banquet",
    "fortress_spear": "The Festering Banquet",
    "fortressstatue_guide_11407": "The Festering Banquet",
    "fortress_mage_16430": "The Festering Banquet",
    "fortress_lit_15226": "The Festering Banquet",
    "purpledress": "Bandit's Pass",
    "hidden_passage_jester_boots": "Bandit's Pass",
    "hidden_tunic_set": "Bandit's Pass",
    "village_white_spark_8031": "Village of Smiles",
    "village_smith_armor6464": "Village of Smiles",
    "village_chef_set_3635": "Village of Smiles",
    "under_village_salt": "Village of Smiles",
    "hidden_passage_7771": "Bandit's Pass",
    "forest_salt_13409": "The Watching Woods",
    "forest_redmage_13008": "The Watching Woods",
    "forest_redhigh_mage": "The Watching Woods",
    "forest_buckler_19508": "The Watching Woods",
    "greenvillage_leather_set": "Sunken Keep",
    "greenvillage_blacksmith": "Sunken Keep",
    "dungeon_health_statue_mage": "Red Hall of Cages",
    "greenvillage_salt6_32253": "Sunken Keep",
    "midsecret_shield_oval": "Sunken Keep",
    "hidden_black_set": "Bandit's Pass",
    "village_hunter_armor": "Castle of Storms",
    "dungeon_37107": "Red Hall of Cages",
    "chest_monk_67709": "Dome of the Forgotten",
    "dungeon_salt3statue_blacksmith": "Red Hall of Cages",
    "dungeon_beast_spark": "Red Hall of Cages",
    "dungeon_knight_armor": "Red Hall of Cages",
    "dungeon_salt_50208": "Red Hall of Cages",
    "dungeon_health_shard": "Red Hall of Cages",
    "cave_paladin_armor": "Hager's Cavern",
    "swamp_salt4_19784": "Mire of Stench",
    "swamp_pirate_24248": "Mire of Stench",
    "alchemist_set_25603": "Mire of Stench",
    "fort_boat_5646": "Fort-Beyond-the-Mire",
    "ruin_salt_4420": "Fort-Beyond-the-Mire",
    "tater_80183": "Pitchwoods",
    "ruins_armor_sorceror": "The Ruined Temple",
    "ruins_spear_pilum": "The Ruined Temple",
    "stag_armor_84279": "Ziggurat of Dust",
    "ruins_guide_armor_59910": "The Ruined Temple",
    "lab_saltknight_50361": "Salt Alkymancery",
    "lab_saltknight_47048": "Salt Alkymancery",
    "chest_dapper_76601": "Mal's Floating Castle",
    "chest_devil_67709": "The Ruined Temple",
    "castle_golem_set_34559": "Castle of Storms",
    "castle_ninja_38321": "Castle of Storms",
    "castle_samurai_48868": "Castle of Storms",
    "fortress_dreadset_14620": "The Festering Banquet",
    "dungeon_38275": "Red Hall of Cages",
    "swamp_cleric_set_16647": "Mire of Stench",
    "dome_fat_set": "Dome of the Forgotten",
    "dome_patched_set": "Dome of the Forgotten",
    "dome_gold_archer_62526": "Dome of the Forgotten",
    "swamp_rust_26825": "Mire of Stench",
    "chest_princess_set": "Dome of the Forgotten",
    "dome_gun_flintlock_60325": "Dome of the Forgotten",
    "dome_merchant_61077": "Dome of the Forgotten",
    "hidden_blades_23019": "Sunken Keep",
    "hidden_blades_24405": "Sunken Keep",
}

# Human-readable names for locations
MULTI_ITEM_NAMES = {
    "sanc1salt": "The Festering Banquet - Sanctuary Salt",
    "fortresssalt2": "The Festering Banquet - Salt & Merchant",
    "fortress_throw_dagger": "The Festering Banquet - Throwing Daggers",
    "village_thief_armor": "The Festering Banquet - Thief Set",
    "fortress_lit_ball": "The Festering Banquet - Blacksmith Statue",
    "hidden_sanctuary_spear_pitchfork": "Bandit's Pass - Hidden Pitchfork",
    "hidden_sanctuary_ring_melee": "Bandit's Pass - Plated Band",
    "hidden_sancledge_spark": "Bandit's Pass - Hidden Ledge",
    "crossbow_27928": "Bandit's Pass - Crossbow",
    "stone_ledge_tribe_armor": "Bandit's Pass - Raider Set",
    "stone_ledge_salt": "Bandit's Pass - Flanged Mace",
    "hidden_tree_heal2": "Bandit's Pass - Hidden Heal",
    "fortress_bow": "The Festering Banquet - Bow",
    "fortress_spear": "The Festering Banquet - Spear",
    "fortressstatue_guide_11407": "The Festering Banquet - Guide Statue",
    "fortress_mage_16430": "The Festering Banquet - Mage Statue",
    "fortress_lit_15226": "The Festering Banquet - Lightning Bolt",
    "purpledress": "Bandit's Pass - Amethyst Set",
    "hidden_passage_jester_boots": "Bandit's Pass - Jester Set",
    "hidden_tunic_set": "Bandit's Pass - Cotton Set",
    "village_white_spark_8031": "Village of Smiles - Lock of Hair",
    "village_smith_armor6464": "Village of Smiles - Blacksmith Armor",
    "village_chef_set_3635": "Village of Smiles - Chef Set",
    "under_village_salt": "Village of Smiles - Warhorn",
    "hidden_passage_7771": "Bandit's Pass - Dish Set",
    "forest_salt_13409": "The Watching Woods - Salt & Antidote",
    "forest_redmage_13008": "The Watching Woods - Red Mage Set",
    "forest_redhigh_mage": "The Watching Woods - High Mage Statue",
    "forest_buckler_19508": "The Watching Woods - Buckler",
    "greenvillage_leather_set": "Sunken Keep - Leather Set",
    "greenvillage_blacksmith": "Sunken Keep - Blacksmith & Poem",
    "dungeon_health_statue_mage": "Red Hall of Cages - Health & Mage",
    "greenvillage_salt6_32253": "Sunken Keep - Salt & Merchant",
    "midsecret_shield_oval": "Sunken Keep - Askarian Scutum",
    "hidden_black_set": "Bandit's Pass - Black Set",
    "village_hunter_armor": "Castle of Storms - Hunter Set",
    "dungeon_37107": "Red Hall of Cages - Salt & Lightning",
    "chest_monk_67709": "Dome of the Forgotten - Sohei Set",
    "dungeon_salt3statue_blacksmith": "Red Hall of Cages - Salt & Blacksmith",
    "dungeon_beast_spark": "Red Hall of Cages - Endless Fang",
    "dungeon_knight_armor": "Red Hall of Cages - Knight Set",
    "dungeon_salt_50208": "Red Hall of Cages - Lightvessel & Salt",
    "dungeon_health_shard": "Red Hall of Cages - Merchant & Salt",
    "cave_paladin_armor": "Hager's Cavern - Paladin Set",
    "swamp_salt4_19784": "Mire of Stench - Salt & Charm",
    "swamp_pirate_24248": "Mire of Stench - Pirate Set",
    "alchemist_set_25603": "Mire of Stench - Alchemist Set",
    "fort_boat_5646": "Fort-Beyond-the-Mire - Boat Set",
    "ruin_salt_4420": "Fort-Beyond-the-Mire - Salt & Pearl",
    "tater_80183": "Pitchwoods - Tater Set",
    "ruins_armor_sorceror": "The Ruined Temple - Sorcerer Set",
    "ruins_spear_pilum": "The Ruined Temple - Breach Pike & Pearl",
    "stag_armor_84279": "Ziggurat of Dust - Plate Set",
    "ruins_guide_armor_59910": "The Ruined Temple - Guide Set",
    "lab_saltknight_50361": "Salt Alkymancery - Ranseur & Shield",
    "lab_saltknight_47048": "Salt Alkymancery - Salt Knight Set",
    "chest_dapper_76601": "Mal's Floating Castle - Dapper Set",
    "chest_devil_67709": "The Ruined Temple - Bloodbrow Set",
    "castle_golem_set_34559": "Castle of Storms - Titan Set",
    "castle_ninja_38321": "Castle of Storms - Assassin Set",
    "castle_samurai_48868": "Castle of Storms - Samurai Set",
    "fortress_dreadset_14620": "The Festering Banquet - Cavalier Set",
    "dungeon_38275": "Red Hall of Cages - Crypt Patched Set",
    "swamp_cleric_set_16647": "Mire of Stench - Cleric Set",
    "dome_fat_set": "Dome of the Forgotten - Scorpion Set",
    "dome_patched_set": "Dome of the Forgotten - Patched Set",
    "dome_gold_archer_62526": "Dome of the Forgotten - Gold Archer Set",
    "swamp_rust_26825": "Mire of Stench - Virulent Scimitar",
    "chest_princess_set": "Dome of the Forgotten - Princess Set",
    "dome_gun_flintlock_60325": "Dome of the Forgotten - Flintlock Set",
    "dome_merchant_61077": "Dome of the Forgotten - Merchant Set",
    "hidden_blades_23019": "Sunken Keep - Lamprey Barbut Set",
    "hidden_blades_24405": "Sunken Keep - Lamprey Cuirass Set",
}

# Raw multi-item data: flag -> list of (item_name, sub_index)
MULTI_ITEM_DATA = {
    "sanc1salt": [
        ("salt1", 0),
        ("health_shard", 1),
    ],
    "fortresssalt2": [
        ("salt2", 0),
        ("statue_merchant", 1),
    ],
    "fortress_throw_dagger": [
        ("throw_dagger", 0),
        ("torch", 1),
    ],
    "village_thief_armor": [
        ("thief_helm", 0),
        ("thief_armor", 1),
        ("thief_boots", 2),
        ("thief_gloves", 3),
    ],
    "fortress_lit_ball": [
        ("statue_blacksmith", 0),
        ("health_shard", 1),
    ],
    "hidden_sanctuary_spear_pitchfork": [
        ("salt1", 0),
        ("spear_pitchfork", 1),
    ],
    "hidden_sanctuary_ring_melee": [
        ("ring_melee", 0),
        ("firepot", 1),
    ],
    "hidden_sancledge_spark": [
        ("mace_flanged", 0),
        ("salt3", 1),
    ],
    "crossbow_27928": [
        ("crossbow", 0),
        ("bolt", 1),
    ],
    "stone_ledge_tribe_armor": [
        ("tribe_armor", 0),
        ("shield_viking", 1),
    ],
    "stone_ledge_salt": [
        ("salt3", 0),
        ("tribe_helm", 1),
        ("tribe_boots", 2),
    ],
    "hidden_tree_heal2": [
        ("heal2", 0),
        ("waterpot", 1),
    ],
    "fortress_bow": [
        ("bow", 0),
        ("arrow", 1),
    ],
    "fortress_spear": [
        ("spear", 0),
        ("salt2", 1),
    ],
    "fortressstatue_guide_11407": [
        ("statue_guide", 0),
        ("horn_guide", 1),
    ],
    "fortress_mage_16430": [
        ("statue_mage", 0),
        ("buff_dark", 1),
    ],
    "fortress_lit_15226": [
        ("torch", 0),
        ("lit_bolt", 1),
    ],
    "purpledress": [
        ("purpledress_armor", 0),
        ("purpledress_boots", 1),
        ("purpledress_helm", 2),
    ],
    "hidden_passage_jester_boots": [
        ("jester_boots", 0),
        ("jester_armor", 1),
        ("jester_helm", 2),
    ],
    "hidden_tunic_set": [
        ("tunic_armor", 0),
        ("tunic_boots", 1),
        ("axe", 2),
    ],
    "village_white_spark_8031": [
        ("white_spark", 0),
        ("salt1", 1),
    ],
    "village_smith_armor6464": [
        ("blacksmith_armor", 0),
        ("blacksmith_gloves", 1),
        ("blacksmith_boots", 2),
    ],
    "village_chef_set_3635": [
        ("chef_helm", 0),
        ("chef_armor", 1),
        ("chef_boots", 2),
        ("mace_pot", 3),
    ],
    "under_village_salt": [
        ("salt2", 0),
        ("horn_will", 1),
    ],
    "hidden_passage_7771": [
        ("dish_armor", 0),
        ("dish_helm", 1),
        ("dish_gloves", 2),
        ("dish_boots", 3),
    ],
    "forest_salt_13409": [
        ("salt1", 0),
        ("antidote", 1),
    ],
    "forest_redmage_13008": [
        ("redmage_helm", 0),
        ("redmage_armor", 1),
        ("redmage_gloves", 2),
        ("redmage_boots", 3),
    ],
    "forest_redhigh_mage": [
        ("statue_mage", 0),
        ("salt2", 1),
    ],
    "forest_buckler_19508": [
        ("shield_buckler", 0),
        ("statue_sellsword", 1),
    ],
    "greenvillage_leather_set": [
        ("leather_helm", 0),
        ("leather_armor", 1),
        ("leather_gloves", 2),
        ("leather_boots", 3),
    ],
    "greenvillage_blacksmith": [
        ("statue_blacksmith", 0),
        ("white_flame", 1),
    ],
    "dungeon_health_statue_mage": [
        ("health_shard", 0),
        ("statue_mage", 1),
    ],
    "greenvillage_salt6_32253": [
        ("salt6", 0),
        ("statue_merchant", 1),
    ],
    "midsecret_shield_oval": [
        ("salt4", 0),
        ("shield_oval", 1),
    ],
    "hidden_black_set": [
        ("black_helm", 0),
        ("black_armor", 1),
        ("black_gloves", 2),
        ("black_boots", 3),
    ],
    "village_hunter_armor": [
        ("hunter_helm", 0),
        ("hunter_armor", 1),
        ("hunter_gloves", 2),
        ("hunter_boots", 3),
    ],
    "dungeon_37107": [
        ("salt3", 0),
        ("buff_lit", 1),
    ],
    "chest_monk_67709": [
        ("monk_armor", 0),
        ("monk_boots", 1),
        ("monk_gloves", 2),
    ],
    "dungeon_salt3statue_blacksmith": [
        ("salt3", 0),
        ("statue_blacksmith", 1),
    ],
    "dungeon_beast_spark": [
        ("salt3", 0),
        ("beast_spark", 1),
    ],
    "dungeon_knight_armor": [
        ("knight_helm", 0),
        ("knight_armor", 1),
        ("knight_gloves", 2),
        ("knight_boots", 3),
    ],
    "dungeon_salt_50208": [
        ("salt4", 0),
        ("waterpot", 1),
    ],
    "dungeon_health_shard": [
        ("statue_merchant", 0),
        ("salt3", 1),
    ],
    "cave_paladin_armor": [
        ("paladin_helm", 0),
        ("paladin_armor", 1),
        ("paladin_gloves", 2),
        ("paladin_boots", 3),
        ("shield_paladin", 4),
    ],
    "swamp_salt4_19784": [
        ("salt4", 0),
        ("charm_heavy_poison", 1),
    ],
    "swamp_pirate_24248": [
        ("pirate_armor", 0),
        ("pirate_helm", 1),
        ("pirate_boots", 2),
    ],
    "alchemist_set_25603": [
        ("alchemist_helm", 0),
        ("alchemist_armor", 1),
        ("alchemist_boots", 2),
    ],
    "fort_boat_5646": [
        ("boat_armor", 0),
        ("boat_helm", 1),
        ("boat_boots", 2),
    ],
    "ruin_salt_4420": [
        ("salt6", 0),
        ("black_pearl", 1),
    ],
    "tater_80183": [
        ("tater_helm", 0),
        ("tater_armor", 1),
        ("tater_gloves", 2),
        ("tater_boots", 3),
    ],
    "ruins_armor_sorceror": [
        ("armor_sorceror", 0),
        ("boots_sorceror", 1),
        ("mag_firestar", 2),
    ],
    "ruins_spear_pilum": [
        ("spear_pilum", 0),
        ("gray_pearl", 1),
    ],
    "stag_armor_84279": [
        ("stag_armor", 0),
        ("stag_gloves", 1),
        ("stag_boots", 2),
        ("sword", 3),
        ("shield_banner", 4),
    ],
    "ruins_guide_armor_59910": [
        ("guide_helm", 0),
        ("guide_boots", 1),
        ("guide_gloves", 2),
        ("guide_armor", 3),
    ],
    "lab_saltknight_50361": [
        ("pole_ranseur", 0),
        ("shield_saltknight", 1),
    ],
    "lab_saltknight_47048": [
        ("saltknight_armor", 0),
        ("saltknight_helm", 1),
        ("saltknight_gloves", 2),
        ("saltknight_boots", 3),
    ],
    "chest_dapper_76601": [
        ("dapper_helm", 0),
        ("dapper_armor", 1),
        ("dapper_gloves", 2),
        ("dapper_boots", 3),
    ],
    "chest_devil_67709": [
        ("devil_helm", 0),
        ("devil_armor", 1),
        ("devil_boots", 2),
    ],
    "castle_golem_set_34559": [
        ("golem_helm", 0),
        ("golem_armor", 1),
        ("golem_gloves", 2),
        ("golem_boots", 3),
    ],
    "castle_ninja_38321": [
        ("ninja_helm", 0),
        ("ninja_armor", 1),
        ("ninja_gloves", 2),
        ("ninja_boots", 3),
    ],
    "castle_samurai_48868": [
        ("samurai_helm", 0),
        ("samurai_armor", 1),
        ("samurai_gloves", 2),
        ("samurai_boots", 3),
    ],
    "fortress_dreadset_14620": [
        ("dread_helm", 0),
        ("dread_armor", 1),
        ("dread_gloves", 2),
        ("dread_boots", 3),
    ],
    "dungeon_38275": [
        ("patched_helm", 0),
        ("patched_armor", 1),
        ("patched_gloves", 2),
        ("patched_boots", 3),
    ],
    "swamp_cleric_set_16647": [
        ("cleric_helm", 0),
        ("cleric_armor", 1),
        ("cleric_boots", 2),
    ],
    "dome_fat_set": [
        ("merchant_helm", 0),
        ("merchant_armor", 1),
        ("merchant_gloves", 2),
        ("merchant_boots", 3),
    ],
    "dome_patched_set": [
        ("fat_helm", 0),
        ("fat_armor", 1),
        ("fat_gloves", 2),
        ("fat_boots", 3),
    ],
    "dome_gold_archer_62526": [
        ("gold_archer_helm", 0),
        ("gold_archer_armor", 1),
        ("gold_archer_gloves", 2),
        ("gold_archer_boots", 3),
    ],
    "swamp_rust_26825": [
        ("sword_rust", 0),
    ],
    "chest_princess_set": [
        ("reddress_helm", 0),
        ("armor_reddress", 1),
        ("boots_reddress", 2),
    ],
    "dome_gun_flintlock_60325": [
        ("gun_flintlock", 0),
        ("flintshot", 1),
    ],
    "dome_merchant_61077": [
        ("merchant_helm", 0),
        ("merchant_armor", 1),
        ("merchant_gloves", 2),
        ("merchant_boots", 3),
    ],
    "hidden_blades_23019": [
        ("lamprey_helm", 0),
        ("lamprey_greaves", 1),
    ],
    "hidden_blades_24405": [
        ("lamprey_armor", 0),
        ("lamprey_gauntlets", 1),
    ],
}


def build_multi_item_locations() -> Dict[str, MultiItemLocationData]:
    """Build the complete multi-item location table."""
    locations = {}
    code_offset = 0
    
    for flag, items in MULTI_ITEM_DATA.items():
        region = MULTI_ITEM_REGIONS.get(flag, "Unknown")
        base_name = MULTI_ITEM_NAMES.get(flag, flag)
        
        for item_name, sub_index in items:
            # Create location name like "Village of Smiles - Thief Set (1)"
            loc_name = f"{base_name} ({sub_index + 1})"
            
            locations[loc_name] = MultiItemLocationData(
                code=MULTI_ITEM_BASE_ID + code_offset,
                flag=flag,
                sub_index=sub_index,
                item_name=item_name,
                region=region,
            )
            code_offset += 1
    
    return locations


# Pre-built location table
multi_item_locations: Dict[str, MultiItemLocationData] = build_multi_item_locations()

# Helper to get all locations for a specific flag
def get_locations_for_flag(flag: str) -> List[MultiItemLocationData]:
    """Get all multi-item locations for a specific flag."""
    return [loc for loc in multi_item_locations.values() if loc.flag == flag]


# Count of total multi-item locations
def get_multi_item_location_count() -> int:
    """Get total number of multi-item locations."""
    return len(multi_item_locations)


# Get flags that have multi-item data
def get_multi_item_flags() -> set:
    """Get set of all flags that have multi-item data."""
    return set(MULTI_ITEM_DATA.keys())
