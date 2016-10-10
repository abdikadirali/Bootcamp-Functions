import unittest

import fib

class TestFib(unittest.TestCase):
    
    fib = staticmethod(fib.fib1)

    def test(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)
        self.assertEqual(self.fib(2), 1)
        self.assertEqual(self.fib(3), 2)
        self.assertEqual(self.fib(4), 3)
        self.assertEqual(self.fib(5), 5)

# This boilerplate allows us to run using unittest.
if __name__ == '__main__':
    unittest.main()