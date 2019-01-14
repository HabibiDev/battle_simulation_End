import unittest
from time import monotonic, sleep
from random import choice
from models.squad import Squad
from models.units.soldier import Soldier
from models.units.vehicle import Vehicle


class TestSquad(unittest.TestCase):

    def test_is_active_and_take_damage(self):
        units = [choice([Soldier(), Vehicle()]) for i in range(5, 11)]
        unit = Squad(units)
        unit.take_damage(100 * len(unit.units))
        vehicle_bool = False
        for i in unit.units:
            if str(i()).startswith('Vehicle'):
                vehicle_bool = True
        if vehicle_bool == True:
            self.assertTrue(unit.is_active())
            unit.take_damage(66.7 * len(unit.units))
            self.assertFalse(unit.is_active())
        else:
            self.assertFalse(unit.is_active())

    def test_damage_and_take_damage(self):
        units = [choice([Soldier(), Vehicle()]) for i in range(5, 11)]
        unit = Squad(units)
        self.assertEqual(unit.damage_rank(), round(0.05 * len(unit.units), 2))
        self.assertEqual(unit.damage(), round(0.05 * len(unit.units), 2))
        sleep(2)
        for comb_unit in unit.units:
            comb_unit.level_up()
        self.assertGreater(unit.damage_rank(),
                           round(0.05 * len(unit.units), 2))
        self.assertGreater(unit.damage(), round(0.05 * len(unit.units), 2))
