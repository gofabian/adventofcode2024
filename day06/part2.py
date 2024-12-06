with open('input', 'r') as f:
    original_map = f.read().splitlines()

max_x = len(original_map[0])
max_y = len(original_map)
original_map = [list(row) for row in original_map]


def does_guard_stay_in_loop(map):
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

    all_guard_directions = [
        dict(direction='^', dx=0, dy=-1),
        dict(direction='>', dx=1, dy=0),
        dict(direction='v', dx=0, dy=1),
        dict(direction='<', dx=-1, dy=0)
    ]
    guard_direction_index = -1
    guard_dx = 0
    guard_dy = 0
    guard_direction = ''

    def turn_right():
        nonlocal guard_direction_index, guard_dx, guard_dy, guard_direction

        guard_direction_index = (guard_direction_index + 1) % len(all_guard_directions)
        guard_direction = all_guard_directions[guard_direction_index]
        guard_dx = guard_direction['dx']
        guard_dy = guard_direction['dy']
        guard_direction = guard_direction['direction']

    def mark_guard():
        map[guard_y][guard_x] = guard_direction

    guard_x, guard_y = find_guard()
    turn_right()
    mark_guard()

    while True:
        # turn right if necessary
        while True:
            target_x = guard_x + guard_dx
            target_y = guard_y + guard_dy
            item = lookup_item(target_x, target_y)

            if item != '#':
                break

            turn_right()

        if item == 'outside':
            return False
        if item == guard_direction:
            return True

        guard_x = target_x
        guard_y = target_y
        mark_guard()

    # result = '\n'.join([''.join(row) for row in map])
    # print(result)
    # print(result.count('^') + result.count('>') + result.count('v') + result.count('<'))


counts = 0

for y in range(max_y):
    for x in range(max_x):
        # copy
        map = [[item for item in row] for row in original_map]

        if map[y][x] != '.':
            continue

        map[y][x] = '#'
        print(f'x={x} y={y}')

        if does_guard_stay_in_loop(map):
            counts += 1

print(counts)
