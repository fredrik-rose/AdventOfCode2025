# Day 12: Christmas Tree Farm
import copy
import os
import pathlib


def main():
    shapes, grids = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(shapes), copy.deepcopy(grids))


def parse(file_path):
    data = []
    with open(file_path) as file:
        data = file.read().split("\n\n")
        shapes = []
        for raw_shape in data[:-1]:
            single_shape = set()
            for y, line in enumerate(raw_shape.split("\n")[1:]):
                for x, char in enumerate(line.strip()):
                    if char == "#":
                        single_shape.add(x + y * 1j)
            shapes.append(single_shape)
        grids = []
        for line in data[-1].strip().split("\n"):
            raw_size, raw_counters = line.strip().split(": ")
            size = tuple(int(e) for e in raw_size.split("x"))
            counters = tuple(int(e) for e in raw_counters.split())
            grids.append((size, counters))
    return shapes, grids


def part_one(shapes, grids):
    answer = 0
    for size, counters in grids:
        min_size = sum(len(s) * c for s, c in zip(shapes, counters))
        max_size = 3 * 3 * sum(counters)
        area = size[0] * size[1]
        if area >= max_size:
            answer += 1  # We know for sure it will fit, even with the worst possible packaging.
        elif area <= min_size:
            pass  # We know for sure it will not fit, even with the best possible packaging.
        else:
            assert False  # Would need to try to fit the shapes on the grid, really hard problem!
    print(f"Part one: {answer}")


if __name__ == "__main__":
    main()
