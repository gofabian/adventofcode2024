import re

with open('input', 'r') as f:
    memory = f.read()

pattern = re.compile(r'mul\((\d+),(\d+)\)')

it = pattern.finditer(memory)

products = [int(m[1]) * int(m[2]) for m in it]
print(sum(products))
