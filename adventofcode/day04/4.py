# Day 4: Printing Department
import copy
import os
import pathlib


def main():
    grid = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(grid))
    part_two(copy.deepcopy(grid))


def parse(file_path):
    grid = set()
    with open(file_path) as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char == "@":
                    grid.add(x + y * 1j)
    return grid


def part_one(grid):
    answer = len(remove_rolls(grid))
    print(f"Part one: {answer}")


def part_two(grid):
    answer = 0
    while removed := remove_rolls(grid):
        grid = grid - removed
        answer += len(removed)
    print(f"Part two: {answer}")


def remove_rolls(grid):
    removed = set()
    for node in grid:
        neighbors = 0
        for y in (-1j, 0j, 1j):
            for x in (-1, 0, 1):
                offset = x + y
                if offset == 0:
                    continue
                if node + offset in grid:
                    neighbors += 1
        if neighbors < 4:
            removed.add(node)
    return removed


if __name__ == "__main__":
    main()
