import unittest
import leap_year

class TestLeap(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leap_year.IsLeap(2000), True)
        self.assertEqual(leap_year.IsLeap(1943), False)
        self.assertEqual(leap_year.IsLeap(400), True)
        self.assertEqual(leap_year.IsLeap(401), False)

if __name__ == "__main__":
    unittest.main()