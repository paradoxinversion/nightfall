import tcod as libtcod

from game_messages import Message
from random import randint
basic_skills = [
    {'skill': 'fighting', 'rank': .9, 'logged_rank': 0},
    {'skill': 'dodging', 'rank': 0, 'logged_rank': 0}
]


class Fighter:
    def __init__(self, hp, endurance, strength, intelligence, willpower, xp=0, known_attacks=[]):
        self.base_max_hp = hp
        self.hp = hp
        self.base_endurance = endurance
        self.base_strength = strength
        self.base_intelligence = intelligence
        self.base_willpower = willpower

        self.xp = xp
        self.skils = basic_skills
        self.known_attacks = known_attacks
        self.owner = None
        self.is_hostile = False

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def strength(self):
        return self.base_strength + self.strength_modifier

    @property
    def strength_modifier(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.strength_bonus
        else:
            bonus = 0

        return bonus

    @property
    def endurance(self):
        return self.base_endurance + self.endurance_modifier

    @property
    def endurance_modifier(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return bonus

    @property
    def total_attack(self):
        total = int(self.attack_bonus)
        return total

    @property
    def attack_bonus(self):
        if self.owner and self.owner.equipment:
            attack_bonus = self.owner.equipment.attack_bonus
        else:
            attack_bonus = 0
        return attack_bonus

    @property
    def defense(self):
        return self.endurance

    def take_damage(self, amount):
        results = []
        self.hp -= amount
        if self.hp <= 0:
            results.append({"dead": self.owner, 'xp': self.xp})
        return results

    def attack(self, target, attack_type=None):
        is_unarmed = self.owner.equipment.main_hand == None

        if attack_type != None:
            atk_using = attack_type
        else:
            if is_unarmed:
                atk_using = self.known_attacks[randint(
                    0, len(self.known_attacks)-1)]
            else:
                atk_using = self.owner.equipment.main_hand.equippable.equippable_attacks[randint(
                    0, len(self.owner.equipment.main_hand.equippable.equippable_attacks)-1)]

        # Attack Contest
        print(self.owner.name, self.attack_bonus)
        attack_roll = randint(1, 10+self.total_attack)
        defense_roll = randint(1, 10+target.fighter.defense)

        results = []
        if (attack_roll > defense_roll):
            if self.owner and self.owner.equipment and self.owner.equipment.main_hand:
                weapon_damage = self.owner.equipment.main_hand.equippable.damage_bonus
            else:
                weapon_damage = 0
            damage = self.total_attack + weapon_damage - target.fighter.defense
            attack_msg = atk_using.hit_description.format(
                self.owner.name.capitalize(), target.name, str(damage))
            if damage > 0:
                results.append({"message": Message(attack_msg, libtcod.white)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({"message": Message('{0} attacks {1} but does no damage.'.format(
                    self.owner.name.capitalize(), target.name), libtcod.white)})
        else:
            results.append({"message": Message('{0} misses {1}!'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})
        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Attack(object):
    def __init__(self, name,  attack_description, hit_description, damage_type, is_melee_attack, is_weapon_attack):
        self.name = name
        self.attack_description = attack_description
        self.hit_description = hit_description
        self.damage_type = damage_type
        self.is_melee_attack = is_melee_attack
        self.is_weapon_attack = is_weapon_attack
