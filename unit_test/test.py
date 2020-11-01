import unittest
from validation import Validator

class test_validator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_reject_if_month_nonexisting(self):
        # assume
        month = '15'

        # action
        result = self.validator.month_is_valid(month)

        # assert
        self.assertFalse(result)

    def test_reject_if_quarter_nonexisting(self):
        # assume
        quarter = '15'

        # action
        result = self.validator.month_is_valid(quarter)

        # assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
