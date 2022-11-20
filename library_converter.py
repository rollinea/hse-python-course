import json
import csv


class LibraryCsvConverter:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        with open(self.file_name) as csvf:
            csvReader = csv.DictReader(csvf)
            data = [row for row in csvReader]

        return data

    def to_json(self):
        data = self.read_data()
        json_object = json.dumps(data, indent=len(data[0]))

        return json_object
