# Day 8: Playground
import collections
import copy
import functools
import itertools
import math
import os
import pathlib


class UnionFind:
    def __init__(self, nodes):
        self.uf = {n: n for n in nodes}

    def union(self, x, y):
        self.uf[self.find(x)] = self.find(y)

    def find(self, x):
        if x == self.uf[x]:
            return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]


def main():
    boxes = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(boxes))
    part_two(copy.deepcopy(boxes))


def parse(file_path):
    boxes = []
    with open(file_path) as file:
        for line in file:
            coordinates = tuple(int(e) for e in line.strip().split(","))
            boxes.append(coordinates)
    return boxes


def part_one(boxes):
    uf = UnionFind(boxes)
    for a, b in itertools.islice(construct_graph(boxes), 1000):
        uf.union(a, b)
    components = collections.defaultdict(set)
    for box in boxes:
        components[uf.find(box)].add(box)
    answer = functools.reduce(
        lambda x, y: x * y,
        sorted([len(e) for e in components.values()], reverse=True)[:3],
    )
    print(f"Part one: {answer}")


def part_two(boxes):
    visited = set()
    for a, b in construct_graph(boxes):
        visited.add(a)
        visited.add(b)
        if len(visited) == len(boxes):
            answer = a[0] * b[0]
            break
    print(f"Part two: {answer}")


def construct_graph(boxes):
    distances = []
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            distances.append((euclidian_distance(a, b), a, b))
    for _, a, b in sorted(distances):
        yield a, b


def euclidian_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


if __name__ == "__main__":
    main()
