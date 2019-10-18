import unittest


class Pling:
    @staticmethod
    def check(number):
        if number % 3 == 0:
            return "Pling"
        else:
            return ""


class Plang:
    @staticmethod
    def check(number):
        if number % 5 == 0:
            return "Plang"
        else:
            return ""


class Plong:
    @staticmethod
    def check(number):
        if number % 7 == 0:
            return "Plong"
        else:
            return ""


class PlingPlangPlong():
    @staticmethod
    def check(number):
        result = Pling.check(number) + Plang.check(number) + Plong.check(number)

        return result or str(number)




class PlingTest(unittest.TestCase):
    def test_pling_primitive_successful(self):
        number = 3
        result = PlingPlangPlong.check(number)

        self.assertEqual("Pling", result)

    def test_pling_not_divisible(self):
        number = 5
        result = PlingPlangPlong.check(number)

        self.assertNotEqual("Pling", result)
    
    def test_pling_divisible(self):
        number = 6
        result = PlingPlangPlong.check(number)

        self.assertEqual("Pling", result)  


class PlangTest(unittest.TestCase):
    def test_plang_primitive_successful(self):
        number = 5
        result = PlingPlangPlong.check(number)

        self.assertEqual("Plang", result)

    def test_plang_not_divisible(self):
        number = 13
        result = PlingPlangPlong.check(number)

        self.assertNotEqual("Plang", result)
    
    def test_plang_divisible(self):
        number = 10
        result = PlingPlangPlong.check(number)

        self.assertEqual("Plang", result)


class PlongTest(unittest.TestCase):
    def test_plong_primitive_successful(self):
        number = 7
        result = PlingPlangPlong.check(number)

        self.assertEqual("Plong", result)

    def test_plong_not_divisible(self):
        number = 13
        result = PlingPlangPlong.check(number)

        self.assertNotEqual("Plong", result)
    
    def test_plong_divisible(self):
        number = 14
        result = PlingPlangPlong.check(number)

        self.assertEqual("Plong", result)


class PlingPlangPlongTest(unittest.TestCase):
    def test_pling_plang_valid(self):
        number = 15
        result = PlingPlangPlong.check(number)

        self.assertEqual("PlingPlang", result)

    def test_pling_plong_valid(self):
        number = 21
        result = PlingPlangPlong.check(number)

        self.assertEqual("PlingPlong", result)

    def test_plang_plong_valid(self):
        number = 35
        result = PlingPlangPlong.check(number)

        self.assertEqual("PlangPlong", result)

    def test_not_pling_plang_plong(self):
        number = 1
        result = PlingPlangPlong.check(number)

        self.assertEqual(str(number), result)
    
        number = 52
        result = PlingPlangPlong.check(number)

        self.assertEqual(str(number), result)


if __name__ == "__main__":
    unittest.main()
