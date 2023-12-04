from collections import defaultdict

from utils.runtime import get_runtime


def get_input():
    with open('inputs/04') as f:
        l = f.read().splitlines()

    return l


def get_matching_numbers(line: str) -> set[int]:
    parts = line.split(' | ')
    winning_numbers = set([int(x) for x in parts[0].split(': ')[1].split()])
    card_numbers = set([int(x) for x in parts[1].split()])

    return winning_numbers & card_numbers


@get_runtime
def part_1(l: list[str]):
    points = 0

    for line in l:
        matching = get_matching_numbers(line)

        if (amount := len(matching)) > 0:
            points += int(2 ** (amount - 1))

    print(points)


@get_runtime
def part_2(l: list[str]):
    card_instances = defaultdict(lambda: 1)

    for i, line in enumerate(l, start=1):
        for j in range(1, len(get_matching_numbers(line)) + 1):
            card_instances[i + j] += 1 * card_instances[i]

    print(sum([card_instances[x] for x in range(1, len(l) + 1)]))


part_1(get_input())
part_2(get_input())
