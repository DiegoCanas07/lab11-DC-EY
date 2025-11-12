import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(5, 0), 0)
        self.assertEqual(calculator.mul(-2,3), -6)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(calculator.div(2,4),2)
        self.assertAlmostEqual(calculator.div(4, 1), 0.25)
        self.assertAlmostEqual(calculator.div(1, -4), -4)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)
        with self.assertRaises(ValueError):
            calculator.log(2, -4)
        with self.assertRaises(ValueError):
            calculator.log(0, 5)


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