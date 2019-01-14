class Squad:

    def __init__(self, units):
        self.units = units
        self.rank = 0

    def is_active(self):
        squad_active = False
        for unit in self.units:
            if unit.is_active() == True:
                squad_active = True
        return squad_active

    def is_attack(self):
        gavg = 1
        for unit in self.units:
            gavg *= unit.is_attack()
        gavg = gavg ** (1 / len(self.units))
        calc_chance = 0.5 * (1 + unit.health / 100) * gavg
        return calc_chance

    def damage(self):
        calc_damage = 0
        for unit in self.units:
            if unit.is_active() == True:
                calc_damage += unit.damage()
        return round(calc_damage, 2)

    def damage_rank(self):
        calc_rank = 0
        for unit in self.units:
            if unit.is_active() == True:
                calc_rank += unit.damage_rank()
        return round(calc_rank, 2)

    def take_damage(self, damage_squad):
        for unit in self.units:
            unit.take_damage(damage_squad / len(self.units))

    def __str__(self):
        return 'Squad:\n Units:{0}\n'.format(self.units)
