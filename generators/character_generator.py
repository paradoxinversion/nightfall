import tcod as libtcod
from entity import Entity
from components.fighter import Fighter, Attack
from attack_definitions import attack_definitions
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.character import Character
from components.race import Race
from render_functions import RenderOrder
from race_templates import race_templates
from random import randint


def generate_character(race):
    """Generates a random character of the chosen race"""

    race_template = race_templates[race]
    base_stat_min = race_template["base_stat_min"]
    base_stat_max = race_template["base_stat_max"]
    age_min = race_template["age_min"]
    age_max = race_template["age_max"]

    age = randint(age_min, age_max)
    defense = randint(base_stat_min, base_stat_max)
    power = randint(base_stat_min, base_stat_max)
    hp = 10 * (defense * power)
    race_component = Race(race_template)
    character_component = Character(race_component, age)

    attacks = []
    for key, value in attack_definitions.items():
        print(key)
        print(value)
        attack = Attack(
            value["name"],
            value["attack_description"],
            value["hit_description"],
            value["damage_type"],
            value["is_melee_attack"],
            value["is_weapon_attack"])
        attacks.append(attack)

    fighter_component = Fighter(
        hp=hp, defense=defense, power=power, known_attacks=attacks)
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()
    character = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                       fighter=fighter_component, inventory=inventory_component, level=level_component, equipment=equipment_component, character=character_component)
    return character
