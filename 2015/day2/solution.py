import os


def get_package_sides(x: str) -> int:
    l, w, h = map(int, x.split("x")) # map( int, ...) is necessary, to cast the strings to ints
    lw, wh, hl = l*w, w*h, h*l
    smallest_side = min(lw, wh, hl)
    all_sides = (lw + wh + hl) * 2
    return smallest_side + all_sides


def calculate_all_packages(x: list) -> int:
    whole_size = 0
    for box in x:
        whole_size += get_package_sides(box)
    return whole_size


if __name__ == '__main__':
    assert get_package_sides("2x3x4") == 58, "Error: Example 1 couldn't be solved"
    assert get_package_sides("1x1x10") == 43, "Error: Example 2 couldn't be solved"

    print("All tests passed!")
    puzzle_input = open("input.txt", "r").read().splitlines()
    print("input: ", puzzle_input)
    print("solution: ", calculate_all_packages(puzzle_input))