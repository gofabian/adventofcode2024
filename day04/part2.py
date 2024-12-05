import re

with open('input', 'r') as f:
    rows = f.read().splitlines()

max_x = len(rows[0])
max_y = len(rows)

# collect 3x3 squares
squares = []
for x in range(0, max_x - 2):
    for y in range(0, max_y - 2):
        square = ''
        for local_y in range(0, 3):
            for local_x in range(0, 3):
                square += rows[x + local_x][y + local_y]
        squares.append(square)

# search X-MAS
matches = []
for square in squares:
    pattern = re.compile(r'M.S.A.M.S|M.M.A.S.S|S.M.A.S.M|S.S.A.M.M')
    it = pattern.findall(square)
    for m in it:
        matches.append(m)

print(len(matches))
