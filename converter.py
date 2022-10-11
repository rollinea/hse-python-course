with open('solution.py') as f:
    content = f.readlines()

out = open("out.txt","w")
for line in content:
    if line.startswith("# title"):
        title = line[7:].strip()
        out.write("+ [{}](#{})\n".format(title,"-".join(title.split())))
    elif line.startswith("# description"):
        description = line[13:]
        out.write(f"# {description}")
    elif line.startswith("# ---start---"):
        out.write("```python\n")
    elif line.startswith("# ---end---"):
        out.write("```\n")
    else:
        out.write(f"{line}")
f.close()
out.close()
