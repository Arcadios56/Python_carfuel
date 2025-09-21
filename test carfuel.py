import unittest
from carfuel import Carfuel

class TestCarfuel(unittest.TestCase):
    def startCar(self):
        self.car = Carfuel(10.0)

    def test_start_with_no_fuel(self):
        self.assertFalse(self.car.start())
        self.assertFalse(self.car.is_running)
        self.assertEqual(self.car.fuel_level, 0.0)

    def test_start_with_fuel(self):
        self.car.refuel(10.0)
        self.assertTrue(self.car.start())
        self.assertTrue(self.car.is_running)
        self.assertEqual(self.car.fuel_level, 10.0)

    def test_start_already_in_ignition(self):
        self.car.refuel(10.0)
        self.car.start()
        self.assertFalse(self.car.start())  # Should not start again
        self.assertTrue(self.car.is_running)  # Should remain running
        self.assertEqual(self.car.fuel_level, 10.0)

    def test_stop_car(self):
        self.car.refuel(10.0)
        self.car.start()
        self.car.stop()
        self.assertFalse(self.car.is_running)
        self.assertEqual(self.car.fuel_level, 10.0)