# Day 11: Reactor
import copy
import functools
import os
import pathlib


def main():
    graph = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(graph))
    part_two(copy.deepcopy(graph))


def parse(file_path):
    graph = {}
    with open(file_path) as file:
        for line in file:
            node, neighbors = line.strip().split(": ")
            assert node not in graph
            graph[node] = neighbors.split()
    return graph


def part_one(graph):
    answer = dfs(graph, "you", tuple(), "out")
    print(f"Part one: {answer}")


def part_two(graph):
    answer = dfs(graph, "svr", ("dac", "fft"), "out")
    print(f"Part two: {answer}")


def dfs(graph, node, visits, end):
    @functools.lru_cache(maxsize=None)
    def step(node, visits):
        visits = tuple(e for e in visits if e != node)
        if node == end:
            return 0 if visits else 1
        return sum(step(n, visits) for n in graph[node])

    return step(node, visits)


if __name__ == "__main__":
    main()
