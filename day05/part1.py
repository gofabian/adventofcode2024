with open('input', 'r') as f:
    parts = f.read().split("\n\n")
    rules = parts[0].splitlines()
    all_pages = parts[1].splitlines()

all_pages = [f',{p},' for p in all_pages]

rules = [r.split('|') for r in rules]


def matches_rule(pages, rule):
    index0 = pages.find(rule[0])
    index1 = pages.find(rule[1])

    if index0 == -1 or index1 == -1:
        return True

    return index0 < index1


def matches_all_rules(pages):
    return not any(not matches_rule(pages, rule) for rule in rules)


all_good_pages = [p for p in all_pages if matches_all_rules(p)]


def get_middle_page_number(page):
    parts = page.split(",")
    return int(parts[len(parts) // 2])


middle_page_numbers = [get_middle_page_number(p) for p in all_good_pages]

print(sum(middle_page_numbers))
