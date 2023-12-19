import re
from operator import add

from utils.runtime import get_runtime

DIRECTIONS = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}


def get_input(test: str = None):
    with open('inputs/18') as f:
        base = test or f.read()
        l = base.splitlines()

    return [(x[0], int(x[1]), x[2]) for x in map(lambda line: line.split(), l)]


def solve(directions, steps):
    edges = {(0, 0)}

    y, x = 0, 0

    for direction, step in zip(directions, steps):
        for _ in range(step):
            y, x = map(add, (y, x), DIRECTIONS[direction])
            edges.add((y, x))

    filled = 0

    for y in range(
        min(edges, key=lambda x: x[0])[0], max(edges, key=lambda x: x[0])[0] + 1
    ):
        num = 0

        for x in range(
            min(edges, key=lambda x: x[1])[1], max(edges, key=lambda x: x[1])[1] + 1
        ):
            if (y, x) in edges:
                if (y - 1, x) in edges and (y + 1, x) in edges:
                    num += 1
                else:
                    if (y + 1, x) in edges and (y, x + 1) in edges:  # D-R
                        s = 0
                        num += 1
                    elif (y - 1, x) in edges and (y, x + 1) in edges:  # U-R
                        s = 1
                        num += 1
                    else:
                        if (y + 1, x) in edges and (y, x - 1) in edges:  # D-L
                            if s == 0:
                                num += 1
                            s = 0
                        elif (y - 1, x) in edges and (y, x - 1) in edges:  # U-L
                            if s == 1:
                                num += 1
                            s = 0
            else:
                if num % 2 == 1:
                    filled += 1

    return len(edges) + filled


@get_runtime
def part_1(l: list[tuple[str, int, str]]):
    print(solve([x[0] for x in l], [x[1] for x in l]))


# takes too long - algorithm too inefficient -> Part 2 not solved
@get_runtime
def part_2(l: list[tuple[str, int, str]]):
    def collect_information(instruction: str):
        groups = re.match(r'\(#(.{5})(.)\)', instruction).groups()
        return int(groups[0], 16), 'RDLU'[int(groups[1])]

    information_map = list(map(collect_information, [x[2] for x in l]))
    print(solve([x[1] for x in information_map], [x[0] for x in information_map]))


part_1(get_input())
# part_2(get_input())
