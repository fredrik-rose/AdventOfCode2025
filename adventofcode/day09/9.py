# Day 9: Movie Theater
import copy
import os
import pathlib


def main():
    points = parse(pathlib.Path(os.path.dirname(__file__)) / "input.txt")
    part_one(copy.deepcopy(points))
    part_two(copy.deepcopy(points))


def parse(file_path):
    points = []
    with open(file_path) as file:
        for line in file:
            x, y = (int(e) for e in line.strip().split(","))
            points.append(x + y * 1j)
    return points


def part_one(points):
    answer = int(max(area for _, __, area in generate_rectangles(points)))
    print(f"Part one: {answer}")


def part_two(points):
    border_points = create_border_points(points)
    border_lines = create_lines(border_points)
    largest = -1
    for a, b, area in generate_rectangles(points):
        if area < largest:
            continue
        valid = True
        for rectangle_line in (
            (a.real + a.imag * 1j, b.real + a.imag * 1j),
            (a.real + b.imag * 1j, b.real + b.imag * 1j),
            (a.real + a.imag * 1j, a.real + b.imag * 1j),
            (b.real + a.imag * 1j, b.real + b.imag * 1j),
        ):
            for border in border_lines:
                if line_intersection(rectangle_line, border):
                    valid = False
                    break
            if not valid:
                break
        if valid and area > largest:
            largest = area
    answer = int(largest)
    print(f"Part two: {answer}")


def generate_rectangles(points):
    for i, a in enumerate(points):
        for b in points[i + 1:]:
            c = a - b
            area = (abs(c.real) + 1) * (abs(c.imag) + 1)
            yield a, b, area


def create_lines(points):
    return list(zip(points, points[1:] + points[:1]))


def create_border_points(points):  # noqa: C901
    border_points = []
    for i, p1 in enumerate(points):
        p2 = points[(i + 1) % len(points)]
        p3 = points[(i + 2) % len(points)]
        d1 = get_line_direction(p1, p2)
        d2 = get_line_direction(p2, p3)
        if d1 == 1:
            if d2 == 1j:  # Right-down corner
                b = p2 + 1 - 1j
            elif d2 == -1j:  # Right-up corner
                b = p2 - 1 - 1j
            else:
                assert False
        elif d1 == -1:
            if d2 == 1j:  # Left-down corner
                b = p2 + 1 + 1j
            elif d2 == -1j:  # Left-up corner
                b = p2 - 1 + 1j
            else:
                assert False
        elif d1 == 1j:
            if d2 == 1:  # Down-right corner
                b = p2 + 1 - 1j
            elif d2 == -1:  # Down-left corner
                b = p2 + 1 + 1j
            else:
                assert False
        elif d1 == -1j:
            if d2 == 1:  # Up-right corner
                b = p2 - 1 - 1j
            elif d2 == -1:  # Up-left corner
                b = p2 - 1 + 1j
            else:
                assert False
        else:
            assert False
        border_points.append(b)
    return border_points


def get_line_direction(start, end):
    diff = end - start
    steps = int(abs(diff))
    assert steps > 0
    direction = diff / steps
    return direction


def line_intersection(a, b):
    if min(a[0].imag, a[1].imag) >= max(b[0].imag, b[1].imag):
        return False
    if min(b[0].imag, b[1].imag) >= max(a[0].imag, a[1].imag):
        return False
    if min(a[0].real, a[1].real) >= max(b[0].real, b[1].real):
        return False
    if min(b[0].real, b[1].real) >= max(a[0].real, a[1].real):
        return False
    return True


if __name__ == "__main__":
    main()
