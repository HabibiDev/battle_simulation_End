import logging
from random import choice
from .units.soldier import Soldier
from .units.vehicle import Vehicle
from .squad import Squad


def sortedlist(mylist):
    return str(mylist)


class Army:

    def __init__(self, squads, number):
        self.armies = []
        self.squads = squads
        self.squads_list = []
        self.choose_army = None
        self.number = number
        self.rank = 0

    def create_army(self, log_info=logging):
        for squad in range(self.squads):
            units_list = [choice([Soldier(), Vehicle()]) for i in range(5, 11)]
            units_list.sort(key=sortedlist)
            self.squads_list.append(Squad(units_list))
            log_info.info('Squad_{0}:\n\nUnits:\n{1}\n\n'.format(
                squad, ''.join(map(str, units_list))))
        return self.squads_list

    def is_attack(self):
        calc_chance = 0
        for squad in self.squads_list:
            calc_chance += squad.is_attack()
        return calc_chance

    def is_active(self):
        army_active = False
        for squad in self.squads_list:
            if squad.is_active() == True:
                army_active = True
            else:
                self.squads_list.remove(squad)
        return army_active

    def damage(self):
        damage_calc = 0
        for squad in self.squads_list:
            damage_calc += squad.damage()
        return round(damage_calc, 2)

    def choose_strategy(self):
        my_strategy = choice(['random', 'weakest', 'strongest'])
        if my_strategy == 'random':
            self.choose_army = choice(self.armies)
        elif my_strategy == 'weakest':
            rank = choice(self.armies).damage_rank()
            for army in self.armies:
                if rank > army.damage_rank():
                    rank = army.damage_rank()
                    self.choose_army = army
                else:
                    self.choose_army = army
        elif my_strategy == 'strongest':
            rank = choice(self.armies).damage_rank()
            for army in self.armies:
                if rank < army.damage_rank():
                    rank = army.damage_rank()
                    self.choose_army = army
                else:
                    self.choose_army = army
        return self.choose_army

    def take_damage(self, army_damage):
        for squad in self.squads_list:
            squad.take_damage(army_damage / len(self.squads_list))

    def attack_success(self, army_attack, damage):
        if self.is_attack() < army_attack.is_attack():
            self.take_damage(damage)

    def damage_rank(self):
        for squad in self.squads_list:
            self.rank += squad.damage_rank()
        return round(self.rank, 2)

    def __str__(self):
        return 'Army_{0}'.format(self.number)
