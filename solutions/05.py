from functools import cache

from utils.runtime import get_runtime


def get_input(test: str = None) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    with open('inputs/05') as f:
        base = test or f.read()
        l = base.split('\n\n')
        seeds = [int(x) for x in l[0].split(': ')[1].split()]

        maps = []

        for garden_map in l[1:]:
            ranges = []
            for map_range in garden_map.splitlines()[1:]:
                ranges.append(tuple(int(x) for x in map_range.split()))
            maps.append(ranges)

    return seeds, maps


@cache
def get_next_value(current_map, current_value: int):
    for destination_start, source_start, length in current_map:
        if source_start <= current_value < source_start + length:
            return destination_start + current_value - source_start

    return current_value


@get_runtime
def part_1(seeds: list[int], maps: list[list[tuple[int, int, int]]]):
    min_location = float('inf')

    for seed in seeds:
        current_value = seed

        for current_map in maps:
            current_value = get_next_value(tuple(current_map), current_value)

        min_location = min(min_location, current_value)

    print(min_location)


# takes too long - algorithm too inefficient -> Part 2 not solved
@get_runtime
def part_2(seed_ranges: list[int], maps: list[list[tuple[int, int, int]]]):
    min_location = float('inf')

    for i in range(0, len(seed_ranges), 2):
        for seed in range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]):
            current_value = seed

            for current_map in maps:
                current_value = get_next_value(tuple(current_map), current_value)

            min_location = min(min_location, current_value)

    print(min_location)


part_1(*get_input())
part_2(*get_input())
