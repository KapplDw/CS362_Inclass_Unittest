import unittest
import calc



class calcTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 11), 16)
        self.assertEqual(calculator.add(9,10), 21)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 0), 5)
        self.assertEqual(calculator.subtract(5, 1), 4)
    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 10), 50)
        self.assertEqual(calculator.multiply(3, 1), 6)
        
    def test_divide(self):
        self.assertEqual(calculator.divide(5, 10), .5)
        self.assertEqual(calculator.divide(12, 6), 2)
        




#if __name__ == '__main__':
    #unittest.main()