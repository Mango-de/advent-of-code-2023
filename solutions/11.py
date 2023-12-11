from itertools import combinations

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/11') as f:
        base = test or f.read()
        l = base.splitlines()

    return list(map(list, l))


def solve(grid: list[list[str]], expansion: int) -> int:
    empty_rows = []
    empty_columns = []
    galaxies = []

    for y in range(len(grid)):
        if all(map(lambda v: v == '.', grid[y])):
            empty_rows.append(y)
    for x in range(len(grid[0])):
        if all(map(lambda line: line[x] == '.', grid)):
            empty_columns.append(x)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                galaxies.append((y, x))

    length_sum = 0

    for (y1, x1), (y2, x2) in sorted(combinations(galaxies, 2), key=lambda n: n[0]):
        steps = 0
        while y1 < y2:
            y1 += 1
            steps += 1
            if y1 in empty_rows:
                steps += expansion
        if x1 > x2:
            x1, x2 = x2, x1
        while x1 < x2:
            x1 += 1
            steps += 1
            if x1 in empty_columns:
                steps += expansion
        length_sum += steps

    return length_sum


@get_runtime
def part_1(grid: list[list[str]]):
    print(solve(grid, 1))


@get_runtime
def part_2(grid: list[list[str]]):
    print(solve(grid, 999_999))


part_1(get_input())
part_2(get_input())
