# Day 7: Laboratories
import collections
import copy
import functools
import os
import pathlib


def main():
    grid, start = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(grid), copy.deepcopy(start))
    part_two(copy.deepcopy(grid), copy.deepcopy(start))


def parse(file_path):
    grid = {}
    start = None
    with open(file_path) as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                pos = x + y * 1j
                if char == "S":
                    assert start is None
                    start = pos
                else:
                    assert char in {".", "^"}
                    grid[pos] = char
    assert start is not None
    return grid, start


def part_one(grid, start):
    answer = bfs(grid, start)
    print(f"Part one: {answer}")


def part_two(grid, start):
    answer = dfs(grid, start + 1j)
    print(f"Part two: {answer}")


def bfs(grid, start):
    queue = collections.deque([start])
    visited = set()
    splits = 0
    while queue:
        pos = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        next_pos = pos + 1j
        if next_pos not in grid:
            continue
        if grid[next_pos] == ".":
            queue.append(next_pos)
        elif grid[next_pos] == "^":
            queue.append(next_pos - 1)
            queue.append(next_pos + 1)
            splits += 1
        else:
            assert False
    return splits


def dfs(grid, start):
    @functools.lru_cache
    def step(pos):
        if pos not in grid:
            return 1
        if grid[pos] == ".":
            return step(pos + 1j)
        elif grid[pos] == "^":
            return step(pos - 1) + step(pos + 1)
        else:
            assert False

    return step(start)


if __name__ == "__main__":
    main()
