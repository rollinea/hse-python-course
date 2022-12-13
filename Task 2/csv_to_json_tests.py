import unittest
from manual_converter import ManualCsvConverter
from library_converter import LibraryCsvConverter


def read_data(file_name):
    f = open(file_name, 'r')
    data = f.readlines()
    f.close()
    return data


class TestManual(unittest.TestCase):

    def setUp(self):
        data = read_data('data.csv')
        self.converter = ManualCsvConverter(data)

    def test_prepare_title(self):
        expected = ['id', 'name', 'birth', 'salary', 'department']
        result = self.converter.prepare_title()
        self.assertEqual(result, expected)

    def test_prepare_row_values_empty_string(self):
        expected = ['']
        result = self.converter.prepare_row_values()
        self.assertEqual(result[0], expected)

    def test_prepare_row_values(self):
        expected = ['1', 'Ivan', '1980', '150000', '1']
        result = self.converter.prepare_row_values()
        self.assertEqual(result[1], expected)

    def test_prepare_row_values_with_empty_data(self):
        expected = ['2', 'Alex', '', '200000', '5']
        result = self.converter.prepare_row_values()
        self.assertEqual(result[2], expected)

    def test_convert_row_to_json(self):
        row = {'id': '1', 'name': 'Ivan', 'birth': '1980', 'salary': '150000', 'department': '1'}
        result = self.converter.convert_row_to_json(row)
        expected = '{ "id": 1,"name": Ivan,"birth": 1980,"salary": 150000,"department": 1 }'
        self.assertEqual(result, expected)

    def test_to_json(self):
        expected = '[{ "id": 1,"name": Ivan,"birth": 1980,"salary": 150000,"department": 1 },{ "id": 2,"name": Alex,"birth": ,"salary": 200000,"department": 5 },{ "id": 3,"name": Ivan,"birth": ,"salary": 130000,"department": 8 }]'
        result = self.converter.to_json()
        self.assertEqual(result, str(expected))

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.converter = LibraryCsvConverter('data.csv')

    def test_read_data(self):
        result = self.converter.read_data()
        expected = [{'id': '1', 'name': 'Ivan', 'birth': '1980', 'salary': '150000', 'department': '1'}, {'id': '2', 'name': 'Alex', 'birth': '', 'salary': '200000', 'department': '5'}, {'id': '3', 'name': 'Ivan', 'birth': '', 'salary': '130000', 'department': '8'}]
        self.assertEqual(result, expected)

    def test_to_json(self):
        result = self.converter.to_json()
        expected = """[
     {
          "id": "1",
          "name": "Ivan",
          "birth": "1980",
          "salary": "150000",
          "department": "1"
     },
     {
          "id": "2",
          "name": "Alex",
          "birth": "",
          "salary": "200000",
          "department": "5"
     },
     {
          "id": "3",
          "name": "Ivan",
          "birth": "",
          "salary": "130000",
          "department": "8"
     }
]"""
        self.assertEqual(result, expected)
