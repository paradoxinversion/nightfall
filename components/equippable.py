class Equippable:
    """Represents an equippable item that can be put on/held or taken off/dropped, unless
    it is for some reason forced to remain (such as curse effects, natural weapons/armor/etc)"""

    def __init__(self, slot, attack_bonus=0, damage_bonus=0, defense_bonus=0, strength_bonus=0, max_hp_bonus=0, attacks=[], stamina_use=0):
        self.slot = slot
        self.attack_bonus = attack_bonus
        self.damage_bonus = damage_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.strength_bonus = strength_bonus
        self.equippable_attacks = attacks
        self.stamina_use = stamina_use
