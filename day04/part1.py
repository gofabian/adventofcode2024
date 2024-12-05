import re

with open('input', 'r') as f:
    rows = f.read().splitlines()

max_x = len(rows[0])
max_y = len(rows)

# rows
texts = rows.copy()

# columns
for x in range(max_x):
    text = ''
    for row in rows:
        text += row[x]
    texts.append(text)


# diagonals
def diagonal(start_x, start_y, plus_y):
    text = ''
    y = start_y
    x = start_x
    while True:
        text += rows[y][x]
        x += 1
        y += plus_y
        if (x < 0) or (x >= max_x) or (y < 0) or (y >= max_y):
            break
    texts.append(text)


for x in range(0, max_x):
    diagonal(start_x=x, start_y=0, plus_y=1)
for y in range(1, max_y):
    diagonal(start_x=0, start_y=y, plus_y=1)
for x in range(0, max_x):
    diagonal(start_x=x, start_y=(max_y - 1), plus_y=-1)
for y in range(0, max_y - 1):
    diagonal(start_x=0, start_y=y, plus_y=-1)

# search XMAS
matches = []
for text in texts:
    pattern = re.compile(r'(?=XMAS|SAMX)')
    it = pattern.findall(text)
    for m in it:
        matches.append(m)

print(len(matches))
