import functools

with open('input', 'r') as f:
    parts = f.read().split("\n\n")
    rules = parts[0].splitlines()
    all_pages = parts[1].splitlines()


def get_all_bad_pages():
    all_pages_comma = [f',{p},' for p in all_pages]
    rules_list = [r.split('|') for r in rules]

    def matches_rule(pages, rule):
        index0 = pages.find(rule[0])
        index1 = pages.find(rule[1])

        if index0 == -1 or index1 == -1:
            return True

        return index0 < index1

    def matches_all_rules(pages):
        return not any(not matches_rule(pages, rule) for rule in rules_list)

    return [p for p in all_pages_comma if not matches_all_rules(p)]


def cmp(page0, page1):
    return -1 if (f"{page0}|{page1}" in rules) else 1


def sort_pages(pages):
    parts = pages.split(',')
    parts_sorted = sorted(parts, key=functools.cmp_to_key(cmp))
    return ','.join(parts_sorted)


all_bad_pages = get_all_bad_pages()

all_corrected_pages = [sort_pages(p) for p in all_bad_pages]


def get_middle_page_number(page):
    parts = page.split(",")
    return int(parts[len(parts) // 2])


middle_page_numbers = [get_middle_page_number(p) for p in all_corrected_pages]

print(sum(middle_page_numbers))
