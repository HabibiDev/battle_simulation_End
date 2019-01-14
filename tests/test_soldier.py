import unittest
from time import monotonic, sleep
from models.units.soldier import Soldier


class TestSoldier(unittest.TestCase):

    def test_is_active(self):
        unit = Soldier()
        unit.take_damage(100)
        self.assertFalse(unit.is_active())

    def test_recharger_and_damage(self):
        unit = Soldier()
        unit.recharge = 500
        unit.zero_time = monotonic() * 1000
        sleep(0.25)
        self.assertFalse(unit.recharger())
        self.assertEqual(unit.damage(), 0)
        sleep(0.25)
        self.assertTrue(unit.recharger())
        self.assertEqual(unit.damage(), 0.05)
        sleep(0.5)
        self.assertEqual(unit.damage(), 0.06)

    def test_level_up(self):
        unit = Soldier()
        unit.damage()
        self.assertEqual(unit.level_up(), 2)
        for i in range(100):
            unit.level_up()
        self.assertEqual(unit.level_up(), 50)

    def test_take_damage(self):
        unit = Soldier()
        self.assertEqual(unit.take_damage(50), 50)
        unit.health = 0
        self.assertEqual(unit.take_damage(100), 0)

    def test_damage_rank(self):
        unit = Soldier()
        self.assertEqual(unit.damage_rank(), 0.05)
        for i in range(1, 51):
            unit.level_up()
            self.assertEqual(unit.damage_rank(), round(0.05 + i / 100, 2))
