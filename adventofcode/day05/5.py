# Day 5: Cafeteria
import copy
import os
import pathlib


def main():
    ranges, ingredients = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(ranges), copy.deepcopy(ingredients))
    part_two(copy.deepcopy(ranges))


def parse(file_path):
    ranges = []
    ingredients = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            left, right = (int(e) for e in line.split("-"))
            ranges.append(range(left, right + 1))
        for line in file:
            line = line.strip()
            ingredients.append(int(line))
    return ranges, ingredients


def part_one(ranges, ingredients):
    answer = 0
    for x in ingredients:
        for r in ranges:
            if x in r:
                answer += 1
                break
    print(f"Part one: {answer}")


def part_two(ranges):
    ranges = merge_ranges(ranges)
    answer = sum(len(r) for r in ranges)
    print(f"Part two: {answer}")


def merge_ranges(ranges):
    events = []
    for r in ranges:
        events.append((r[0], True))
        events.append((r[-1], False))
        assert r[0] <= r[-1]
    merged = []
    stack = []
    for pos, on in sorted(events, key=lambda x: (x[0], not x[1])):
        if on:
            stack.append(pos)
        else:
            start = stack.pop()
        if not stack:
            merged.append(range(start, pos + 1))
    assert not stack
    return merged


if __name__ == "__main__":
    main()
