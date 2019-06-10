import tcod as libtcod
from entity import Entity
from components.fighter import Fighter, Attack
from attack_definitions import unarmed_attack_definitions, blade_attack_definitions
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.character import Character
from render_functions import RenderOrder
from race_templates import race_templates
from random import randint
from components.ai import BasicMonster
from pprint import pprint
from generators.generator_helpers import generate_attack_set


def generate_attribute_values(race_template):
    base_attribute_min = race_template["base_attribute_min"]
    base_attribute_max = race_template["base_attribute_max"]
    age_min = race_template["age_min"]
    age_max = race_template["age_max"]

    age = randint(age_min, age_max)
    endurance = randint(base_attribute_min, base_attribute_max)
    strength = randint(base_attribute_min, base_attribute_max)
    hp = endurance * strength

    attributes = {
        "age": age,
        "endurance": endurance,
        "strength": strength,
        "hp": hp
    }
    return attributes


def generate_character(x, y, race, with_AI):
    """Generates a random character of the chosen race"""
    race_template = race_templates[race]
    attribute_values = generate_attribute_values(race_template)
    character_component = Character(attribute_values["age"], race_template)
    attacks = generate_attack_set(unarmed_attack_definitions)

    fighter_component = Fighter(
        hp=attribute_values["hp"], endurance=attribute_values["endurance"], strength=attribute_values["strength"], intelligence=1, willpower=1, known_attacks=attacks)
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()

    ai_component = None

    if with_AI:
        ai_component = BasicMonster()
        character_name = race_template["race_name"]
        color = libtcod.gray
    else:
        character_name = "Player"
        color = libtcod.orange

    character = Entity(x, y, '@', color, character_name, blocks=True, render_order=RenderOrder.ACTOR,
                       fighter=fighter_component, inventory=inventory_component, level=level_component,
                       equipment=equipment_component, character=character_component, ai=ai_component)
    return character
