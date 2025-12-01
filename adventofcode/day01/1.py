# Day 1: Secret Entrance
import copy
import os
import pathlib


def main():
    combination = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(combination))
    part_two(copy.deepcopy(combination))


def parse(file_path):
    combination = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            assert line[0] in {"L", "R"}
            direction = -1 if line[0] == "L" else 1
            distance = int(line[1:])
            combination.append((direction, distance))
    return combination


def part_one(combination):
    answer = solve(combination, single_click=False)
    print(f"Part one: {answer}")


def part_two(combination):
    answer = solve(combination, single_click=True)
    print(f"Part two: {answer}")


def solve(combination, single_click):
    return sum(1 for position in rotate(combination, single_click) if position == 0)


def rotate(combination, single_click):
    position = 50
    for direction, distance in combination:
        for _ in range(distance):
            position = (position + direction) % 100
            if single_click:
                yield position
        if not single_click:
            yield position


if __name__ == "__main__":
    main()
