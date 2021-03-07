import unittest
import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizz_buzz.FizzBuzz(3), "Fizz")
        self.assertEqual(fizz_buzz.FizzBuzz(5), "Buzz")
        self.assertEqual(fizz_buzz.FizzBuzz(15), "FizzBuzz")
        
if __name__ == '__main__':
    unittest.main()