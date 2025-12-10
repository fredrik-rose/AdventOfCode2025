# Day 10: Factory
import collections
import copy
import os
import pathlib

import z3


def main():
    machines = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(machines))
    part_two(copy.deepcopy(machines))


def parse(file_path):
    machines = []
    with open(file_path) as file:
        for line in file:
            parts = line.strip().split()
            raw_lights = parts[0]
            lights = int(raw_lights[1:-1].replace("#", "1").replace(".", "0"), 2)
            joltage = [int(e) for e in parts[-1][1:-1].split(",")]
            buttons = []
            for raw_botton in parts[1:-1]:
                indexes = set(int(e) for e in raw_botton[1:-1].split(","))
                buttons.append([1 if i in indexes else 0 for i in range(len(joltage))])
            machines.append((lights, buttons, joltage))
    return machines


def part_one(machines):
    answer = 0
    for goal, buttons, _ in machines:
        mask_buttons = [int("".join(str(e) for e in single_button), 2) for single_button in buttons]
        answer += bfs(mask_buttons, goal)
    print(f"Part one: {answer}")


def part_two(machines):
    answer = sum(solve(buttons, goal) for _, buttons, goal in machines)
    print(f"Part two: {answer}")


def bfs(buttons, goal):
    queue = collections.deque([(0, b, 0) for b in buttons])
    visited = set()
    while queue:
        value, mask, steps = queue.popleft()
        if (value, mask) in visited:
            continue
        visited.add((value, mask))
        if value == goal:
            return steps
        value ^= mask
        for b in buttons:
            queue.append((value, b, steps + 1))
    assert False


def solve(buttons, goal):
    # Buttons (variables):
    # [1, 0, 0, 1] (x1)
    # [0, 1, 0, 1] (x2)
    # [1, 0, 1, 0] (x3)
    #
    # Goal:
    # [3, 4, 2, 5]
    #
    # Constraints:
    # x1 + x3 = 3
    # x2      = 4
    # x3      = 2
    # x1 + x2 = 5
    # x1 >= 0, x2 >= 0, x3 >=0
    #
    # Objective:
    # min(x1 + x2 + x3)

    # Variables
    variables = [z3.Int(f"x{i}") for i in range(len(buttons))]

    # Constraints
    opt = z3.Optimize()
    for i, g in enumerate(goal):
        terms = []
        for j, b in enumerate(buttons):
            if b[i]:
                terms.append(variables[j])
        opt.add(sum(terms) == g)
    for x in variables:
        opt.add(x >= 0)

    # Objective
    total_sum = sum(variables)
    opt.minimize(total_sum)

    # Solve
    if opt.check() == z3.sat:
        model = opt.model()
    else:
        assert False
    return model.eval(total_sum).as_long()


if __name__ == "__main__":
    main()
