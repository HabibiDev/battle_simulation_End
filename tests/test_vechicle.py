import unittest
from time import monotonic, sleep
from models.units.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def test_is_active(self):
        unit = Vehicle()
        unit.take_damage(100)
        self.assertTrue(unit.is_active())
        unit.take_damage(66.7)
        self.assertFalse(unit.is_active())

    def test_recharger_and_damage(self):
        unit = Vehicle()
        unit.recharge = 1500
        unit.zero_time = monotonic() * 1000
        sleep(0.75)
        self.assertFalse(unit.recharger())
        self.assertEqual(unit.damage(), 0)
        sleep(0.75)
        self.assertTrue(unit.recharger())
        self.assertEqual(unit.damage(), 0.05)
        sleep(1.5)
        self.assertEqual(unit.damage(), round(
            0.05 + len(unit.operators) / 100, 2))

    def test_level_up(self):
        unit = Vehicle()
        unit.damage()
        for oper in unit.operators:
            self.assertEqual(oper.level_up(), 2)
        for i in range(100):
            unit.level_up()
        for oper in unit.operators:
            self.assertEqual(oper.level_up(), 50)

    def test_take_damage(self):
        unit = Vehicle()
        self.assertEqual(unit.take_damage(100), 40)
        for oper in unit.operators:
            self.assertNotEqual(oper.health, 100)
        unit.health = 0
        self.assertEqual(unit.take_damage(100), 0)
        unit.health = 1
        unit.take_damage(1000)
        for oper in unit.operators:
            self.assertFalse(oper.is_active())

    def test_damage_rank(self):
        unit = Vehicle()
        self.assertEqual(unit.damage_rank(), 0.05)
        for i in range(1, 51):
            unit.level_up()
            self.assertEqual(unit.damage_rank(), round(
                0.05 + (i * len(unit.operators)) / 100, 2))
        for i in range(51, 100):
            unit.level_up()
            self.assertNotEqual(unit.damage_rank(), round(
                0.05 + (i * len(unit.operators)) / 100, 2))
