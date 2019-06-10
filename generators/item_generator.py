from generators.generator_helpers import generate_attack_set
from attack_definitions import blade_attack_definitions
from components.equippable import Equippable
from components.equipment import EquipmentSlots
from item_definitions import weapon_definitions
from entity import Entity
import tcod as libtcod


def generate_weapon_equippable(weapon_definition):
    """Generates a weapon"""
    attack_bonus = weapon_definition["attack_bonus"]
    damage_bonus = weapon_definition["base_damage"]
    equippable_component = Equippable(
        EquipmentSlots.MAIN_HAND, attack_bonus=attack_bonus, damage_bonus=damage_bonus, attacks=generate_attack_set(blade_attack_definitions))
    return equippable_component


def generate_weapon_from_template(template_name):
    weapon_definition = weapon_definitions[template_name]
    equippable_component = generate_weapon_equippable(weapon_definition)
    weapon_entity = Entity(0, 0, weapon_definition["display_character"], libtcod.sky, weapon_definition["name"],
                           equippable=equippable_component)
    return weapon_entity
