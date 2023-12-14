from collections import defaultdict
from copy import deepcopy
from itertools import pairwise
from operator import sub

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/14') as f:
        base = test or f.read()
        l = base.splitlines()

    return list(map(list, l))


@get_runtime
def part_1(grid: list[list[str]]):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 'O':
                ny = y
                while ny > 0 and grid[ny - 1][x] == '.':
                    ny -= 1
                grid[y][x] = '.'
                grid[ny][x] = 'O'

    load = 0
    for n, line in zip(range(len(grid), 0, -1), grid):
        load += n * line.count('O')

    print(load)


@get_runtime
def part_2(grid: list[list[str]], cycles: int):
    destination_grids = defaultdict(list)

    for i in range(cycles):
        # north
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 'O':
                    ny = y
                    while ny > 0 and grid[ny - 1][x] == '.':
                        ny -= 1
                    grid[y][x] = '.'
                    grid[ny][x] = 'O'

        # west
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'O':
                    nx = x
                    while nx > 0 and grid[y][nx - 1] == '.':
                        nx -= 1
                    grid[y][x] = '.'
                    grid[y][nx] = 'O'

        # south
        for x in range(len(grid[0]) - 1, -1, -1):
            for y in range(len(grid) - 1, -1, -1):
                if grid[y][x] == 'O':
                    ny = y
                    while ny < len(grid) - 1 and grid[ny + 1][x] == '.':
                        ny += 1
                    grid[y][x] = '.'
                    grid[ny][x] = 'O'

        # east
        for y in range(len(grid) - 1, -1, -1):
            for x in range(len(grid[0]) - 1, -1, -1):
                if grid[y][x] == 'O':
                    nx = x
                    while nx < len(grid[0]) - 1 and grid[y][nx + 1] == '.':
                        nx += 1
                    grid[y][x] = '.'
                    grid[y][nx] = 'O'

        if (
            len((dest := destination_grids[deepcopy(tuple(map(tuple, grid)))])) == 3
            and len((dif_set := set(map(sub, *pairwise(dest)))))
            == 1  # repeats periodically
            and (
                (cycles - dest[0]) / list(dif_set)[0]
            ).is_integer()  # cycles = dest[0] + dif * n -> n needs to be whole number
        ):
            break
        else:
            dest.append(i + 1)

    load = 0
    for n, line in zip(range(len(grid), 0, -1), grid):
        load += n * line.count('O')

    print(load)


part_1(get_input())
part_2(get_input(), 1000000000)
