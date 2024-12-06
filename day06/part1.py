with open('input', 'r') as f:
    map = f.read().splitlines()

max_x = len(map[0])
max_y = len(map)
map = [list(row) for row in map]


def lookup_item(x, y):
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return 'outside'
    return map[y][x]


def find_guard():
    for x in range(max_x):
        for y in range(max_y):
            item = lookup_item(x, y)
            if item == '^':
                return x, y


guard_x, guard_y = find_guard()
guard_dx = 0
guard_dy = -1


def mark_guard():
    map[guard_y][guard_x] = 'X'


mark_guard()


def turn_right():
    global guard_dx, guard_dy
    old_guard_dy = guard_dy
    guard_dy = guard_dx
    guard_dx = old_guard_dy
    if old_guard_dy != 0:
        guard_dx *= -1


while True:
    # turn right if necessary
    while True:
        target_x = guard_x + guard_dx
        target_y = guard_y + guard_dy
        item = lookup_item(target_x, target_y)

        if item != '#':
            break

        turn_right()

    # outside of map?
    if item == 'outside':
        break

    guard_x += guard_dx
    guard_y += guard_dy
    mark_guard()

result = '\n'.join([''.join(row) for row in map])
print(result)
print(result.count('X'))
