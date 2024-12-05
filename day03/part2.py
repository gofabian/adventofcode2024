import re

with open('input', 'r') as f:
    memory = f.read()

pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")

it = pattern.finditer(memory)

active = True
collected = []
for m in it:
    if m[0] == "do()":
        active = True
        continue
    if m[0] == "don't()":
        active = False
        continue
    if active:
        collected.append(m)

products = [int(m[1]) * int(m[2]) for m in collected]
print(sum(products))
