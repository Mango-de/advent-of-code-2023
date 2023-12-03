import re

from utils.runtime import get_runtime


def get_input():
    with open('inputs/02') as f:
        l = f.read().splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    game_id_sum = 0

    for line in l:
        game, sets = line.split(':')

        r = max([int(amount) for amount in re.findall(r'(\d+) red', sets)])
        g = max([int(amount) for amount in re.findall(r'(\d+) green', sets)])
        b = max([int(amount) for amount in re.findall(r'(\d+) blue', sets)])

        if r <= 12 and g <= 13 and b <= 14:
            game_id_sum += int(re.findall(r'\d+', game)[0])

    print(game_id_sum)


@get_runtime
def part_2(l: list[str]):
    power_sum = 0

    for line in l:
        sets = line.split(':')[1]

        r = max([int(amount) for amount in re.findall(r'(\d+) red', sets)])
        g = max([int(amount) for amount in re.findall(r'(\d+) green', sets)])
        b = max([int(amount) for amount in re.findall(r'(\d+) blue', sets)])

        power_sum += r * g * b

    print(power_sum)


part_1(get_input())
part_2(get_input())
