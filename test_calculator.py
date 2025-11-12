#https://github.com/DiegoCanas07/lab11-DC-EY.git
#Partner 1: Diego Canas
#Partner 2: Ethan Yin
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-5, 5), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(4, 10), -6)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(5, 0), 0)
        self.assertEqual(calculator.mul(-2,3), -6)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(a=2, b=4), 0.5)
        self.assertAlmostEqual(calculator.div(a=4, b=1), 4.0)
        self.assertAlmostEqual(calculator.div(a=1, b=-4), -0.25)
    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.logarithm(4, 1024), 5.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -4)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)


    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5.0)


    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)



# Do not touch this
if __name__ == "__main__":
    unittest.main()