import unittest
from time import monotonic, sleep
from random import choice, randint
from models.squad import Squad
from models.army import Army
from models.units.soldier import Soldier
from models.units.vehicle import Vehicle


class TestSquad(unittest.TestCase):

    def test_create_army(self):
        for i in range(1, 50):
            unit = Army(i, 1)
            unit.create_army()
            for comb_unit in unit.squads_list:
                self.assertGreaterEqual(len(comb_unit.units), 5)
                self.assertLessEqual(len(comb_unit.units), 10)
            self.assertEqual(len(unit.squads_list), i)

    def test_is_active_and_take_damage(self):
        unit = Army(randint(2, 100), 1)
        unit.create_army()
        self.assertTrue(unit.is_active())
        unit.take_damage(166.7 * sum(
            [len(unit.squads_list[i].units) for i in range(unit.squads)]))
        self.assertFalse(unit.is_active())

    def test_damage_and_damage_rank(self):
        unit = Army(randint(2, 100), 1)
        unit.create_army()
        temp_damage_rank = unit.damage_rank()
        unit.damage()
        self.assertGreater(unit.damage_rank(), temp_damage_rank)
