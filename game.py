"""
Name: Eric Choi
Student Number: A01260740
Name: Justin Yoon
Student Number: A01247378
"""
import itertools
import random
import doctest
import time
import math


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def STORY_LINES_CONSTANT():
    """Returns dictionary constant for STORY_LINES."""
    return {"ellinia": ["You see the ancient green trees of Ellinia grow over head.",
                        "The rainforest around you absorbs you, you are lost in the deep woods."],
            "perion": ["The heat of the desert sun beats down on your back. The sun of Perion",
                       "The dry air surrounds you. It's hard to breathe in the heat"],
            "kerning": ["You see the abandoned sky scrapers of Kerning City in the distance.",
                        "The small of urban sprawl enters your nostrils. You long for the clean air of Ellinia."],
            "henesys": ["A cheerful little area you find yourself in. The fields of Henesys are in the distance",
                        "You see the farmers of Henesys hard at work."],
            "sleepy wood": ["The ominous vibes around you are strong. Are you in Sleepy Wood?",
                            "The woods here differ from those you found in Ellinia. This must be Sleepy Wood."]}


def MAX_HP_CHARACTER_CONSTANT():
    """Returns max hp for player."""
    return 20


def MAX_HP_MONSTER_CONSTANT():
    """Returns max hp for monsters."""
    return 10


def BASE_PLAYER_DMG_CONSTANT():
    """Returns base dmg for player."""
    return 10


def MAX_FLEE_DMG_CONSTANT():
    """Returns max dmg for fleeing."""
    return 4


def FLEE_DMG_CHANCE_CONSTANT():
    """Returns the chance of taking flee damage."""
    return 0.2


def MONSTER_FLEE_CHANCE_CONSTANT():
    """Returns the chance of monsters fleeing from you."""
    return 0.2


def MAX_MONSTER_DMG_CONSTANT():
    """Returns max dmg for monsters."""
    return 10


def ENCOUNTER_CHANCE_CONSTANT():
    """Returns percentage of an encounter."""
    return 0.2


def NON_VALID_SYMBOLS_FOR_NAME_CONSTANT():
    """Returns list of symbols not valid for name."""
    return ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "{", "]", "}", "|", ";", ">",
            "<", "/", "?"]


def STARTING_POSITION_CONSTANT():
    """Returns an array for the starting position of players."""
    return [0, 0]


def EXP_BEFORE_LEVEL_UP_CONSTANT():
    """Returns how much EXP you need before leveling up."""
    return 500


def NUMBER_COL_CONSTANT():
    """Returns the number of columns on the game board."""
    return 25


def MONSTER_FLEE_CHANCE():
    """Returns the percentage chance of a monster fleeing mid combat."""
    return 0.2


def NUMBER_ROW_CONSTANT():
    """Returns the number of columns on the game board."""
    return 25


def BOSS_DICTIONARY_CONSTANT():
    """Returns the dictionary of the boss."""
    return {"name": "Crimson Balrog", "desc": "It's a Crimson Balrog .. OMG!!!", "level": 3, "hp": 160, "dmg": 25,
            "zones": ["sleepy wood"]}


def LIST_OF_DICTIONARY_MONSTERS_CONSTANT():
    """Returns the list of dictionary monsters."""
    return [{"name": "Zombie Lupin", "desc": "It's a monkey... but a zombie",
             "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"], "exp": 100},
            {"name": "Ribbon Pig", "desc": "It's a pig ... with a ribbon",
             "level": 1, "hp": 8, "dmg": 15, "zones": ["henesys", "kerning", "perion"], "exp": 100},
            {"name": "Snail", "desc": "It's a snail ... yeah ",
             "level": 1, "hp": 15, "dmg": 2, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100},
            {"name": "Zakum", "desc": "It's a Zakum ... lol good luck",
             "level": 3, "hp": 80, "dmg": 20, "zones": ["sleepy wood"], "exp": 200},
            {"name": "Horntail", "desc": "It's a Horntail ... even worse than the zakum imo",
             "level": 3, "hp": 80, "dmg": 20, "zones": ["sleepy wood"], "exp": 200},
            {"name": "Blue Snail", "desc": "It's a snail ... yeah ",
             "level": 1, "hp": 15, "dmg": 2, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100},
            {"name": "Red Snail", "desc": "It's a snail ... yeah ",
             "level": 1, "hp": 15, "dmg": 2, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100},
            {"name": "Slime", "desc": "It's a slime ... kinda like jello ",
             "level": 1, "hp": 10, "dmg": 7, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100},
            {"name": "Blue Slime", "desc": "It's a slime ... kinda like blue jello ",
             "level": 2, "hp": 15, "dmg": 20, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 150},
            {"name": "Steel Pig", "desc": "It's a pig ... in armor ",
             "level": 2, "hp": 30, "dmg": 15, "zones": ["henesys", "kerning", "perion"], "exp": 150},
            {"name": "Stump", "desc": "It's a tree stump ... that moves ",
             "level": 1, "hp": 15, "dmg": 5, "zones": ["ellinia", "henesys", "kerning", "perion", "sleepy wood"],
             "exp": 100},
            {"name": "Axe Stump", "desc": "It's a tree stump ... with an axe",
             "level": 2, "hp": 30, "dmg": 14, "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 150},
            {"name": "Green Mushroom", "desc": "It's a mushroom ... but green this time ",
             "level": 2, "hp": 15, "dmg": 10, "zones": ["ellinia", "henesys", "kerning"], "exp": 150},
            {"name": "Blue Mushroom", "desc": "It's a mushroom ... but blue this time ",
             "level": 2, "hp": 15, "dmg": 10, "zones": ["henesys", "kerning", "sleepy wood"], "exp": 150},
            ]


def LIST_OF_CLASSES():
    """Returns the list of dictionary classes."""
    return [{"name": "warrior",
             "class_tier": {"first": {"name": "Spearman",
                                      "exp": 0,
                                      "hp": 50,
                                      "dmg": 10,
                                      "dodge": 0,
                                      "dmg_reduc": 0,
                                      },
                            "second": {"name": "Berserker",
                                       "exp": 200,
                                       "hp": 100,
                                       "dmg": 20,
                                       "dodge": 0.02,
                                       "dmg_reduc": 0,
                                       "attacks": ["Rushes forwards to knock back the enemy",
                                                   "wields his spear like a windmill to to pierce the enemy"]
                                       },
                            "third": {"name": "Dark Knight",
                                      "exp": 600,
                                      "hp": 200,
                                      "dmg": 30,
                                      "dodge": 0.05,
                                      "dmg_reduc": 0,
                                      "attacks": ["uses Dark Impale! You rapidly strike the enemy!",
                                                  "uses Gungnir's Descent! A mythical spear \033[1mDROPS\033[0m from "
                                                  "the heavens!"],
                                      }},
             "attack_lines": ["whacks the enemy with a spear!",
                              "smacks the enemy with a spear!",
                              "punches the enemy with fists!"]},
            {"name": "magician",
             "class_tier": {"first": {"name": "Magician",
                                      "exp": 0,
                                      "hp": 10,
                                      "dmg": 15,
                                      "dodge": 0,
                                      "dmg_reduc": 5
                                      },
                            "second": {"name": "Wizard",
                                       "exp": 200,
                                       "hp": 20,
                                       "dmg": 25,
                                       "dodge": 0.02,
                                       "dmg_reduc": 10,
                                       "attacks": ["uses Ice Strike to create an Ice explosion!",
                                                   "uses Explosion to create a Fire explosion!"]

                                       },
                            "third": {"name": "Arch Magician",
                                      "exp": 600,
                                      "hp": 30,
                                      "dmg": 35,
                                      "dodge": 0.05,
                                      "dmg_reduc": 20,
                                      "attacks": ["uses Blizzard! You summon a freezing artic wind to freeze your "
                                                  "enemy!",
                                                  "uses Meteor Shower! You summon meteorites from the sky to rain "
                                                  "down on the enemy"]

                                      }},
             "attack_lines": ["uses Magic Claw! You cast magical energy to scratch the enemy.",
                              "whacks the enemy with a staff!",
                              "uses Magic Ball to his the enemy with energy"]},
            {"name": "thief",
             "class_tier": {"first": {"name": "Assassin",
                                      "exp": 0,
                                      "hp": 15,
                                      "dmg": 15,
                                      "dodge": 0.20,
                                      "dmg_reduc": 0
                                      },
                            "second": {"name": "Hermit",
                                       "exp": 200,
                                       "hp": 30,
                                       "dmg": 25,
                                       "dodge": 0.50,
                                       "dmg_reduc": 10,
                                       "attacks": ["uses Shuriken Burst to throw exploding stars at the enemy!",
                                                   "uses Gust Charm to blow the enemy back!"]

                                       },
                            "third": {"name": "Night Lord",
                                      "exp": 600,
                                      "hp": 50,
                                      "dmg": 35,
                                      "dodge": 0.80,
                                      "dmg_reduc": 0,
                                      "attacks": ["uses Triple Throw! You throw 3 stars simultaneously",
                                                  "uses Dark Flare! You summon the Dark Lord's throwing star "
                                                  "and hurl it at the enemy"]

                                      }},
             "attack_lines": ["throws ninja stars at the enemy!",
                              "punches the enemy."]},
            {"name": "beginner",
             "class_tier": {"first": {"name": "Beginner",
                                      "exp": 0,
                                      "hp": 20,
                                      "dmg": 10,
                                      "dodge": 0,
                                      "dmg_reduc": 0
                                      },
                            "second": {"name": "Beginner",
                                       "exp": 200,
                                       "hp": 20,
                                       "dmg": 25,
                                       "dodge": 0,
                                       "dmg_reduc": 0,
                                       "attacks": ["threw a red snail shell!",
                                                   "threw a blue snail shell!",
                                                   "threw a snail shell!"]
                                       },
                            "third": {"name": "Beginner",
                                      "exp": 2000,
                                      "hp": 1000,
                                      "dmg": 500,
                                      "dodge": 1.00,
                                      "dmg_reduc": 0,
                                      "attacks": ["threw a red snail shell!",
                                                  "threw a blue snail shell!",
                                                  "threw a snail shell!"]
                                      }},
             "attack_lines": ["threw a red snail shell!",
                              "threw a blue snail shell!",
                              "threw a snail shell!"]}
            ]


def KERNING_BOUNDARY():
    """Returns the kerning boundary for the grid-based environment."""
    return {"x bound": (0, 12),
            "y bound": (0, 12)}


def PERION_BOUNDARY():
    """Returns the perion boundary for the grid-based environment."""
    return {"x bound": (13, 24),
            "y bound": (0, 12)}


def ELLINIA_BOUNDARY():
    """Returns the ellinia boundary for the grid-based environment."""
    return {"x bound": (13, 24),
            "y bound": (13, 24)}


def HENESYS_BOUNDARY():
    """Returns the henesys boundary for the grid-based environment."""
    return {"x bound": (0, 12),
            "y bound": (14, 24)}


def SLEEPY_BOUNDARY():
    """Returns the sleepy woods boundary for the grid-based environment."""
    return {"x bound": (7, 13),
            "y bound": (7, 13)}


def BOSS_POSITION():
    """Returns the boss position."""
    return 11, 11


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MOVEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def movement(character: dict):
    """
    Invokes get_valid_movement_input() and updates character['position'].
    Shows map at start.

    :param character: dictionary
    :precondition: character is a valid character dictionary
    :postcondition: updates character['position'] depending on get_valid_movement()
    """
    show_map(character['position'])
    player_input = get_valid_movement_input(character)
    if player_input == "North":
        character['position'][0] -= 1
    elif player_input == "South":
        character['position'][0] += 1
    elif player_input == "West":
        character['position'][1] -= 1
    elif player_input == "East":
        character['position'][1] += 1
    update_distance(character)
    activate_character(character)


def update_distance(character: dict):
    """
    Updates character['distance_goal'] to new values.

    :param character:  dictionary
    :precondition: character is a valid character dictionary
    :post condition: character[distance_goal] will hold a new array of [new distance from goal, old distance from goal]

    >>> test_dict = {'distance_goal': [30, 17], 'position': [11,0]}
    >>> update_distance(test_dict)
    >>> test_dict
    {'distance_goal': [11.0, 30], 'position': [11, 0]}
    """
    new_distance = calculate_distance_to_goal(character['position'])
    character['distance_goal'][1] = character['distance_goal'][0]
    character['distance_goal'][0] = new_distance


def get_valid_movement_input(character: dict) -> str:
    """
    Gets player input and validates it and returns it.

    :param character: dictionary
    :precondition: character is a valid character dictionary
    :postcondition: takes player input and returns a valid move from character['position']
    :return: string
    """
    list_of_valid_moves = get_valid_moves(character['position'])
    player_input = enumerate_list_options(list_of_valid_moves)
    return player_input


def get_valid_moves(position: list) -> list:
    """
    Returns list of valid moves from that position in respect to the game board dimensions.

    :param position: array of int
    :precondition: position is array of int and is of length 2
                    values in position[0] must be within range of range(NUMBER_ROW_CONSTANT)
                    values in position[1] must be within range of range(NUMBER_COL_CONSTANT)
    :postcondition: checks which moves are valid from position
                    returns a list of those valid moves
    :return: list of strings

    >>> get_valid_moves([0, 0])
    ['South', 'East']
    >>> get_valid_moves([2, 2])
    ['North', 'South', 'West', 'East']
    """
    list_of_valid_moves = []
    if position[0] > 0:
        list_of_valid_moves.append("North")
    if position[0] < NUMBER_ROW_CONSTANT():
        list_of_valid_moves.append("South")
    if position[1] > 0:
        list_of_valid_moves.append("West")
    if position[1] < NUMBER_COL_CONSTANT():
        list_of_valid_moves.append("East")
    return list_of_valid_moves


def activate_character(character: dict):
    """
    Changes the active key in character dictionary.

    :param character: dictionary
    :precondition: character is a valid character dictionary
    :postcondition: character['active'] = True

    >>> test_dict = {'active': False}
    >>> activate_character(test_dict)
    >>> test_dict['active']
    True
    """
    character['active'] = True


def calculate_distance_to_goal(position_array: list) -> float:
    """
    Returns an integer representing the distance to the goal.

    :param position_array: is an array of int
    :precondition:position_array: is an array of length 2 holding two integer within the bounds of game board
    :postcondition: find the distance between the goal x,y and the position_array x,y pair
    :return: a number

    >>> calculate_distance_to_goal([11, 0])
    11.0
    """
    return math.sqrt((BOSS_POSITION()[0] - position_array[0]) ** 2 + (BOSS_POSITION()[1] - position_array[1]) ** 2)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END MOVEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START COMBAT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_monster(character: dict, monster_cycle: dict) -> dict:
    """
    Gets the a monster dictionary from monster_cycle.

    :param character: dictionary
    :param monster_cycle: dictionary
    :precondition: character is a valid character dictionary
                    monster_cycle is a valid dictionary where  the values are itertools cycle objects
    :postcondition: finds what zone character is in
                    gets a monster from that zone
                    gets a monster within a level range
                    returns a valid monster dictionary
    :return: dictionary
    """
    zoned_cycle = monster_cycle.get(get_zone(character["position"]))
    while True:
        current_monster = next(zoned_cycle)
        if current_monster["level"] <= character["level"]["level"]:
            return current_monster


def combat(character: dict, monster_cycle: dict):
    """
    Picks boss from BOSS_DICTIONARY_CONSTANT.
    Simulates the combat between the character and the boss.
    Randomly picks monster from MONSTER_DICTIONARY_CONSTANT.
    Simulates chance of monster encounter.
    Either invokes combat_sim or heal depending on simulation.

    :param character: dictionary
    :param monster_cycle: dictionary
    :precondition: character is a valid character dictionary
                    monster_cycle is a valid dictionary where  the values are itertools cycle objects
    :postcondition: Simulates encountering boss and chance of encountering a monster
                    either invokes combat_sim or heal depending on simulation
    """
    if character["position"] == [BOSS_POSITION()[0], BOSS_POSITION()[1]]:
        encounter_boss(character)
    elif encountered():
        encountered_monster = get_monster(character, monster_cycle)
        combat_sim(character, encountered_monster)
    else:
        timed_print(f"There seems to be no monsters in the room, poggies!", 2)
        if character["hp"] < character["max_hp"]:
            heal(character)


def heal(character: dict):
    """
    Increases character["hp"] by 4.

    character ["hp"] is capped at MAX_CHARACTER_HP_CONSTANT()
    :param character: dictionary

    >>> test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "max_hp":30, "level": {"level": 1, "exp": 100}}
    >>> heal(test_player)
    You have healed 4, you now have 24 hp!
    """
    old_hp = character["hp"]
    if old_hp > character["max_hp"] - 4:
        character["hp"] = character["max_hp"]
    else:
        character["hp"] += 4
    timed_print(f"You have healed {character['hp'] - old_hp}, you now have {character['hp']} hp!", 2)


def combat_sim(character: dict, monster: dict):
    """
    Invokes either combat_round() or run_away_dmg_calc depending on player input.

    :param character: dictionary
    :param monster: dictionary
    :precondition: character is a valid character dictionary
                    monster is a valid monster dictionary
    :postcondition: takes user input to decide if combat_round() or run_away_dmg_calc() is
                    invoked.
                    Invokes combat_round(character, monster, 'monster' or 'character')  depending
                    on initiative roll.
    """
    monster_combat_dict = monster.copy()
    first_round = True
    while character["hp"] > 0 and monster_combat_dict["hp"] > 0 and \
            validate_player_input_combat(character, monster_combat_dict, first_round) == "Fight":
        first_round = False
        if monster_flee(monster):
            break
        combat_round(character, monster_combat_dict, combat_initiative_roll())
    if monster_combat_dict["hp"] <= 0:
        give_exp(character, monster)
    else:
        if run_away_damage_chance():
            run_away_dmg_calc(character, monster)


def monster_flee(monster: dict) -> bool:
    """
    Simulates monster fleeing in combat.

    :param monster: dictionary
    :precondition: monster is a valid monster dictionary
    :postcondition: simulates a chance of monster fleeing
                    returns true if simulated monster fleeing
                    returns false if monster doesnt flee
    :return: boolean
    """
    if random.random() <= MONSTER_FLEE_CHANCE():
        timed_print(f"{monster['name']} ran away!")
        return True
    else:
        return False


def boss_combat_sim(character: dict, monster: dict):
    """
    Invokes either combat_round() or run_away_dmg_calc depending on player input.

    :param character: dictionary
    :param monster: dictionary
    :precondition: character is a valid character dictionary
                    monster is a valid monster dictionary
    :postcondition: takes user input to decide if combat_round() or run_away_dmg_calc() is
                    invoked.
                    Invokes combat_round(character, monster, 'monster' or 'character')  depending
                    on initiative roll.
    """
    boss_first_round = True
    while character["hp"] > 0 and monster["hp"] > 0 and \
            validate_player_input_combat(character, monster, boss_first_round) == "Fight":
        boss_first_round = False
        combat_round(character, monster, combat_initiative_roll())
    if monster["hp"] <= 0:
        give_exp(character, monster)
    else:
        if run_away_damage_chance():
            run_away_dmg_calc(character, monster)


def combat_initiative_roll() -> str:
    """
    Returns string, either "monster" or "player" depending on who rolls higher.

    :postcondition: simulates 1d10 dice rolls for monster and player and returns whoever rolled higher
                    if rolls are equal call combat_initiative_roll again
    :return: string
    """
    player_roll = roll_dice(1, 10)
    monster_roll = roll_dice(1, 10)
    if player_roll > monster_roll:
        return "player"
    elif monster_roll > player_roll:
        return "monster"
    else:
        combat_initiative_roll()


def validate_player_input_combat(character: dict, monster: dict, first_encounter=True) -> str:
    """
    Takes player input for combat_sim

    :param first_encounter: boolean
    :param character: dictionary
    :param monster: dictionary
    :precondition: monster is a valid monster dictionary
                    character is a valid player dictionary
                    first_counter is a boolean
    :postcondition: returns a valid input choice from player
    :return: string
    """
    while True:
        if first_encounter:
            timed_print(f"You encounter a {monster['name']}: {monster['desc']}, will you fight or run away?", 1)
        else:
            timed_print(f"You have {character['hp']} health points.")
            timed_print(f"{monster['name']} has {monster['hp']} health points left.")
            timed_print(f"Will you continue to fight?")
        player_input = enumerate_list_options(["Fight", "Run away"])
        if player_input in ["Fight", "Run away"]:
            return player_input


def run_away_damage_chance() -> bool:
    """
    Simulated the chance of taking damage while fleeing returns boolean.
    True if you do get damage while fleeing.
    False if you dont.

    :postcondition: randomly generates a float between 0 and 1
                    if less that FLEE_DMG_CHANCE_CONSTANT()
    :return: Boolean
    """
    return random.random() < FLEE_DMG_CHANCE_CONSTANT()


def run_away_dmg_calc(character: dict, monster: dict):
    """
    Reduced character['hp'] by random.randint between 1 and MAX_RUN_AWAY_DMG_CONSTANT.

    :param character: dictionary
    :param monster: dictionary
    :precondition: character is a valid character dictionary
                    monster is a valid monster dictionary
                    character['hp'] > 0
    :postcondition: reduces character['hp'] by random.randint between 1 and MAX_RUN_AWAY_DMG_CONSTANT
    """
    timed_print(f"You tried to running away but the {monster['name']} was too fast for you.", 3)
    dmg_taken = random.randint(1, MAX_FLEE_DMG_CONSTANT())
    character["hp"] -= dmg_taken
    timed_print(f"You took a total of {dmg_taken} damage and now have {character['hp']} hp left", 1)


def combat_round(character: dict, monster: dict, attacker: str):
    """
    Depending on attacker character and monster take turns dealing damage to each other.

    :param character: dictionary
    :param monster: dictionary
    :param attacker: string
    :precondition: character is a valid character dictionary
                    monster is a valid monster dictionary
                    attacker is either "player" or "monster"
                    both character['hp'] and monster['hp'] > 0
    :postcondition: at least one of character or monster  hp values has decreased
    """
    if attacker == "monster":
        monster_dmg_deal(monster, character)
        if character["hp"] < 1:
            return
        else:
            player_dmg_deal(monster, character)
    else:
        player_dmg_deal(monster, character)
        if monster["hp"] < 1:
            return
        else:
            monster_dmg_deal(monster, character)


def player_dmg_deal(monster: dict, character: dict):
    """
    Handles when character deals damage to monster.

    :param monster: dictionary
    :param character: dictionary
    :precondition: monster is a valid monster dictionary
                    character is a valid character dictionary
    :postcondition: prints out battle text
                    monster["hp"] is reduced
    """
    character_dmg = roll_dice(1, character["dmg"])
    monster["hp"] -= character_dmg
    timed_print(f"{character['name']} {player_dmg_line(character, character_dmg)}")
    timed_print(f"You dealt {character_dmg} to the monster, it has {monster['hp']} hp left", 2)


def player_dmg_line(character: dict, dmg: int) -> str:
    """
    Chooses an attack line and prints it based on dmg value.

    :param character: dictionary
    :param dmg: integer
    :precondition: character is a valid character dictionary
                    dmg is a int within the range of the character's dmg
    :postcondition: finds what tier the dmg is in
                    picks a dmg line from that tier
                    prints dmg line
    :return: string
    """
    level_to_string_tier = {2: "second", 3: "third"}
    if dmg <= get_class(character.get("class"))["class_tier"]["first"]["dmg"]:
        return random.choice(get_class(character.get("class"))["attack_lines"])
    else:
        character_tier = get_class(character["class"])["class_tier"][level_to_string_tier[character["level"]["level"]]]
        return random.choice(character_tier["attacks"])


def monster_dmg_deal(monster: dict, character: dict):
    """
    Handles when monster deals damage to character.

    :param monster: dictionary
    :param character: dictionary
    :precondition: monster is a valid monster dictionary
                    character is a valid character dictionary
    :postcondition: prints out battle text
                    monster["hp"] is reduced
    """
    level_to_string_tier = {1: "first", 2: "second", 3: "third"}
    character_class_info = get_class(character["class"])["class_tier"][level_to_string_tier[character["level"]["level"]]]
    if random.random() < character_class_info["dodge"]:
        timed_print(f"You avoided the {monster['name']}'s attack!")
    else:
        try:
            block_amount = roll_dice(1, character_class_info["dmg_reduc"])
        except ValueError:
            block_amount = 0
        if block_amount > 0:
            timed_print(f"You blocked {block_amount} of damage!")
        monster_dmg = roll_dice(1, monster["dmg"]) - block_amount
        character["hp"] -= monster_dmg
        timed_print(f"The {monster['name']} deals {monster_dmg} to you with one swipe, you have {character['hp']} hp left")


def encountered() -> bool:
    """Returns boolean depending on if randomly randomly generated float is less than ENCOUNTER_CHANCE_CONSTANT.

    :postcondition: randomly generate a float in range 0 to 1.0 and does comparison to ENCOUNTER_CHANCE_CONSTANT
    :returns: boolean
    """
    return random.random() <= ENCOUNTER_CHANCE_CONSTANT()


def encounter_boss(character: dict):
    """
    Encounter the boss.

    When the character runs into the boss's tile on the map, the character is fought with the boss until death. The game
    ends with a victorious message if the player defeats the boss.

    :param character: a dictionary
    :precondition: character is a valid dictionary
    :postcondition: character battles the boss till death
    """
    boss_copy = BOSS_DICTIONARY_CONSTANT().copy()
    boss_combat_sim(character, boss_copy)
    if character["hp"] <= 0:
        player_died()
    elif boss_copy["hp"] <= 0:
        congrats(character)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END COMBAT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START EXP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def give_exp(character: dict, monster: dict):
    """
    Gives the character an exp according to the monster's level.
    Level 1 monsters should give 100 exp.
    Level 2 monsters should give 150 exp.
    Level 3 monsters should give 200 exp.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition: character and monster must be a valid dictionary
    :postcondition: character['exp'] has been adjusted according to monster['exp']
    {'level: {'level':2, 'exp': 400}, 'dmg': 13}
    >>> test_player = {"level": {"level": 1, "exp": 0}, "class": "warrior"}
    >>> test_monster = {"level": 1}
    >>> give_exp(test_player, test_monster)
    You have gained 100 exp
    >>> test_player["level"]["exp"] == 100
    True
    """
    if monster["level"] == 1:
        character["level"]["exp"] += 100
        timed_print("You have gained 100 exp")
    elif monster["level"] == 2:
        character["level"]["exp"] += 150
        timed_print("You have gained 150 exp")
    else:
        character["level"]["exp"] += 200
        timed_print("You have gained 200 exp", 1)
    if character["level"]["exp"] >= get_class(character["class"])["class_tier"]["third"]["exp"] \
            and character["level"]["level"] != 3:
        upgrade_character(character, "third")
    elif character["level"]["exp"] >= get_class(character["class"])["class_tier"]["second"]["exp"] \
            and character["level"]["level"] != 2:
        upgrade_character(character, "second")


def upgrade_character(character: dict, tier: str):
    """
    Upgrades damage and hp values for character to their current level.

    :param tier: string
    :param character: dictionary
    :precondition: character is a valid character dictionary
                    character hit a exp threshold
                    tier is either "first", "second", or "third"
    :postcondition: character max_hp and dmg has been updated
    """
    character_class_dictionary = get_class(character["class"])
    tier_string_number_dict = {"first": 1, "second": 2, "third": 3}
    character["max_hp"] = character_class_dictionary["class_tier"][tier]["hp"]
    character["dmg"] = character_class_dictionary["class_tier"][tier]["dmg"]
    character["level"]["level"] = tier_string_number_dict.get(tier)
    timed_print(f"You leveled up to {character['level']['level']}!!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END EXP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def story_time(character: dict):
    """
    Displays the story element from the story dictionary for corresponding position.

    :param character: dictionary
    :precondition: character is a valid character dictionary with a key of position
    :postcondition: uses position to get correct value from STORY_LINES_CONSTANT and
                    displays it.
    """
    strings_to_print = random.choice(STORY_LINES_CONSTANT().get(get_zone(character["position"])))
    timed_print(strings_to_print)
    if character["active"]:
        if character["distance_goal"][0] < character["distance_goal"][1]:
            timed_print("The aura is getting stronger", 0.5)
        elif character["distance_goal"][0] > character["distance_goal"][1]:
            timed_print("I feel the power drawing me get weaker", 0.5)
        else:
            timed_print("The aura feels the same.", 0.5)


def create_character() -> dict:
    """
    Returns a dictionary representing a character information.

    :postcondition: takes player input and creates and returns a new dictionary.
                    dictionary has key value pairs of:
                        - "name" : String
                        - "hp": int
                        - "position": [int, int]
                        - "level": {"level": int, "exp": int}
                        - distance_to_goal: [int, int]
    :return: dictionary
    """
    player_input_name = validate_name()
    player_input_class = choose_class()
    player_dict = {"name": player_input_name,
                   "hp": get_class(player_input_class).get("class_tier").get("first").get("hp"),
                   "max_hp": get_class(player_input_class).get("class_tier").get("first").get("hp"),
                   "class": player_input_class,
                   "position": STARTING_POSITION_CONSTANT(),
                   "level": {"level": 1, "exp": 0},
                   "distance_goal": [calculate_distance_to_goal(STARTING_POSITION_CONSTANT()),
                                     calculate_distance_to_goal(STARTING_POSITION_CONSTANT())],
                   "active": False,
                   "dmg": get_class(player_input_class).get("class_tier").get("first").get("dmg"), }
    return player_dict


def choose_class() -> str:
    """
    Returns string of class name a user picks.

    :postcondition: Shows users all possible class choices
                    Asks users to pick one
                    returns the string value of class name of chosen class
    :return: string
    """
    list_of_class_names = [each.get("name") for each in LIST_OF_CLASSES()]
    return enumerate_list_options(list_of_class_names)


def intro() -> dict:
    """
    Invokes create_character and returns that dictionary value.
    Prints message to player.

    :postcondition: prints a message
                    calls create_character
    :return: dictionary from create_character
    """
    timed_print("Hello, this is Victoria Island.")
    timed_print("Unfortunately your family has been brutally murdered by the Crimson Balrog.")
    timed_print("As you search for the beast you will encounter smaller monsters.")
    timed_print("Kill them to become stronger before you face your nemesis.")
    timed_print("As you move around the aura towards the beast will get stronger or weaker.")
    timed_print("Give up on your quest by using the 'quit' command as well")
    player_dictionary = create_character()

    return player_dictionary


def validate_name() -> str:
    """
    Takes input and returns input if valid input.
    Valid inputs are inputs not containing: !, @, #, $, %, ^, &, *, (, ), _, +, -, =, [, {, ], }, \, |, ;, >, <, /, ?

    :postcondition: Takes user input and makes sure it doesnt contain invalid symbols, returns player input
    :return: String
    """
    list_of_symbols_not_allowed = NON_VALID_SYMBOLS_FOR_NAME_CONSTANT()
    while True:
        timed_print("What is your name?")
        player_input = input("")
        if any(chac in player_input for chac in list_of_symbols_not_allowed):
            timed_print("Please do not use any strange characters, we don't have the budget for that", 2)
        else:
            return player_input


def player_died():
    """
    Prints message to player and exits program.

    :postcondition: prints message
                    exits python program
    """
    timed_print("Overconfidence is a slow and insidious killer ..", 1)
    timed_print("As you slowly bleed out, you look back at the death of your family ..", 1)
    timed_print("Filled with regret our hero could not get his revenge ..", 1)
    timed_print("You have died ..", 1)
    exit("Thanks for playing")


def congrats(character: dict):
    """
    Prints message to player.

    :param character: dictionary
    :precondition: character is a valid character dictionary
    :postcondition: prints out messages
    """
    timed_print("congrats you finished the game poggies", 1)
    timed_print(f"You finished the game at level {character['level']['level']}")
    exit("See you next time!")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END STORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START GAME STATE MANAGEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def is_player_dead(character: dict) -> bool:
    """
    Checks to see if character['hp'] is greater than 0.
    Returns True if isn't, False if it is.

    :param character: dictionary
    :precondition character: valid character dictionary
    :post condition: checks character dictionary value at key "hp" to see if it is greater than 0
                    returns boolean False if it is greater
                    returns True if it is not greater
    :return: boolean
    >>> is_player_dead({"hp": 0})
    True
    >>> is_player_dead({"hp": 2})
    False
    """
    return not character["hp"] > 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END GAME STATE MANAGEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UTILITY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def timed_print(string: str, delay=0.33):
    """
    Prints out string after delay amount of time.

    :param string: string
    :param delay: float
    :precondition: string is a string
                    delay is a float
    :postcondition: prints out string after delay amount of seconds

    >>> timed_print("Hello")
    Hello
    """
    time.sleep(delay)
    print(string)


def show_map(position_array: list):
    """"
    Prints out representation of map.
    X marks where player is.
    - marks rooms/possible positions.
    O marks goal.

    :param position_array: list
    :postcondition: prints out a representation of game board
    """
    grid_as_string = [[" - " for col in range(NUMBER_COL_CONSTANT())] for row in range(NUMBER_ROW_CONSTANT())]
    grid_as_string[BOSS_POSITION()[0]][BOSS_POSITION()[1]] = " O "
    grid_as_string[position_array[0]][position_array[1]] = " X "
    for row in grid_as_string:
        print(" ".join(each for each in row))


def get_zone(player_coords_list: list) -> str:
    """
    Returns the name of the zone the coordinates will fall under.

    :param player_coords_list: list
    :precondition: player_coords_list is a valid location on  the game map
    :postcondition: checks where the player_coord_list will fall under on the game map
                    returns the name of that zone
    :return: string
    >>> get_zone([0,0])
    'kerning'
    """
    if SLEEPY_BOUNDARY().get("x bound")[0] <= player_coords_list[1] <= SLEEPY_BOUNDARY().get("x bound")[1] \
            and SLEEPY_BOUNDARY().get("y bound")[0] <= player_coords_list[0] <= SLEEPY_BOUNDARY().get("y bound")[1]:
        return "sleepy wood"
    elif HENESYS_BOUNDARY().get("x bound")[0] <= player_coords_list[1] <= HENESYS_BOUNDARY().get("x bound")[1] \
            and HENESYS_BOUNDARY().get("y bound")[0] <= player_coords_list[0] <= HENESYS_BOUNDARY().get("y bound")[1]:
        return "henesys"
    elif PERION_BOUNDARY().get("x bound")[0] <= player_coords_list[1] <= PERION_BOUNDARY().get("x bound")[1] \
            and PERION_BOUNDARY().get("y bound")[0] <= player_coords_list[0] <= PERION_BOUNDARY().get("y bound")[1]:
        return "perion"
    elif ELLINIA_BOUNDARY().get("x bound")[0] <= player_coords_list[1] <= ELLINIA_BOUNDARY().get("x bound")[1] \
            and ELLINIA_BOUNDARY().get("y bound")[0] <= player_coords_list[0] <= ELLINIA_BOUNDARY().get("y bound")[1]:
        return "ellinia"
    elif KERNING_BOUNDARY().get("x bound")[0] <= player_coords_list[1] <= KERNING_BOUNDARY().get("x bound")[1] \
            and KERNING_BOUNDARY().get("y bound")[0] <= player_coords_list[0] <= KERNING_BOUNDARY().get("y bound")[1]:
        return "kerning"


def get_class(class_name: str) -> dict:
    """
    Gets the class dictionary from LIST_of_CLASSES that matches class_name.

    :param class_name: string
    :precondition: class_name is a valid string of value warrior, magician, bowman, thief
    :postcondition: finds the dictionary that holds the name value of the class_name and returns that
    :return: dictionary
    >>> get_class("magician").get("name")
    'magician'
    """
    return list(filter((lambda x: x.get("name") == class_name), LIST_OF_CLASSES()))[0]


def enumerate_list_options(choices: list) -> str:
    """
    Prints each element in choices and gets player to choose one.
    This function will be used to get all player choices in the game.

    :param choices: list
    :precondition: choices are a list of valid options as strings
    :postcondition: Shows player all elements in choices, with a number corresponding to it
                    gets player input
                    validates player input as an option we displayed
                    returns the element in choice player chose
    :return: string
    """
    while True:
        timed_print("Pick an option!", 1)
        for count, value in enumerate(choices):
            timed_print(f"{count + 1}.  {value}", 0.5)
        choice = input("")
        was_input_quit(choice)
        try:
            if int(choice) - 1 in range(len(choices)):
                return choices[int(choice) - 1]
            else:
                timed_print("Please pick a valid number from below :/", 1)
        except ValueError:
            timed_print("Please pick a valid number from below:/")


def was_input_quit(input_string: str):
    """
    Checks if input is quit, if it is exit program.

    :param input_string: string
    :precondition:  input_string is a string
    :postcondition: checks if input is "quit"
                    if it is exit program
    >>> was_input_quit("north")
    """
    if input_string == "quit":
        exit("You have quit the game \n Thanks for playing")


def roll_dice(number_of_rolls: int, sides_of_dice: int) -> int:
    """
    Simulates a XdY format of dice roll.
    X is the number of rolls.
    Y is the number of faces on the dice.

    :param number_of_rolls: integer
    :param sides_of_dice: integer
    :precondition: number_of_rolls is a positive non zero int
                    sides_of_dice is a positive non zero int
    :postcondition: randomly generates number_of_rolls amount of integers in range of 1 to sides_of_dice
                    sums all the numbers
                    returns that sum
    :return: integer
    >>> roll_dice(1, 6) >= 1
    True
    """
    sum_of_rolls = 0
    for roll in range(number_of_rolls):
        sum_of_rolls += random.randint(1, sides_of_dice)
    return sum_of_rolls


def make_italic(string: str) -> str:
    """
     Returns string with ansi escape sequence for italics

    :param string: string
    :precondition: string is a string
    :postcondition: adds formatting to string
    :return: string

    >>> test = make_italic("Hello")
    >>> test == "\x1B[3mHello\x1B[23m"
    True
    """
    return f"\x1B[3m{string}\x1B[23m"


def make_bold(string: str) -> str:
    """
    Returns string with ansi escape sequence for bolding.

    :param string: string
    :precondition: string is a string
    :postcondition: adds formatting to string
    :return: string

    >>> test = make_bold("Hello")
    >>> test == "\033[1mHello\033[0m"
    True
    """
    return f"\033[1m{string}\033[0m"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END UTILITY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def monster_cycle_creator() -> dict:
    """Returns dictionary where keys are zones and values are itertools cycles."""
    monster_dictionary = {"ellinia": itertools.cycle(list(filter((lambda x: "ellinia" in x.get("zones")),
                                                                 LIST_OF_DICTIONARY_MONSTERS_CONSTANT()))),
                          "kerning": itertools.cycle(list(filter((lambda x: "kerning" in x.get("zones")),
                                                                 LIST_OF_DICTIONARY_MONSTERS_CONSTANT()))),
                          "perion": itertools.cycle(list(filter((lambda x: "perion" in x.get("zones")),
                                                                LIST_OF_DICTIONARY_MONSTERS_CONSTANT()))),
                          "henesys": itertools.cycle(list(filter((lambda x: "henesys" in x.get("zones")),
                                                                 LIST_OF_DICTIONARY_MONSTERS_CONSTANT()))),
                          "sleepy wood": itertools.cycle(list(filter((lambda x: "sleepy wood" in x.get("zones")),
                                                                     LIST_OF_DICTIONARY_MONSTERS_CONSTANT())))}
    return monster_dictionary


def game_state():
    """
    Initiates and controls the game state for our game.

    game_state manages variables as well as makes sures appropriate functions are called.
    :postcondition:
    """

    player_character = intro()
    monster_cycle = monster_cycle_creator()
    while True:
        story_time(player_character)
        if player_character["active"]:
            combat(player_character, monster_cycle)
            if is_player_dead(player_character):
                player_died()
        movement(player_character)


def main():
    """Drives the program."""
    doctest.testmod(verbose=False)
    game_state()


if __name__ == '__main__':
    main()
