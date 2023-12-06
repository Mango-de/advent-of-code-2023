from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/06') as f:
        base = test or f.read()
        l = base.splitlines()

    return list(
        zip(
            [int(x) for x in l[0].split(': ')[1].split()],
            [int(x) for x in l[1].split(': ')[1].split()],
        )
    )


@get_runtime
def part_1(l: list[tuple[int, int]]):
    product = 1

    for time, distance in l:
        winners = 0
        for i in range(1, time):
            if i * (time - i) > distance:
                winners += 1
        product *= winners

    print(product)


@get_runtime
def part_2(l: list[str]):
    time = int(''.join([str(x[0]) for x in l]))
    distance = int(''.join([str(x[1]) for x in l]))

    winners = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            winners += 1

    print(winners)


part_1(get_input())
part_2(get_input())
