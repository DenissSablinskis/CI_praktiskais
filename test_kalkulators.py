import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):
    def test_saskaitit_5_10(self):
        self.assertEqual(saskaitit(5, 10), 15)
    
    def test_saskaitit_10_20(self):
        self.assertEqual(saskaitit(10, 20), 30)
    
    def test_saskaitit_2_3(self):
        self.assertEqual(saskaitit(2, 3), 4)

    def test_saskaitit_8_10(self):
        self.assertEqual(saskaitit(8, 10), 18)

if __name__ == '__main__':
    unittest.main()