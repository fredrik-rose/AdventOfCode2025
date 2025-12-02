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
