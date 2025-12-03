# Day 3: Lobby
import copy
import os
import pathlib

import numpy as np


def main():
    banks = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(banks))
    part_two(copy.deepcopy(banks))


def parse(file_path):
    banks = []
    with open(file_path) as file:
        for line in file:
            banks.append([int(e) for e in line.strip()])
    return banks


def part_one(banks):
    answer = solve(banks, 2)
    print(f"Part one: {answer}")


def part_two(banks):
    answer = solve(banks, 12)
    print(f"Part two: {answer}")


def solve(banks, n):
    return sum(int(turn_on(batteries, n)) for batteries in banks)


def turn_on(batteries, n):
    if n == 0:
        return ""
    largest = np.argmax(batteries[:len(batteries) - n + 1])
    return str(batteries[largest]) + turn_on(batteries[largest + 1:], n - 1)


if __name__ == "__main__":
    main()
