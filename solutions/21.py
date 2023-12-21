from operator import add

from utils.runtime import get_runtime

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_input(test: str = None):
    with open('inputs/21') as f:
        base = test or f.read()
        l = base.splitlines()

    return list(map(list, l))


@get_runtime
def part_1(grid: list[list[str]], steps: int):
    rocks = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start_position = (y, x)
            if grid[y][x] == '#':
                rocks.append((y, x))

    current_tiles = {start_position}

    for _ in range(steps):
        new_tiles = set()

        for tile in current_tiles:
            for direction in DIRECTIONS:
                if (new_tile := tuple(map(add, tile, direction))) not in rocks:
                    new_tiles.add(new_tile)

        current_tiles = new_tiles

    print(len(current_tiles))


@get_runtime
def part_2(grid: list[list[str]], steps: int):
    pass


part_1(get_input(), 64)
# part_2(get_input(), 26501365)
