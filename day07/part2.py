import itertools
import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

equations = [re.split(r"[\s:]+", line) for line in lines]


def combine_operations_and_values(operations, values):
    return [[operations[i], values[i]] for i in range(len(operations))]


def generate_actions(values):
    combinations = list(itertools.product(['+', '*', '||'], repeat=len(values)))
    return [[[ops[i], int(values[i])] for i in range(len(ops))] for ops in combinations]


def calc(initial_value, actions):
    result = initial_value
    for op, value in actions:
        if op == '+':
            result += value
        elif op == '*':
            result *= value
        else:
            result = int(str(result) + str(value))
    return result


def is_match(initial_value, actions, expected_result):
    result = initial_value
    for op, value in actions:
        if op == '+':
            result += value
        elif op == '*':
            result *= value
        else:
            result = int(str(result) + str(value))

        if result > expected_result:
            return False
    return result == expected_result


def has_any_match(equation):
    expected_result = int(equation[0])
    initial_value = int(equation[1])
    actions_list = generate_actions(equation[2:])
    return any(is_match(initial_value, actions, expected_result) for actions in actions_list)


valid_equations = [e for e in equations if has_any_match(e)]

valid_results = [int(e[0]) for e in valid_equations]
print(sum(valid_results))
