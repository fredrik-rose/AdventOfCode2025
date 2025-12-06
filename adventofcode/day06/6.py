# Day 6: Trash Compactor
import copy
import functools
import operator
import os
import pathlib

OPERATORS = {
    "+": operator.add,
    "*": operator.mul,
}


def main():
    numbers, operators = parse_one(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(numbers), copy.deepcopy(operators))
    digits, operators = parse_two(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_two(copy.deepcopy(digits), copy.deepcopy(operators))


def parse_one(file_path):
    numbers = []
    with open(file_path) as file:
        content = file.read().splitlines()
        for line in content[:-1]:
            numbers.append([int(e) for e in line.split()])
        operators = content[-1].split()
    return numbers, operators


def parse_two(file_path):
    digits = []
    with open(file_path) as file:
        content = file.read().splitlines()
        for line in content[:-1]:
            digits.append([int("0" if char == " " else char) for char in line])
        operators = content[-1].split()
    lenght = max(len(line) for line in digits)
    for line in digits:
        line.extend([0] * (lenght - len(line)))
    return digits, operators


def part_one(numbers, operators):
    numbers = list(zip(*numbers))
    answer = solve(numbers, operators)
    print(f"Part one: {answer}")


def part_two(digits, operators):
    digits = list(zip(*digits))
    numbers = [[]]
    for line in digits:
        num = "".join(str(e) for e in line if e)
        if num:
            numbers[-1].append(int(num))
        else:
            numbers.append([])
    answer = solve(numbers, operators)
    print(f"Part two: {answer}")


def solve(numbers, operators):
    return sum(functools.reduce(OPERATORS[op], line) for line, op in zip(numbers, operators))


if __name__ == "__main__":
    main()
