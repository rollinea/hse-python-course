import os


class MdConverter:

    INPUT_CODE_DELIMITER = "# ---end---"
    MD_CODE_DELIMITER = '<!-- end -->'

    @staticmethod
    def read_data(file_name):
        f = open(file_name, "r")
        content = f.read()
        f.close()
        return content

    @staticmethod
    def write_data(file_name, data):
        out = open(file_name, 'w')
        out.write(data)
        out.close()

    @staticmethod
    def files_names():
        names = []

        a = os.path.basename(__file__)
        file_path = os.path.abspath(__file__).replace(a, '')
        for file in os.listdir(file_path):
            if file.endswith('.py') and file != "md_converter_as_class.py" and file != "md_converter_tests.py":
                names.append(file)

        return names

    @staticmethod
    def prepare_titles(data):
        title = description = None

        for line in data.split("\n"):
            if line.startswith("# title"):
                title = line.replace('# title ', '')
            elif line.startswith('# description'):
                description = line.replace('# description ', '')

        return title, description

    @staticmethod
    def convert_data(data):
        titles, source_code = data.split(MdConverter.INPUT_CODE_DELIMITER)
        title, description = MdConverter.prepare_titles(titles)
        head, template = MdConverter.prepare_format(title, description, source_code)
        return head, template

    @staticmethod
    def prepare_format(title, description, source_code):
        md_link = '-'.join(title.lower().split())
        head = f'[{title}](#{md_link})\n'
        tail = """
## {}
### {}  
```python
{}
```""".format(title, description, source_code.lstrip())
        return head, tail

    @staticmethod
    def md_update(file_name, head, tail):
        headers, solutions = '', ''
        if os.path.isfile(file_name):
            with open(file_name, 'r') as f:
                headers, code = f.read().split(MdConverter.MD_CODE_DELIMITER)

            headers += f'{head}\n{MdConverter.MD_CODE_DELIMITER}\n'
            solutions += code + tail + '\n'

            res = headers + solutions
            MdConverter.write_data('out.md', res)

        else:
            res = head + '\n<!-- end -->\n' + tail
            MdConverter.write_data('out.md', res)

    @staticmethod
    def to_md():
        solutions = MdConverter.files_names()

        for solution in solutions:
            content = MdConverter.read_data(solution)
            head, tail = MdConverter.convert_data(content)
            MdConverter.md_update('out.md', head, tail)
