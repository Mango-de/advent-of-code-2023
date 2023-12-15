import re
from collections import defaultdict

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/15') as f:
        base = test or f.read()
        l = base.split(',')

    return l


def hash_algorithm(string: str):
    current_value = 0

    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


@get_runtime
def part_1(l: list[str]):
    print(sum(map(hash_algorithm, l)))


@get_runtime
def part_2(l: list[str]):
    boxes = defaultdict(dict)

    for step in l:
        label, operation, focal_length = re.match(r'([a-z]+)(=|-)(\d?)', step).groups()
        current_box = hash_algorithm(label)
        if operation == '-':
            if label in boxes[current_box]:
                del boxes[current_box][label]
        elif operation == '=':
            boxes[current_box][label] = int(focal_length)

    focusing_power_sum = 0

    for box_nr, lens in boxes.items():
        for c, focal_length in enumerate(lens.values(), start=1):
            focusing_power_sum += (box_nr + 1) * c * focal_length

    print(focusing_power_sum)


part_1(get_input())
part_2(get_input())
