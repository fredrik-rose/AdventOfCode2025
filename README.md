# Advent of Code 25

Solutions for the advent of code 2025 puzzles, implemented in Python. The
puzzles can be found here: https://adventofcode.com/2025

## Static Code Analysis

```
flake8 adventofcode/
black --line-length 120 --diff adventofcode/
pylint adventofcode/
```

## Algorithms

### Repeated Substring Trick

To check if `string` is a repeated substring (e.g. `ABABAB` or `ABCABC`) one can use this trick:
```
def is_repeated_substring(string):
    return string in (string + string)[1:-1]
```

An alternative is to use regexp:
```
pattern = re.compile(r"^(\d+)\1+$")
pattern.match(string)
```

### Monotonic Stack

The monotonic stack is a data structure that keeps elements in sorted order. It works like a
regular stack until a push of an item that would break the order, then the stack is popped until
the new element can be pushed in order. Common use cases include finding the next greater or smaller
element in an array. Note that the `compare` function can be more advanced than just simple `<` or
`>`, if needed.

```
class MonotonicStack:
    def __init__(self, compare):
        self.stack = []
        self.compare = compare

    def __repr__(self):
        return ", ".join(str(e) for e in self.stack[::-1])

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        while self.stack and self.compare(self.stack[-1], item):
            self.stack.pop()
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
```
```
x = [1, 7, 9, 5, 8]
increasing_stack = MonotonicStack(operator.ge)
decreasing_stack = MonotonicStack(operator.lt)
for e in x:
    increasing_stack.push(e)
    decreasing_stack.push(e)
print(increasing_stack)
print(decreasing_stack)
>>> 8, 5, 1
>>> 8, 9
```

### Merge Ranges

To merge ranges/intervals the following algorithm can be used:

1. Create events (position, type) for the start end end of each range
2. Sort the events (make sure the "on" events come before the "off" events for equal positions)
3. Iterate the events, for "on" events push to a stack, for "off" events pop from the stack
4. If the stack becomes empty, create a range starting from the popped value, ending at the current position

See day 5.

### Union-Find

Also known as Disjoint-set data structure, is a data structure that can be used to handle subsets
(e.g. components of a graph). It starts in a state where all nodes are disconnected and supports
connecting nodes to subsets in an efficient manner. See day 8 and
https://en.wikipedia.org/wiki/Disjoint-set_data_structure.

```
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
```

## Python

### Range

The built in `range` can be useful for handing ranges.

```
>>> r = range(2,5)
>>> 3 in r
True
>>> len(r)
3
```

### Transpose

To transpose a matrix represented as a list of lists:
```
list(zip(*matrix))
```
