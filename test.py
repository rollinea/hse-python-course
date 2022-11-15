import unittest
from manual_converter_from_csv_to_json import ManConverter
from library_converter import LibConverter


def manual_convert(file_name):
    data = ManConverter.read_data(file_name)
    title, rows = ManConverter.prepare_data(data)
    print(title)
    result = ManConverter.convert_csv_to_json(title, rows)
    ManConverter.write_data('output_1.json', result)


def convert_with_libraries(file_name):
    title, data = LibConverter.read_data(file_name)
    json_data = LibConverter.convert_csv_to_json(title, data)
    LibConverter.write_data('output_2.json', json_data)


# manual_convert('data.csv')
# convert_with_libraries('data.csv')

class TestManual(unittest.TestCase):

    data = ManConverter.read_data('data.csv')
    title, rows = ManConverter.prepare_data(data)

    def test_title(self):

        self.assertEqual(TestManual.title, ['id', 'name', 'birth', 'salary', 'department'])

    def test_title_empty_data(self):

        self.assertEqual(TestManual.title, ['id', 'name', 'birth', 'salary', 'department'])
        self.assertEqual(TestManual.rows, [])

    def test_data_with_None(self):

        self.assertEqual(TestManual.rows[1],'2,Alex,,200000,5\n')

    def test_data(self):

        self.assertEqual(TestManual.rows,['1,Ivan,1980,150000,1\n', '2,Alex,,200000,5\n', '3,Ivan,,130000,8'])




