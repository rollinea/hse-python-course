import unittest
from md_converter_as_class import MdConverter


class TestMdConverter(unittest.TestCase):

    def setUp(self):
        self.converter = MdConverter()

    def test_prepare_titles(self):
        titles = '# title Merge\n# description Слияние двух отсортированных массивов в один'
        title, description = self.converter.prepare_titles(titles)
        self.converter.to_md()

        self.assertEqual(title, 'Merge')
        self.assertEqual(description, 'Слияние двух отсортированных массивов в один')

    def test_prepare_format(self):
        titles = '# title Merge\n# description Слияние двух отсортированных массивов в один'
        title, description = self.converter.prepare_titles(titles)
        source_code = '\ndef merge(first, second):\n    merged_list = []\n    i, j = 0, 0\n    while i < len(first) and j < len(first):\n        if first[i] < second[j]:\n            merged_list.append(first[i])\n            i += 1\n        else:\n            merged_list.append(second[j])\n            j += 1\n\n    while i < len(first):\n        merged_list.append(first[i])\n        i += 1\n\n    while j < len(second):\n        merged_list.append(second[j])\n        j += 1\n\n    return merged_list\n'
        head, template = self.converter.prepare_format(title, description, source_code)
        expected_head = '[Merge](#merge)\n'
        expected_tail = '\n## Merge\n### Слияние двух отсортированных массивов в один  \n```python\ndef merge(first, second):\n    merged_list = []\n    i, j = 0, 0\n    while i < len(first) and j < len(first):\n        if first[i] < second[j]:\n            merged_list.append(first[i])\n            i += 1\n        else:\n            merged_list.append(second[j])\n            j += 1\n\n    while i < len(first):\n        merged_list.append(first[i])\n        i += 1\n\n    while j < len(second):\n        merged_list.append(second[j])\n        j += 1\n\n    return merged_list\n\n```'

        self.assertEqual(head, expected_head)
        self.assertEqual(template, expected_tail)





