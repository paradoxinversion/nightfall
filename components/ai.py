import tcod as libtcod
from random import randint
from game_messages import Message


class NeutralAI:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        actor = self.owner
        if actor.fighter.attacked_last_tick:
            if actor.fighter.last_attacker is not None:
                self.owner.set_ai(HostileAI())
        return results


class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)
            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)
        return results


class HostileAI:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        actor = self.owner
        if actor.fighter.last_attacker:
            target = actor.fighter.last_attacker
        if libtcod.map_is_in_fov(fov_map, actor.x, actor.y):
            if actor.distance_to(target) >= 2:
                actor.move_astar(target, entities, game_map)
            elif target.fighter.hp > 0:
                attack_results = actor.fighter.attack(target)
                results.extend(attack_results)
        return results


class ExhaustedAI:
    def take_turn(self):
        results = []
        actor = self.owner
        results.append(
            {"message": Message('{0} is exhausted!'.format(actor.name), libtcod.red)})
        return results


class ConfusedMonster:
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        if self.number_of_turns > 0:
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1

            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)

            self.number_of_turns -= 1
        else:
            self.owner.ai = self.previous_ai
            results.append({'message': Message(
                'The {0} is no longer confused!'.format(self.owner.name), libtcod.red)})

        return results
