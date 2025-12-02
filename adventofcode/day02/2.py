# Day 2: Gift Shop
import copy
import os
import pathlib
import re


def main():
    ranges = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(ranges))
    part_two(copy.deepcopy(ranges))


def parse(file_path):
    ranges = []
    with open(file_path) as file:
        for raw_range in file.readline().strip().split(","):
            start, end = (int(e) for e in raw_range.split("-"))
            ranges.append((start, end))
    return ranges


def part_one(ranges):
    pattern = re.compile(r"^(\d+)\1$")
    answer = solve(ranges, pattern)
    print(f"Part one: {answer}")


def part_two(ranges):
    pattern = re.compile(r"^(\d+)\1+$")
    answer = solve(ranges, pattern)
    print(f"Part two: {answer}")


def solve(ranges, pattern):
    answer = 0
    for start, end in ranges:
        answer += sum(n for n in range(start, end + 1) if pattern.match(str(n)))
    return answer


if __name__ == "__main__":
    main()
