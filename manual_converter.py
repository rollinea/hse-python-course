class ManualCsvConverter:

    def __init__(self, scv_data):
        self.title = scv_data[0]
        self.values = scv_data[1:]

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        return values

    def convert_row_to_json(self, data):
        formatted_values = ",".join([""""{}": {}""".format(key, value) for key, value in data.items()])
        pretty_line = """{{ {} }}""".format(formatted_values)
        return pretty_line

    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        return "[{}]".format(",".join(result))
