import unittest
from hour_income import GetHourIncome


class TestHourIncome(unittest.TestCase):
    def setUp(self):
        self.program = GetHourIncome('input.json')

    def test_get_number_of_days(self):
        result = self.program.get_the_number_of_days('2020', 'JUNE')

        self.assertTrue(20 <= result and result <= 23)

    def test_calc_hour_income(self):
        days = 21
        salary = 150000
        expected = 892.86
        self.assertEqual(expected, self.program.hour_income(salary, 21))

    def test_update_json(self):
        self.program.json_data.append({"year": 2016, "month": "JANUARY", "salary": 1000000})
        self.program.update_json(0)
        self.assertIn("hour_income", self.program.json_data[0])
