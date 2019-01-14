from random import randint
from time import monotonic
from .unit import Unit
from .soldier import Soldier


@Unit.register('Vehicle')
class Vehicle(Unit):

    def __init__(self, health=100):
        self.operators = [Soldier() for i in range(randint(1, 4))]
        self.recharge = randint(1000, 2000)
        self.health = health
        self.zero_time = 0
        self.exp = 0
        self.rank_vehicle = 0

    def recharger(self):
        if (self.zero_time + self.recharge) <= monotonic() * 1000:
            return True
        else:
            return False

    def is_active(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, damage_enemy):
        if self.is_active() == True:
            self.health -= 0.6 * damage_enemy
            lucky_operator_number = randint(0, len(self.operators) - 1)
            if len(self.operators) != 0:
                for i in range(len(self.operators)):
                    if i != lucky_operator_number:
                        if self.operators[i].is_active() == True:
                            self.operators[i].take_damage(0.1 * damage_enemy)
            if self.operators[lucky_operator_number].is_active() == True:
                self.operators[lucky_operator_number].take_damage(
                    0.2 * damage_enemy)
        return self.health

    def level_up(self):
        for oper in self.operators:
            oper.level_up()
        self.exp = sum([i.exp for i in self.operators])
        return self.exp

    def is_attack(self):
        gavg = 1
        for attack in self.operators:
            gavg *= attack.is_attack()
        gavg = gavg ** (1 / len(self.operators))
        calc_chance = 0.5 * (1 + self.health / 100) * gavg
        return calc_chance

    def damage(self):
        if self.recharger() == True:
            operators_exp = [i.exp for i in self.operators]
            calc_damage = 0.05 + sum(operators_exp) / 100
            self.zero_time = monotonic() * 1000
            self.level_up()
            return round(calc_damage, 2)
        else:
            return 0

    def damage_rank(self):
        operators_exp = [i.exp for i in self.operators]
        damage_calc = 0.05 + sum(operators_exp) / 100
        return round(damage_calc, 2)

    def __call__(self):
        return 'Vehicle'

    def __str__(self):
        return '\nVehicle: health={0}, recharge={1}, exp={2}, damage_rank={3}, Operators:{4}\nOperators:\n{5}\n'.format(
            self.health,
            self.recharge,
            self.exp,
            self.damage_rank(),
            len(self.operators),
            ''.join(map(str, self.operators)))
