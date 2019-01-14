from random import randint
from time import monotonic
from .unit import Unit


@Unit.register('Soldier')
class Soldier(Unit):

    def __init__(self, health=100):
        self.recharge = randint(100, 2000)
        self.health = health
        self.zero_time = 0
        self.exp = 0

    def recharger(self):
        if (self.zero_time + self.recharge) <= monotonic() * 1000:
            return True
        else:
            return False

    def level_up(self):
        if self.exp != 50:
            self.exp += 1
            return self.exp
        else:
            return self.exp

    def is_attack(self):
        calc_chance = 0.5 * (1 + self.health / 100) * \
            randint((50 + self.exp), 100) / 100
        return round(calc_chance, 2)

    def damage(self):
        if self.recharger() == True:
            calc_damage = 0.05 + self.exp / 100
            self.zero_time = monotonic() * 1000
            self.level_up()
            return round(calc_damage, 2)
        else:
            return 0

    def damage_rank(self):
        damage_calc = 0.05 + self.exp / 100
        return round(damage_calc, 2)

    def take_damage(self, damage_enemy):
        if self.is_active() == True:
            self.health -= round(damage_enemy, 2)
        return self.health

    def is_active(self):
        if self.health <= 0:
            return False
        else:
            return True

    def __call__(self):
        return 'Soldier'

    def __str__(self):
        return 'Soldier: health={0}, recharge={1}, exp={2}, damage_rank={3}\n'.format(
            self.health,
            self.recharge,
            self.exp,
            self.damage_rank())
