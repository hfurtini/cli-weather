import unittest
import unit_conversor

class TestConversor(unittest.TestCase):

    def test_kelvin_to_celsius(self):
        result = unit_conversor.kelvin_to_celsius(300)
        self.assertAlmostEqual(result, 26.9)

    def test_kelvin_to_fahrenheit(self):
        result = unit_conversor.kelvin_to_fahrenheit(300)
        self.assertAlmostEqual(result, 80.3)

if __name__ == "__main__":
    unittest.main()