import csv
import json


class LibConverter:

    @staticmethod
    def read_data(file_name):
        with open(file_name) as csvfile:
            csvreader = csv.reader(csvfile)
            title = next(csvreader)
            data = []
            for row in csvreader:
                data.append(row)

        return title, data

    @staticmethod
    def convert_csv_to_json(title, data):

        prepared_data = []
        for row in data:
            prepared_data.append(dict(zip(title, row)))

        json_object = json.dumps(prepared_data,indent=len(prepared_data))

        return json_object

    @staticmethod
    def write_data(file_name, data):

        with open(file_name,'w') as outfile:
            outfile.write(data)



