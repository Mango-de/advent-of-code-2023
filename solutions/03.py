from collections import defaultdict

from utils.runtime import get_runtime


def get_input():
    with open('inputs/03') as f:
        l = [[x for x in y] for y in f.read().splitlines()]

    return l


@get_runtime
def part_1(l: list[list[str]]):
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    part_number_sum = 0

    for i, y in enumerate(l):
        j = 0
        x = lambda: y[j]

        while j < len(y) - 1:
            while not x().isdigit():
                if j < len(y) - 1:
                    j += 1
                else:
                    break
            number = ''
            while x().isdigit():
                part_number = False
                number += x()
                for a, b in adjacent:
                    if 0 <= i + a < len(l) - 1 and 0 <= j + b < len(y) - 1:
                        cell = l[i + a][j + b]
                        if cell != '.' and not cell.isdigit():
                            part_number = True
                            break
                if part_number:
                    while x().isdigit():
                        if j < len(y) - 1:
                            j += 1
                            if x().isdigit():
                                number += x()
                        else:
                            break
                    part_number_sum += int(number)
                    number = ''
                    break
                else:
                    if j < len(y) - 1:
                        j += 1
                    else:
                        number = ''
                        break

    print(part_number_sum)


@get_runtime
def part_2(l: list[list[str]]):
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    gears = defaultdict(list)

    for i, y in enumerate(l):
        j = 0
        x = lambda: y[j]

        while j < len(y) - 1:
            while not x().isdigit():
                if j < len(y) - 1:
                    j += 1
                else:
                    break
            number = ''
            while x().isdigit():
                gear_number = False
                number += x()
                for a, b in adjacent:
                    if 0 <= i + a < len(l) - 1 and 0 <= j + b < len(y) - 1:
                        cell = l[i + a][j + b]
                        if cell == '*':
                            gear_number = True
                            coordinates = (i + a, j + b)
                            break
                if gear_number:
                    while x().isdigit():
                        if j < len(y) - 1:
                            j += 1
                            if x().isdigit():
                                number += x()
                        else:
                            break
                    gears[coordinates].append(int(number))
                    number = ''
                    break
                else:
                    if j < len(y) - 1:
                        j += 1
                    else:
                        number = ''
                        break

    gear_ratio_sum = 0

    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += nums[0] * nums[1]

    print(gear_ratio_sum)


part_1(get_input())
part_2(get_input())
