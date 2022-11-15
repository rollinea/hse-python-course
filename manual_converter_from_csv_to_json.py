class ManConverter:

    @staticmethod
    def read_data(file_name):
        file = open(file_name)
        content = file.readlines()
        file.close()
        return content

    @staticmethod
    def write_data(file_name, data):
        file = open(file_name, 'w')
        file.write(data)
        file.close()

    @staticmethod
    def prepare_data(data):
        title = data.pop(0).strip().split(',')
        return title, data

    @staticmethod
    def convert_row_to_pretty_json(keys, row):
        values = row.strip().split(',')
        d = dict(zip(keys, values))

        return """ {{
      "id": "{}",
      "name": "{}",
      "birth": "{}",
      "salary": "{}",
      "department": "{}"
   }}""".format(*d.values())

    @staticmethod
    def convert_csv_to_json(title, data):
        result = "[\n"
        for i in range(len(data)):
            result += f'  {ManConverter.convert_row_to_pretty_json(title, data[i])},\n'
        result = result[:(len(result) - 2)]
        result += '\n]'

        return str(result)
