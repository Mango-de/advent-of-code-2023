from itertools import pairwise

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/09') as f:
        base = test or f.read()
        l = base.splitlines()

    return [[int(x) for x in line.split()] for line in l]


@get_runtime
def part_1(histories: list[list[int]]):
    extrapolated_values_sum = 0

    for history in histories:
        sequences = [history]

        while not all(x == 0 for x in sequences[-1]):
            new_sequence = []
            for a, b in pairwise(sequences[-1]):
                new_sequence.append(b - a)
            sequences.append(new_sequence)

        extrapolated_value = 0
        for sequence in sequences[::-1]:
            extrapolated_value += sequence[-1]

        extrapolated_values_sum += extrapolated_value

    print(extrapolated_values_sum)


@get_runtime
def part_2(histories: list[list[int]]):
    extrapolated_values_sum = 0

    for history in histories:
        sequences = [history]

        while not all(x == 0 for x in sequences[-1]):
            new_sequence = []
            for a, b in pairwise(sequences[-1]):
                new_sequence.append(b - a)
            sequences.append(new_sequence)

        extrapolated_value = 0
        for sequence in sequences[::-1]:
            extrapolated_value = sequence[0] - extrapolated_value

        extrapolated_values_sum += extrapolated_value

    print(extrapolated_values_sum)


part_1(get_input())
part_2(get_input())
