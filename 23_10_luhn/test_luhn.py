import unittest
from luhn import Luhn

class LuhnTest(unittest.TestCase):
    def setUp(self):
        cc_number = '4539 1488 0343 6467'
        self.luhn_instance = Luhn(cc_number)


    def test_clean_should_remove_spaces(self):
        self.luhn_instance.clean()

        self.assertEqual(self.luhn_instance.cc_number, '4539148803436467')

    
    def test_clean_should_remove_hyphen(self):
        cc_number_hyphen = '4539-1488-0343-6467'
        luhn_instance = Luhn(cc_number_hyphen)
        luhn_instance.clean()

        self.assertEqual(luhn_instance.cc_number, '4539148803436467')


    def test_check_selection_seconds_digits(self):
        self.luhn_instance.clean()
        self.luhn_instance.select_digits()

        self.assertEqual(self.luhn_instance.seconds, [6, 6, 4, 0, 8, 1, 3, 4])


    def test_check_selection_firsts_digits(self):
        self.luhn_instance.clean()
        self.luhn_instance.select_digits()

        self.assertEqual(self.luhn_instance.firsts, [7, 4, 3, 3, 8, 4, 9, 5])


    def test_multiply_by_two_should_subtract_nine_if_greater_than_nine(self):
        self.luhn_instance.clean()
        self.luhn_instance.select_digits()
        self.luhn_instance.double_seconds()

        self.assertEqual(self.luhn_instance.seconds, [3, 3, 8, 0, 7, 2, 6, 8])


    def test_check_should_pass_if_valid_number(self):
        is_valid = self.luhn_instance.check()
        
        self.assertEqual(is_valid, True)


    def test_check_should_pass_if_invalid_number(self):
        cc_number = '8273 1232 7352 0569'
        luhn_instance = Luhn(cc_number)
        is_valid = luhn_instance.check()
        
        self.assertEqual(is_valid, False)


if __name__ == "__main__":
    unittest.main()