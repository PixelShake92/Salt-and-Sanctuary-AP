# Options for Salt and Sanctuary
from dataclasses import dataclass
from Options import Toggle, Choice, PerGameCommonOptions


class SkillTreeRandomized(Choice):
    """
    Randomizes the skill tree.
    Vanilla: No skill tree randomization
    Skills Only: Equipment class nodes are shuffled, other nodes work normally
    Full Shuffle: All nodes become AP locations and skill unlocks become AP items
    """
    display_name = "Skill Tree Randomized"
    option_vanilla = 0
    option_skills_only = 1
    option_full_shuffle = 2
    default = 0


class SkillTreeLogicStrictness(Choice):
    """
    How strictly skill tree locations are gated by game progression.
    
    Lenient: Assumes aggressive salt farming. Earlier access to deeper nodes.
    Normal: Standard progression pace for most players.
    Strict: Assumes minimal grinding, boss-only salt income. Later access.
    
    This affects when skill tree locations become logically accessible based
    on how many bosses you've defeated.
    """
    display_name = "Skill Tree Logic Strictness"
    option_lenient = 0
    option_normal = 1
    option_strict = 2
    default = 1


class SkillTreeLogicMethod(Choice):
    """
    How skill tree progression requirements are calculated.
    
    Brands: Locations unlock based on which movement brands you have.
            More reliable since brands are actual items in your inventory.
    Boss Count: Locations unlock based on how many boss locations are reachable.
                More dynamic but can have edge cases.
    """
    display_name = "Skill Tree Logic Method"
    option_brands = 0
    option_boss_count = 1
    default = 0


class SkillTreeRequireParents(Toggle):
    """
    In Full Shuffle mode, require parent node items to access child nodes.
    
    When enabled, you must receive the item from a parent node before
    the child node location becomes accessible. This creates a more
    interconnected logic structure.
    
    Only applies when Skill Tree Randomized is set to Full Shuffle.
    """
    display_name = "Skill Tree Require Parents"
    default = True


class LevelSanity(Choice):
    """
    Adds level-ups as locations that grant items.
    Vanilla: No level locations (default)
    Level 50: Levels 1-50 are locations (50 checks)
    Level 150: Levels 1-150 are locations (150 checks)
    Level 250: Levels 1-250 are locations (250 checks)
    All Levels: Levels 1-549 are locations (549 checks)
    """
    display_name = "Level Sanity"
    option_vanilla = 0
    option_level_50 = 1
    option_level_150 = 2
    option_level_250 = 3
    option_all_levels = 4
    default = 0


class FallDamageReduction(Choice):
    """
    Reduces or eliminates fall damage.
    Normal: Standard fall damage
    Half: Fall damage reduced by 50%
    None: No fall damage (lethal falls become heavy landings)
    """
    display_name = "Fall Damage Reduction"
    option_normal = 0
    option_half = 1
    option_none = 2
    default = 0


class SplitMultiItemLocations(Toggle):
    """
    Splits multi-item pickups into separate locations.
    When enabled, pickups that contain multiple items (like armor sets)
    become multiple AP checks instead of one.
    Adds approximately 70 extra locations.
    """
    display_name = "Split Multi-Item Locations"
    default = False


class SkillTreeHintProgression(Toggle):
    """
    Automatically hint skill tree locations that contain progression items.
    
    When enabled, any skill tree node that has a progression item (for any player)
    will be auto-hinted at the start of the game. This helps players identify
    which skill tree nodes are worth prioritizing without excessive grinding.
    
    Only applies when Skill Tree Randomized is enabled.
    """
    display_name = "Skill Tree Hint Progression"
    default = True


class KillSanity(Toggle):
    """
    Adds first-time bestiary kills as AP location checks.
    Each unique enemy type in the bestiary becomes a location when you kill
    it for the first time. Adds 71 locations.
    """
    display_name = "Kill Sanity"
    default = False


class ShopSanity(Toggle):
    """
    Adds shop purchases as AP location checks.
    Each item in every shop (sanctuary NPCs, map NPCs, special vendors)
    becomes a location check when purchased. Adds 872 locations.
    """
    display_name = "Shop Sanity"
    default = False


class IncludeUnspeakableDeep(Toggle):
    """
    Include the Unspeakable Deep boss and its associated locations.
    
    The Unspeakable Deep is a unique "trick" boss at the very start of the game.
    You only get ONE attempt per save file - if you die or skip it, you cannot
    retry without starting a new save.
    
    When disabled (default): The Unspeakable Deep locations are excluded from
    the randomizer, preventing potential softlocks.
    
    When enabled: The Unspeakable Deep locations are included. Players must
    defeat this boss on their first attempt or restart their save file.
    
    WARNING: Only enable this if you're confident in defeating this boss
    on your first try, or willing to restart if you fail.
    """
    display_name = "Include Unspeakable Deep"
    default = False


@dataclass
class SaltSanctuaryOptions(PerGameCommonOptions):
    skill_tree_randomized: SkillTreeRandomized
    skill_tree_logic_strictness: SkillTreeLogicStrictness
    skill_tree_logic_method: SkillTreeLogicMethod
    skill_tree_require_parents: SkillTreeRequireParents
    level_sanity: LevelSanity
    fall_damage_reduction: FallDamageReduction
    split_multi_item_locations: SplitMultiItemLocations
    skill_tree_hint_progression: SkillTreeHintProgression
    kill_sanity: KillSanity
    shop_sanity: ShopSanity
    include_unspeakable_deep: IncludeUnspeakableDeep
