import re
f = open("day_3_input.txt")
content = "".join(f.readlines())
print(content)
matches = re.findall( r'mul\(\d+,\d+\)', content)
pairs = [[int(y) for y in x[4:-1].split(",")] for x in matches]
print(sum([x[0] * x[1] for x in pairs]))
