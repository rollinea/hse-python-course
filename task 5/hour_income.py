import json
import random


class GetHourIncome:

    def __init__(self, file_name):
        self.file_name = file_name
        self.json_data = []

    def read_json(self):
        f = open(self.file_name, 'r')
        self.string_data = f.readlines()
        f.close()
        self.json_data = [json.loads(string) for string in self.string_data]

    def write_data(self, file_name):
        f = open(file_name, 'w')
        f.write('[')
        data = [json.dumps(employee, indent=len(employee)) for employee in self.json_data]
        f.write(',\n'.join(data))
        f.write(']')
        f.close()

    def get_the_number_of_days(self, year, month):
        return random.randint(20, 23)

    def hour_income(self, salary, days):
        return float('%.2f' % round(salary / (days * 8), 2))

    def update_json(self, id_):
        employee = self.json_data[id_]
        working_days = self.get_the_number_of_days(employee['year'], employee['month'])
        employee['hour_income'] = self.hour_income(employee['salary'], working_days)

    def update_all_employees(self):
        self.read_json()
        for id_ in range(len(self.json_data)):
            self.update_json(id_)
        self.write_data('output.json')
