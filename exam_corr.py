SEPARATOR = '-----'


class StrategyDeal:
    def __init__(self, *, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        return [round(target, 1) for target in self.targets]

    def get_target_percents(self):
        return [round((target / self.entry)*100-100, 3) for target in self.targets]

    def get_target_banks(self):
        return [round((self.bank / self.entry) * target, 3) for target in self.targets]

    def __str__(self):
        triplet = list(zip(self.get_targets(), self.get_target_percents(), self.get_target_banks()))
        head_template = """BANK: {}\nSTART_PRICE: {}\nSTOP_PRICE: {}\n\n""".format(self.bank, self.entry, self.close)
        targets_template = ["""{} target: {}\nPercent: {}\nBank: {}""".format(i, target, percent, bank) for i, (target, percent, bank) in enumerate(triplet, 1)]
        template = head_template + '\n\n'.join(targets_template)

        return template


def read_data(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    return (part.split('\n') for part in data.split(SEPARATOR))


def filter_data(data):
    return list(filter(None, data))


def prepare_data(data):
    d = {}
    for s in data:
        if s.startswith('Bank'):
            d['bank'] = int(s[6:].replace('USD', ''))
        elif s.startswith('Entry'):
            d['entry'] = float(s[6:-3].replace('USD', ''))
        elif s.startswith('Target'):
            d['targets'] = list(map(lambda x: float(x.replace('USD', '')), s[8:].split('; ')))
        elif s.startswith('Close'):
            d['close'] = float(s[7:-3].replace('USD', ''))

    return d


def write_data(file_name, data):
    with open(file_name, 'a') as f:
        f.write(data)


def main():
    content = read_data('deals.txt')
    filtered_content = [filter_data(data) for data in content]
    deals = [prepare_data(data) for data in filtered_content if data]
    deals_ans = [str(StrategyDeal(**deal)) for deal in deals]
    ans = f'\n{SEPARATOR}\n'.join(deals_ans)
    write_data('output.txt',ans)

if __name__ == '__main__':
    main()