# Level Sanity Locations for Salt and Sanctuary
from typing import Dict, NamedTuple
from BaseClasses import ItemClassification


class LevelLocationData(NamedTuple):
    code: int
    region: str = "Menu"


# Level location base ID: 283690000
# Levels 1-549 (max level is 550, but you start at level 1)
LEVEL_BASE_ID = 283690000

# Generate all level locations (1-549)
level_locations: Dict[str, LevelLocationData] = {}
for level in range(1, 550):
    level_locations[f"Level {level}"] = LevelLocationData(
        code=LEVEL_BASE_ID + level,
        region="Menu"
    )


def get_level_locations_for_mode(mode: int) -> Dict[str, LevelLocationData]:
    """
    Returns level locations based on the level sanity mode.
    Mode 0: No locations (vanilla)
    Mode 1: Levels 1-50
    Mode 2: Levels 1-150
    Mode 3: Levels 1-250
    Mode 4: All levels 1-549
    """
    if mode == 0:
        return {}
    elif mode == 1:
        max_level = 50
    elif mode == 2:
        max_level = 150
    elif mode == 3:
        max_level = 250
    else:  # mode 4
        max_level = 549
    
    return {name: data for name, data in level_locations.items() 
            if data.code <= LEVEL_BASE_ID + max_level}
