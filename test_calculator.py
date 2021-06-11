import unittest, json
from loan_calculator import Loan

# Testing class to run test on the Loan Calculator
class CalculatorTest(unittest.TestCase):
    def test_total_payment(self):
        Total = 100000
        Downpayment = 20000
        rate = 5.5
        term = 30
        # declaring the results variable to compare to the test
        expected_result = {
            "monthly_payment": 454.23,
            "total_interest": 83523.23,
            "total_payment": 163523.23
        }
        # using json.dump to make the result variable as close to the payment calculator result
        json_result = json.dumps(expected_result)

        test_result = Loan(Total, Downpayment, rate, term).totalPayment()

        self.assertEqual(test_result, json_result)

# unittest.main executes an object of test program. No need to contain a main function in testing file
if __name__ == '__main__':
    unittest.main()
