import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #Add
    def test_add1(self):
        self.assertEqual(self.calc.add(-2,-7),-9)

    def test_add2(self):
        self.assertEqual(self.calc.add(10,-8),2)

    #Subtract
    def test_sub1(self):
        self.assertEqual(self.calc.subtract(10.5, 5), 5.5)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(8, 5), 3)

    #Multiply
    def test_mul1(self):
        self.assertEqual(self.calc.multiply(4.5,38), 171)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply(10, -9), -90)

    #Divide
    def test_div1(self):
        self.assertEqual(self.calc.divide(25, 5), 5)

    def test_div2(self):
        self.assertEqual(self.calc.divide(0, 8), 0)

    #Modulo
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(50, 3), 2)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)
    

if __name__ == '__main__':
    unittest.main()