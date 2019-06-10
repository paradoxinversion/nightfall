
from components.fighter import Attack


def generate_attack_set(attack_definition):
    """Generates an attack set (for equipment or other things) from an attack definition"""
    attacks = []

    for key, value in attack_definition.items():
        attack = Attack(
            value["name"],
            value["attack_description"],
            value["hit_description"],
            value["damage_type"],
            value["is_melee_attack"],
            value["is_weapon_attack"])
        attacks.append(attack)
    return attacks
