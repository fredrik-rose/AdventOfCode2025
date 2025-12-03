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
