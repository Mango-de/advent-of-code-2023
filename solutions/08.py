import re
from itertools import cycle

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/08') as f:
        base = test or f.read()
        instructions = cycle(base.split('\n\n')[0])
        nodes = {
            x[0]: (x[1], x[2])
            for x in re.findall(r'(.{3}) = \((.{3}), (.{3})\)', base.split('\n\n')[1])
        }

    return instructions, nodes


@get_runtime
def part_1(instructions: cycle, nodes: dict[str, tuple[str, str]]):
    current_node = 'AAA'
    c = 0

    for i in instructions:
        c += 1
        current_node = nodes[current_node]['LR'.index(i)]

        if current_node == 'ZZZ':
            break

    print(c)


# @get_runtime
# def part_2(instructions: cycle, nodes: dict[str, tuple[str, str]]):
#     current_nodes = [n for n in nodes if n.endswith('A')]
#     c = 0

#     for i in instructions:
#         c += 1

#         for j, node in enumerate(current_nodes):
#             current_nodes[j] = nodes[node]['LR'.index(i)]

#         if all(m.endswith('Z') for m in current_nodes):
#             break

#     print(c)


part_1(*get_input())
# part_2(*get_input())
