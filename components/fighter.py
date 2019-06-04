import tcod as libtcod

from game_messages import Message

basic_skills = [
    {'skill': 'fighting', 'rank': .9, 'logged_rank': 0},
    {'skill': 'dodging', 'rank': 0, 'logged_rank': 0}
]


class Fighter:
    def __init__(self, hp, defense, power, xp=0, known_attacks=[]):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp
        self.skils = basic_skills
        self.known_attacks = known_attacks

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    def take_damage(self, amount):
        results = []
        self.hp -= amount
        if self.hp <= 0:
            results.append({"dead": self.owner, 'xp': self.xp})
        return results

    def attack(self, target):
        results = []
        damage = self.power - target.fighter.defense
        if damage > 0:
            results.append({"message": Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({"message": Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})
        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Attack(object):
    def __init__(self, name,  attack_description, hit_description, damage_type, is_melee_attack, is_weapon_attack):
        self.name = name
        self.attack_desc = attack_description
        self.hit_desc = hit_description
        self.damage_type = damage_type
        self.is_melee_attack = is_melee_attack
        self.is_weapon_attack = is_weapon_attack
