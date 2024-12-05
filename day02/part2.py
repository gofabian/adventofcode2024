import csv


def filter(row):
    factor = 1 if (row[1] - row[0] > 0) else -1

    for i in range(len(row) - 1):
        diff = (row[i + 1] - row[i]) * factor
        if diff < 1 or diff > 3:
            return False
    return True


def filter_with_tolerance(row):
    valid = filter(row)

    if not valid:
        for i in range(len(row)):
            temp = row.copy()
            temp.pop(i)
            valid = filter(temp)
            if valid:
                break

    return valid


with open('input', newline='') as f:
    rows = csv.reader(f, delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
    filtered = [row for row in rows if filter_with_tolerance(row)]
    print(len(filtered))
