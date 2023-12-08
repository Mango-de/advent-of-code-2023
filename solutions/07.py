from collections import defaultdict
from enum import IntEnum

from utils.runtime import get_runtime


class HandType(IntEnum):
    five = 1
    four = 2
    full_house = 3
    three = 4
    two_pair = 5
    one_pair = 6
    high_card = 7


def get_input(test: str = None):
    with open('inputs/07') as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    cards = defaultdict(list)

    for line in l:
        hand = line.split()[0]

        chars = defaultdict(int)
        for char in hand:
            chars[char] += 1

        value_list = sorted(list(chars.values()))

        if any(v == 5 for v in value_list):
            cards[HandType.five].append(line)
        elif any(v == 4 for v in value_list):
            cards[HandType.four].append(line)
        elif value_list[0] == 2 and value_list[1] == 3:
            cards[HandType.full_house].append(line)
        elif any(v == 3 for v in value_list):
            cards[HandType.three].append(line)
        elif value_list[-2] == value_list[-1] == 2:
            cards[HandType.two_pair].append(line)
        elif any(v == 2 for v in value_list):
            cards[HandType.one_pair].append(line)
        else:
            cards[HandType.high_card].append(line)

    order = []
    labels = 'AKQJT98765432'

    for k, v in cards.items():
        cards[k] = sorted(v, key=lambda x: tuple(labels.index(x[i]) for i in range(5)))

    for i in range(1, 8):
        order.extend(cards[i])

    print(sum(c * int(line.split()[-1]) for c, line in enumerate(order[::-1], start=1)))


@get_runtime
def part_2(l: list[str]):
    pass


part_1(get_input())
part_2(get_input())
