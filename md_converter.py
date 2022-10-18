import os

INPUT_CODE_DELIMITER = "# ---end---"
MD_CODE_DELIMITER = '<!-- end -->'


def read_data(file_name):
    f = open(file_name, "r")
    content = f.read()
    f.close()
    return content


def write_data(file_name, data):
    out = open(file_name, 'w')
    out.write(data)
    out.close()


def files_names():
    names = []

    a = os.path.basename(__file__)
    file_path = os.path.abspath(__file__).replace(a, '')

    for file in os.listdir(file_path):
        if file.endswith('.py') and file != "md_converter.py":
            names.append(file)

    return names


def prepare_titles(data):
    title = description = None

    for line in data.split("\n"):
        if line.startswith("# title"):
            title = line.replace('# title', '')
        elif line.startswith('# description'):
            description = line.replace('# description', '')

    return title, description


def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_titles(titles)
    head, template = prepare_format(title, description, source_code)
    return head, template


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


def md_update(file_name, head, tail):
    headers, solutions = '', ''

    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            headers, code = f.read().split(MD_CODE_DELIMITER)

        headers += f'{head}\n{MD_CODE_DELIMITER}\n'
        solutions += code + tail + '\n'

        res = headers + solutions
        write_data('out.md', res)

    else:
        res = head + '\n<!-- end -->\n' + tail
        write_data('out.md', res)


def main():
    solutions = files_names()

    for solution in solutions:
        content = read_data(solution)
        head, tail = convert_data(content)
        md_update('out.md', head, tail)


main()
