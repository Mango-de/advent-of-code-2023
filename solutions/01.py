import re

from utils.runtime import get_runtime


def get_input():
    with open('inputs/01') as f:
        l = f.read().splitlines()

    return l


def get_sum_calibration_values(l: list[str]):
    sum_calibration_values = 0

    for line in l:
        for c in line:
            if c.isdigit():
                first = c
                break
        for c in line[::-1]:
            if c.isdigit():
                last = c
                break
        sum_calibration_values += int(first + last)

    return sum_calibration_values


@get_runtime
def part_1(l: list[str]):
    print(get_sum_calibration_values(l))


@get_runtime
def part_2(l: list[str]):
    to_replace = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    } | {str(i): i for i in range(1, 10)}

    new = []

    for line in l:
        pattern = re.compile('|'.join(to_replace.keys()))
        reversed_pattern = re.compile('|'.join(to_replace.keys())[::-1])

        left_replaced = pattern.sub(lambda m: str(to_replace[m.group(0)]), line, 1)
        right_replaced = reversed_pattern.sub(
            lambda m: str(to_replace[m.group(0)[::-1]]), left_replaced[::-1], 1
        )
        new.append(right_replaced[::-1])

    print(get_sum_calibration_values(new))


part_1(get_input())
part_2(get_input())
