import unittest
import cache

class TestCache(unittest.TestCase):

    def test_create_city_cache(self):
        cache.create_city_cache("Campinas")
        self.assertEqual("Campinas", cache.read_city_cache())




if __name__ == "__main__":
    unittest.main()