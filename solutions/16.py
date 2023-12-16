from operator import add

from utils.runtime import get_runtime

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r, d, l, u | coming from l, u, r, d


def get_input(test: str = None):
    with open('inputs/16') as f:
        base = test or f.read()
        l = base.splitlines()

    return list(map(list, l))


def solve(grid: list[list[str]], starting_beam: tuple[tuple[int, int], int, int]):
    beams = [starting_beam]
    all_beams = []

    energized = set()

    while len(beams) > 0:
        direction, y, x = beams.pop(0)

        while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            energized.add((y, x))

            match grid[y][x]:
                case '/':
                    if (i := DIRECTIONS.index(direction)) % 2 == 0:  # l, r
                        direction = DIRECTIONS[(i - 1) % 4]
                    else:
                        direction = DIRECTIONS[(i + 1) % 4]
                case '\\':
                    if (i := DIRECTIONS.index(direction)) % 2 == 0:  # l, r
                        direction = DIRECTIONS[(i + 1) % 4]
                    else:
                        direction = DIRECTIONS[(i - 1) % 4]
                case '-':
                    if (i := DIRECTIONS.index(direction)) % 2 == 1:  # u, d
                        direction = DIRECTIONS[(i + 1) % 4]
                        if (
                            new_beam := (DIRECTIONS[(i - 1) % 4], y, x)
                        ) not in all_beams:
                            beams.append(new_beam)
                            all_beams.append(new_beam)
                        else:
                            break
                case '|':
                    if (i := DIRECTIONS.index(direction)) % 2 == 0:  # l, r
                        direction = DIRECTIONS[(i + 1) % 4]
                        if (
                            new_beam := (DIRECTIONS[(i - 1) % 4], y, x)
                        ) not in all_beams:
                            beams.append(new_beam)
                            all_beams.append(new_beam)
                        else:  # loop detected
                            break

            y, x = map(add, (y, x), direction)

    return len(energized)


@get_runtime
def part_1(grid: list[list[str]]):
    print(solve(grid, ((0, 1), 0, 0)))


@get_runtime
def part_2(grid: list[list[str]]):
    max_energization = 0

    for x in range(len(grid[0])):
        max_energization = max(max_energization, solve(grid, ((1, 0), 0, x)))
        max_energization = max(
            max_energization, solve(grid, ((-1, 0), len(grid) - 1, x))
        )

    for y in range(len(grid)):
        max_energization = max(max_energization, solve(grid, ((0, 1), y, 0)))
        max_energization = max(
            max_energization, solve(grid, ((0, -1), y, len(grid[0]) - 1))
        )

    print(max_energization)


part_1(get_input())
part_2(get_input())
