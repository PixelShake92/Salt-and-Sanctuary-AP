from typing import Dict, Any
from BaseClasses import MultiWorld, Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld

from .Items import SaltSanctuaryItem, item_table
from .Locations import SaltSanctuaryLocation, location_table
from .Regions import (create_regions, set_region_rules, LEVER_ITEM_NAMES,
                      LEVERS, LEVER_ITEM_IDS, LEVER_LOC_IDS,
                      LEVER_ITEM_BASE_ID, LEVER_LOC_BASE_ID)
from .SkillItems import skill_item_table
from .SkillTreeLocations import skilltree_locations
from .SkillTreeLogic import create_combined_rules, create_level_rules
from .LevelLocations import level_locations, get_level_locations_for_mode
from .MultiItemLocations import multi_item_locations, get_multi_item_flags
from .KillLocations import kill_locations, KILL_BASE_ID
from .Options import SaltSanctuaryOptions


class SaltSanctuaryWebWorld(WebWorld):
    theme = "dirt"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up Salt and Sanctuary for Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["PixelShake92"]
        )
    ]


# Build item name to ID mapping
_item_name_to_id: Dict[str, int] = {}
for name, data in item_table.items():
    _item_name_to_id[name] = data.code
for name, data in skill_item_table.items():
    _item_name_to_id[name] = data.code
for name, item_id in LEVER_ITEM_IDS.items():
    _item_name_to_id[name] = item_id

# Build location name to ID mapping (includes all possible locations)
_location_name_to_id: Dict[str, int] = {}
for name, data in location_table.items():
    _location_name_to_id[name] = data.code
for name, data in skilltree_locations.items():
    _location_name_to_id[name] = data.code
for name, data in level_locations.items():
    _location_name_to_id[name] = data.code
for name, data in multi_item_locations.items():
    _location_name_to_id[name] = data.code
for name, loc_id in LEVER_LOC_IDS.items():
    _location_name_to_id[name] = loc_id
for name, data in kill_locations.items():
    _location_name_to_id[name] = data.code


class SaltSanctuaryWorld(World):
    """
    Salt and Sanctuary is a 2D action RPG with brutal combat and deep progression.
    Explore a cursed island, defeat challenging bosses, and uncover dark secrets.
    """
    game = "Salt and Sanctuary"
    web = SaltSanctuaryWebWorld()
    
    options_dataclass = SaltSanctuaryOptions
    options: SaltSanctuaryOptions
    
    item_name_to_id = _item_name_to_id
    location_name_to_id = _location_name_to_id
    
    data_version = 5
    
    def create_item(self, name: str) -> SaltSanctuaryItem:
        if name in item_table:
            item_data = item_table[name]
            return SaltSanctuaryItem(name, item_data.classification, item_data.code, self.player)
        elif name in skill_item_table:
            item_data = skill_item_table[name]
            return SaltSanctuaryItem(name, item_data.classification, item_data.code, self.player)
        elif name in LEVER_ITEM_IDS:
            return SaltSanctuaryItem(name, ItemClassification.progression, LEVER_ITEM_IDS[name], self.player)
        else:
            raise KeyError(f"Unknown item: {name}")
    
    def create_items(self) -> None:
        skill_tree_mode = self.options.skill_tree_randomized.value
        skill_tree_enabled = skill_tree_mode > 0  # Mode 1 or 2
        level_sanity_mode = self.options.level_sanity.value
        split_multi_items = self.options.split_multi_item_locations.value
        include_unspeakable_deep = self.options.include_unspeakable_deep.value
        kill_sanity = self.options.kill_sanity.value
        
        # Import here to avoid circular imports
        from .Locations import UNSPEAKABLE_DEEP_LOCATIONS
        
        # Get level locations for this mode
        active_level_locations = get_level_locations_for_mode(level_sanity_mode)
        
        # Calculate total locations
        total_locations = len(location_table)
        
        # Subtract Unspeakable Deep locations if disabled
        if not include_unspeakable_deep:
            total_locations -= len(UNSPEAKABLE_DEEP_LOCATIONS)
        
        if skill_tree_enabled:
            total_locations += len(skilltree_locations)
        total_locations += len(active_level_locations)
        
        # Add multi-item locations if enabled
        if split_multi_items:
            # Multi-item locations REPLACE their base pickup counterparts,
            # so subtract the overlapping base pickups and add the sub-locations
            multi_flags = get_multi_item_flags()
            total_locations -= len(multi_flags)
            total_locations += len(multi_item_locations)
        
        # Add lever locations (always on when AP connected)
        total_locations += len(LEVERS)
        
        # Add kill sanity locations if enabled
        if kill_sanity:
            total_locations += len(kill_locations)
        
        items_created = 0
        
        # Starting items - player gets these automatically
        starting_items = ["Sanctuary Key", "Fortress Key"]
        for item_name in starting_items:
            item = self.create_item(item_name)
            self.multiworld.push_precollected(item)
        
        # If skill tree is randomized, precollect Class 1 unlocks needed by starting classes
        # This ensures any starting class can use their starting equipment
        # Classes and their Class 1 requirements:
        #   Knight: Swordfighter 1, Heavy Armor 1
        #   Mage: Magic 1, Wand 1
        #   Paladin: Berzerker 1, Heavy Armor 1
        #   Cleric: Prayer 1, Light Armor 1
        #   Hunter: Marksman 1, Hunter 1
        #   Thief/Chef/Pauper: Only use Class 0 items (no unlocks needed)
        if skill_tree_enabled:
            starting_class_unlocks = [
                "Swordfighter Class 1",  # Knight (swords/daggers)
                "Berzerker Class 1",     # Paladin (hammers/axes)
                "Magic Class 1",         # Mage (spells)
                "Wand Class 1",          # Mage (wands)
                "Prayer Class 1",        # Cleric (prayers)
                "Light Armor Class 1",   # Cleric
                "Heavy Armor Class 1",   # Knight, Paladin
                "Marksman Class 1",      # Hunter (crossbows/pistols)
                "Hunter Class 1",        # Hunter (whips/reapers)
            ]
            for item_name in starting_class_unlocks:
                item = self.create_item(item_name)
                self.multiworld.push_precollected(item)
        
        # Add all PROGRESSION items (required) - except starting items
        for item_name, item_data in item_table.items():
            if item_data.classification == ItemClassification.progression:
                if item_name in starting_items:
                    continue  # Skip, already given as starting item
                item = self.create_item(item_name)
                self.multiworld.itempool.append(item)
                items_created += 1
        
        # Add all USEFUL items (important)
        for item_name, item_data in item_table.items():
            if item_data.classification == ItemClassification.useful:
                item = self.create_item(item_name)
                self.multiworld.itempool.append(item)
                items_created += 1
        
        # Add lever items (always shuffled, progression)
        for lever in LEVERS:
            item = self.create_item(lever.item_name)
            self.multiworld.itempool.append(item)
            items_created += 1
        
        # Add skill items if skill tree randomized (mode 1 or 2)
        if skill_tree_enabled:
            # Track which items were precollected as starting class unlocks
            starting_class_unlocks = {
                "Swordfighter Class 1",
                "Berzerker Class 1",
                "Magic Class 1",
                "Wand Class 1",
                "Prayer Class 1",
                "Light Armor Class 1",
                "Heavy Armor Class 1",
                "Marksman Class 1",
                "Hunter Class 1",
            }
            
            for item_name, item_data in skill_item_table.items():
                quantity = item_data.quantity
                
                # Subtract 1 from quantity if this was precollected as a starting unlock
                if item_name in starting_class_unlocks:
                    quantity -= 1
                
                # Add remaining copies to the pool
                for _ in range(max(0, quantity)):
                    item = self.create_item(item_name)
                    self.multiworld.itempool.append(item)
                    items_created += 1
        
        # Add FILLER items only to fill remaining slots
        filler_items = [name for name, data in item_table.items() 
                       if data.classification == ItemClassification.filler]
        
        filler_needed = total_locations - items_created
        for i in range(max(0, filler_needed)):
            filler_name = filler_items[i % len(filler_items)]
            item = self.create_item(filler_name)
            self.multiworld.itempool.append(item)
    
    def create_regions(self) -> None:
        from .Regions import _DEFAULT_SUBREGION
        
        skill_tree_mode = self.options.skill_tree_randomized.value
        skill_tree_enabled = skill_tree_mode > 0  # Mode 1 or 2
        level_sanity_mode = self.options.level_sanity.value
        split_multi_items = self.options.split_multi_item_locations.value
        
        # Create base regions
        # When split_multi_items is enabled, exclude base pickup locations
        # whose flags are replaced by multi-item sub-locations
        if split_multi_items:
            excluded_flags = get_multi_item_flags()
        else:
            excluded_flags = None
        create_regions(self, skill_tree_enabled, excluded_pickup_flags=excluded_flags)
        
        # Add level locations to Menu region if level sanity is enabled
        if level_sanity_mode > 0:
            active_level_locations = get_level_locations_for_mode(level_sanity_mode)
            menu_region = self.multiworld.get_region("Menu", self.player)
            
            for loc_name, loc_data in active_level_locations.items():
                location = SaltSanctuaryLocation(self.player, loc_name, loc_data.code, menu_region)
                menu_region.locations.append(location)
        
        # Add multi-item locations if enabled
        if split_multi_items:
            for loc_name, loc_data in multi_item_locations.items():
                # Map old coarse region names to new sub-region names
                subregion_name = _DEFAULT_SUBREGION.get(loc_data.region, loc_data.region)
                try:
                    region = self.multiworld.get_region(subregion_name, self.player)
                except KeyError:
                    # Fallback: try the original name
                    region = self.multiworld.get_region("Menu", self.player)
                location = SaltSanctuaryLocation(self.player, loc_name, loc_data.code, region)
                region.locations.append(location)
        
        # Add kill sanity locations if enabled (placed in vanilla spawn regions)
        if self.options.kill_sanity.value:
            for loc_name, loc_data in kill_locations.items():
                if loc_data.region == "Menu":
                    region = self.multiworld.get_region("Menu", self.player)
                else:
                    try:
                        region = self.multiworld.get_region(loc_data.region, self.player)
                    except KeyError:
                        region = self.multiworld.get_region("Menu", self.player)
                location = SaltSanctuaryLocation(self.player, loc_name, loc_data.code, region)
                region.locations.append(location)
    
    def set_rules(self) -> None:
        # Apply region connection rules (brands, keys, levers)
        set_region_rules(self)
        
        # Get strictness option (used for both skill tree and levels)
        strictness_map = {0: "lenient", 1: "normal", 2: "strict"}
        strictness = strictness_map.get(
            self.options.skill_tree_logic_strictness.value, 
            "normal"
        )
        
        # Apply skill tree logic rules if skill tree is randomized
        skill_tree_mode = self.options.skill_tree_randomized.value
        
        if skill_tree_mode > 0:
            # Get method option (0 = brands, 1 = boss_count)
            method_map = {0: "brands", 1: "boss_count"}
            method = method_map.get(
                self.options.skill_tree_logic_method.value,
                "brands"
            )
            
            # Check if parent requirements are enabled (only for full_shuffle mode 2)
            require_parents = (
                skill_tree_mode == 2 and 
                self.options.skill_tree_require_parents.value
            )
            
            # Apply combined rules to skill tree locations
            create_combined_rules(
                world=self,
                strictness=strictness,
                method=method,
                require_parents=require_parents,
                require_all_parents=False  # ANY parent is sufficient
            )
        
        # Apply level location rules if level sanity is enabled
        level_sanity_mode = self.options.level_sanity.value
        if level_sanity_mode > 0:
            create_level_rules(
                world=self,
                strictness=strictness
            )
        
        # Set completion condition - must defeat The Nameless God
        self.multiworld.completion_condition[self.player] = lambda state: (
            state.has("Victory - The Nameless God", self.player)
        )
    
    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        """
        Provide additional context for hints about skill tree locations.
        This adds depth information to help players understand progression requirements.
        """
        skill_tree_mode = self.options.skill_tree_randomized.value
        if skill_tree_mode == 0:
            return
        
        # Add depth info to skill tree location hints
        for location in self.multiworld.get_locations(self.player):
            if location.name in skilltree_locations:
                loc_data = skilltree_locations[location.name]
                depth_info = f" (Depth {loc_data.depth})"
                
                # hint_data[player][location_id] = extra_hint_text
                if self.player not in hint_data:
                    hint_data[self.player] = {}
                hint_data[self.player][location.address] = depth_info
    
    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "skill_tree_randomized": self.options.skill_tree_randomized.value,
            "skill_tree_logic_strictness": self.options.skill_tree_logic_strictness.value,
            "skill_tree_logic_method": self.options.skill_tree_logic_method.value,
            "skill_tree_require_parents": self.options.skill_tree_require_parents.value,
            "level_sanity": self.options.level_sanity.value,
            "fall_damage_reduction": self.options.fall_damage_reduction.value,
            "split_multi_item_locations": self.options.split_multi_item_locations.value,
            "skill_tree_hint_progression": self.options.skill_tree_hint_progression.value,
            "include_unspeakable_deep": self.options.include_unspeakable_deep.value,
            "kill_sanity": self.options.kill_sanity.value,
        }
